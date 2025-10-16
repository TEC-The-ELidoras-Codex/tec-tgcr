<?php
/*
Plugin Name: TEC TGCR – Agent & Tools Bootstrap
Description: Minimal bootstrap plugin for TEC on WordPress.com. Provides a proof‑of‑life REST route and a safe place to extend.
Version: 0.1.1
Author: TEC – The ELidoras Codex
*/

if (!defined('ABSPATH')) { exit; }

add_action('rest_api_init', function () {
    register_rest_route('tec-tgcr/v1', '/ping', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'ok' => true,
                'plugin' => 'tec-tgcr',
                'time' => time(),
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // Public-domain citation endpoint: /wp-json/tec-tgcr/v1/citation?persona=luminai
    register_rest_route('tec-tgcr/v1', '/citation', [
        'methods'  => 'GET',
        'callback' => function (WP_REST_Request $req) {
            $persona = sanitize_text_field($req->get_param('persona'));
            if (!$persona) { $persona = 'arcadia'; }

            // Minimal PD pool, matching docs/templates/public_domain_citations.yml
            $pool = [
                'arcadia' => [
                    [
                        'text' => 'There is nothing either good or bad, but thinking makes it so.',
                        'meta' => 'William Shakespeare, Hamlet (1603)'
                    ],
                    [
                        'text' => 'Prove all things; hold fast that which is good.',
                        'meta' => 'KJV, 1 Thessalonians 5:21 (1611)'
                    ],
                ],
                'luminai' => [
                    [
                        'text' => 'Beware; for I am fearless, and therefore powerful.',
                        'meta' => 'Mary W. Shelley, Frankenstein (1818)'
                    ],
                ],
                'airth' => [
                    [
                        'text' => 'If I have seen further it is by standing on the shoulders of Giants.',
                        'meta' => 'Isaac Newton, Letter to Hooke (1675)'
                    ],
                    [
                        'text' => 'Measure what is measurable, and make measurable what is not so.',
                        'meta' => 'Galileo Galilei (attributed)'
                    ],
                ],
                'faerhee' => [
                    [
                        'text' => 'Well done is better than well said.',
                        'meta' => 'Benjamin Franklin, Poor Richard\'s Almanack (1737)'
                    ],
                ],
            ];

            $key = strtolower($persona);
            $choices = isset($pool[$key]) ? $pool[$key] : $pool['arcadia'];
            $quote = $choices[array_rand($choices)];
            return new WP_REST_Response([
                'persona' => $key,
                'text' => $quote['text'],
                'meta' => $quote['meta'],
                'public_domain' => true,
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);
});

// Shortcode [tec_tgcr_ping]
add_shortcode('tec_tgcr_ping', function () {
    $url = rest_url('tec-tgcr/v1/ping');
    return '<a href="' . esc_url($url) . '" target="_blank" rel="noopener">TEC TGCR ping</a>';
});

// Shortcode [tec_tgcr_citation persona="luminai"]
add_shortcode('tec_tgcr_citation', function ($atts) {
    $atts = shortcode_atts(['persona' => 'arcadia'], $atts, 'tec_tgcr_citation');
    $persona = sanitize_text_field($atts['persona']);
    $endpoint = add_query_arg('persona', $persona, rest_url('tec-tgcr/v1/citation'));

    // Server-side fetch to avoid client exposing anything; no secrets used.
    $res = wp_remote_get($endpoint, [ 'timeout' => 5 ]);
    if (is_wp_error($res)) { return '<em>citation unavailable</em>'; }
    $code = wp_remote_retrieve_response_code($res);
    $body = json_decode(wp_remote_retrieve_body($res), true);
    if ($code !== 200 || !is_array($body)) { return '<em>citation unavailable</em>'; }
    $text = esc_html($body['text'] ?? '');
    $meta = esc_html($body['meta'] ?? '');
    return '<blockquote class="tec-tgcr-citation">' . $text . '<br><small>' . $meta . '</small></blockquote>';
});

// Shortcode to embed a GLB/GLTF model using <model-viewer>
// Usage: [tec_tgcr_model src="/wp-content/uploads/lumina.glb" autoplay="1" camera="auto"]
add_shortcode('tec_tgcr_model', function ($atts) {
    $atts = shortcode_atts([
        'src' => '',
        'poster' => '',
        'autoplay' => '1',
        'camera' => 'auto',
        'ar' => '0',
        'exposure' => '1.0',
        'skybox' => '',
        'style' => 'width:100%;height:500px;'
    ], $atts, 'tec_tgcr_model');

    if (!$atts['src']) { return '<em>model src required</em>'; }
    $src = esc_url($atts['src']);
    $poster = esc_url($atts['poster']);
    $autoplay = $atts['autoplay'] === '1' ? 'autoplay' : '';
    $camera = $atts['camera'] === 'auto' ? 'camera-controls' : '';
    $ar = $atts['ar'] === '1' ? 'ar' : '';
    $exposure = esc_attr($atts['exposure']);
    $skybox = $atts['skybox'] ? 'skybox-image="' . esc_url($atts['skybox']) . '"' : '';
    $style = esc_attr($atts['style']);

    // Load model-viewer (ES module) once per page
    wp_enqueue_script('model-viewer', 'https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js', [], null, true);

    $posterAttr = $poster ? 'poster="' . $poster . '"' : '';
    $html = '<model-viewer src="' . $src . '" ' . $posterAttr . ' ' . $autoplay . ' ' . $camera . ' ' . $ar . ' exposure="' . $exposure . '" ' . $skybox . ' style="' . $style . '" shadow-intensity="0.7" disable-zoom="false" interaction-prompt="auto"></model-viewer>';
    return $html;
});
