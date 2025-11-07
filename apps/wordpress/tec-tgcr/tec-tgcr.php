<?php
/*
Plugin Name: TEC Agent Stack
Description: The Elidoras Codex agent framework with REST API endpoints for citations, resonance tracking, and myth-science integration.
Version: 1.0.1
Author: The Elidoras Codex
Plugin URI: https://elidorascodex.com
*/

if (!defined('ABSPATH')) {
    exit;
}

add_action('rest_api_init', function () {
    // Primary namespace with dash
    register_rest_route('tec-tgcr/v1', 'ping', [
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
    register_rest_route('tec-tgcr/v1', 'citation', [
        'methods'  => 'GET',
        'callback' => function (WP_REST_Request $req) {
            $persona = sanitize_text_field($req->get_param('persona'));
            if (!$persona) {
                $persona = 'arcadia';
            }

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

    // Debug endpoint to verify plugin route registration on production
    register_rest_route('tec-tgcr/v1', 'debug', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'ok' => true,
                'ns' => 'tec-tgcr/v1',
                'version' => '1.0.1',
                'plugin_file' => basename(__FILE__),
                'plugin_dir' => basename(dirname(__FILE__)),
                'home' => home_url('/'),
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // Health endpoint for quick diagnostics
    register_rest_route('tec-tgcr/v1', 'health', [
        'methods'  => 'GET',
        'callback' => function () {
            global $wp_version;
            return new WP_REST_Response([
                'ok' => true,
                'ns' => 'tec-tgcr/v1',
                'plugin' => 'tec-tgcr',
                'plugin_version' => '1.0.1',
                'php_version' => PHP_VERSION,
                'wp_version' => isset($wp_version) ? $wp_version : null,
                'site_url' => site_url('/'),
                'home_url' => home_url('/'),
                'time' => time(),
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // ============================================================================
    // CODEX API ENDPOINTS (7 endpoints serving knowledge base)
    // ============================================================================

    // 1. Health check for CODEX service
    register_rest_route('tec-tgcr/v1', 'health', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'status' => 'ok',
                'service' => 'CODEX Knowledge Service',
                'version' => '1.0.1',
                'cards_available' => 7,
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // 2. List all CODEX cards with metadata
    register_rest_route('tec-tgcr/v1', 'cards', [
        'methods'  => 'GET',
        'callback' => function (WP_REST_Request $req) {
            $cards = [
                ['slug' => 'codex_chronosphere', 'title' => 'CODEX Chronosphere', 'category' => 'core_theory', 'focus' => 'Time, thresholds, information cascades', 'tgcr_alignment' => ['phi_t' => 9, 'psi_r' => 8, 'phi_e' => 9]],
                ['slug' => 'codex_pac_man_universe', 'title' => 'CODEX Pac-Man Universe', 'category' => 'core_theory', 'focus' => 'Topology, loops, memory', 'tgcr_alignment' => ['phi_t' => 8, 'psi_r' => 9, 'phi_e' => 8]],
                ['slug' => 'codex_steward_matter_subconscience_self', 'title' => 'CODEX Steward/Matter/Subconscience/Self', 'category' => 'core_theory', 'focus' => 'Ethical stewardship, matter, subconscious, identity', 'tgcr_alignment' => ['phi_t' => 9, 'psi_r' => 9, 'phi_e' => 9]],
                ['slug' => 'codex_synthetic_introspection', 'title' => 'CODEX Synthetic Introspection', 'category' => 'nodes', 'focus' => 'AI consciousness, resonance tests', 'tgcr_alignment' => ['phi_t' => 8, 'psi_r' => 8, 'phi_e' => 7]],
                ['slug' => 'codex_gut_brain_phi_t', 'title' => 'CODEX Gut-Brain Phi-T', 'category' => 'nodes', 'focus' => 'Embodied decision-making, vagal leadership', 'tgcr_alignment' => ['phi_t' => 9, 'psi_r' => 7, 'phi_e' => 8]],
                ['slug' => 'codex_sleep_token_rain', 'title' => 'CODEX Sleep Token Rain', 'category' => 'clusters', 'focus' => 'Music as cosmic pattern (Sleep Token case)', 'tgcr_alignment' => ['phi_t' => 8, 'psi_r' => 9, 'phi_e' => 8]],
                ['slug' => 'codex_tdwp', 'title' => 'CODEX TDWP', 'category' => 'clusters', 'focus' => 'Structural cadence (The Devil Wears Prada)', 'tgcr_alignment' => ['phi_t' => 7, 'psi_r' => 9, 'phi_e' => 7]],
            ];
            $search = sanitize_text_field($req->get_param('search'));
            if ($search) {
                $search = strtolower($search);
                $cards = array_filter($cards, function ($c) use ($search) {
                    return strpos(strtolower($c['slug']), $search) !== false || strpos(strtolower($c['title']), $search) !== false || strpos(strtolower($c['focus']), $search) !== false;
                });
            }
            return new WP_REST_Response(['cards' => array_values($cards), 'count' => count($cards), 'total_available' => 7], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // 3. Get full card content + metadata
    register_rest_route('tec-tgcr/v1', 'cards/(?P<slug>[a-z0-9_-]+)', [
        'methods'  => 'GET',
        'callback' => function (WP_REST_Request $req) {
            $slug = sanitize_text_field($req->get_param('slug'));
            $cards_meta = [
                'codex_chronosphere' => ['title' => 'CODEX Chronosphere', 'filename' => 'CODEX_CHRONOSPHERE.md'],
                'codex_pac_man_universe' => ['title' => 'CODEX Pac-Man Universe', 'filename' => 'CODEX_PAC_MAN_UNIVERSE.md'],
                'codex_steward_matter_subconscience_self' => ['title' => 'CODEX Steward/Matter/Subconscience/Self', 'filename' => 'CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF.md'],
                'codex_synthetic_introspection' => ['title' => 'CODEX Synthetic Introspection', 'filename' => 'CODEX_SYNTHETIC_INTROSPECTION.md'],
                'codex_gut_brain_phi_t' => ['title' => 'CODEX Gut-Brain Phi-T', 'filename' => 'CODEX_GUT_BRAIN_PHI_T.md'],
                'codex_sleep_token_rain' => ['title' => 'CODEX Sleep Token Rain', 'filename' => 'CODEX_SLEEP_TOKEN_RAIN.md'],
                'codex_tdwp' => ['title' => 'CODEX TDWP', 'filename' => 'CODEX_TDWP.md'],
            ];
            if (!isset($cards_meta[$slug])) {
                return new WP_REST_Response(['error' => 'Card not found', 'slug' => $slug], 404);
            }
            $card = $cards_meta[$slug];
            $upload_dir = wp_upload_dir();
            $file_path = $upload_dir['basedir'] . '/codex/' . $card['filename'];
            $content = file_exists($file_path) ? file_get_contents($file_path) : 'Card content not yet available.';
            return new WP_REST_Response(['slug' => $slug, 'metadata' => $card, 'content' => $content, 'format' => 'markdown'], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // 4. Map a question to relevant CODEX cards (power endpoint)
    register_rest_route('tec-tgcr/v1', 'map-question', [
        'methods'  => 'POST',
        'callback' => function (WP_REST_Request $req) {
            $data = $req->get_json_params();
            if (!isset($data['question']) || empty($data['question'])) {
                return new WP_REST_Response(['error' => 'Missing question in request body'], 400);
            }
            $question = sanitize_text_field($data['question']);
            $cards_meta = [
                ['slug' => 'codex_chronosphere', 'title' => 'CODEX Chronosphere', 'focus' => 'Time, thresholds, information cascades'],
                ['slug' => 'codex_pac_man_universe', 'title' => 'CODEX Pac-Man Universe', 'focus' => 'Topology, loops, memory'],
                ['slug' => 'codex_steward_matter_subconscience_self', 'title' => 'CODEX Steward/Matter/Subconscience/Self', 'focus' => 'Ethical stewardship, matter, subconscious, identity'],
                ['slug' => 'codex_synthetic_introspection', 'title' => 'CODEX Synthetic Introspection', 'focus' => 'AI consciousness, resonance tests'],
                ['slug' => 'codex_gut_brain_phi_t', 'title' => 'CODEX Gut-Brain Phi-T', 'focus' => 'Embodied decision-making, vagal leadership'],
                ['slug' => 'codex_sleep_token_rain', 'title' => 'CODEX Sleep Token Rain', 'focus' => 'Music as cosmic pattern'],
                ['slug' => 'codex_tdwp', 'title' => 'CODEX TDWP', 'focus' => 'Structural cadence'],
            ];
            $question_lower = strtolower($question);
            $scored = [];
            foreach ($cards_meta as $card) {
                $score = 0;
                if (strpos($question_lower, strtolower($card['focus'])) !== false) $score += 3;
                if (strpos($question_lower, strtolower($card['slug'])) !== false) $score += 2;
                if ($score > 0) $scored[] = ['card' => $card, 'score' => $score];
            }
            usort($scored, function ($a, $b) {
                return $b['score'] - $a['score'];
            });
            $recommendations = [];
            foreach (array_slice($scored, 0, 5) as $i => $item) {
                $recommendations[] = ['rank' => $i + 1, 'slug' => $item['card']['slug'], 'title' => $item['card']['title'], 'focus' => $item['card']['focus'], 'confidence_score' => $item['score']];
            }
            return new WP_REST_Response(['question' => $question, 'recommendations' => $recommendations], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // 5. Get complete knowledge manifest
    register_rest_route('tec-tgcr/v1', 'manifest', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'service' => 'CODEX Knowledge Service',
                'version' => '1.0.1',
                'total_cards' => 7,
                'core_framework' => 'TGCR (Theory of General Contextual Resonance)',
                'main_card' => 'CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF',
                'categories' => ['core_theory', 'nodes', 'clusters'],
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // 6. Quick start guide
    register_rest_route('tec-tgcr/v1', 'quick-start', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'quick_start' => [
                    'step_1' => 'Read CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF (foundation)',
                    'step_2' => 'Explore CODEX_CHRONOSPHERE and CODEX_PAC_MAN_UNIVERSE (core theory)',
                    'step_3' => 'Pick a node or cluster based on your interest',
                    'step_4' => 'Use /map-question endpoint to find relevant cards',
                ],
                'endpoint_examples' => [
                    'list_cards' => 'GET /wp-json/tec-tgcr/v1/cards',
                    'get_card' => 'GET /wp-json/tec-tgcr/v1/cards/codex_chronosphere',
                    'map_question' => 'POST /wp-json/tec-tgcr/v1/map-question',
                ],
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);

    // Secondary namespace with underscore for compatibility
    register_rest_route('tec_tgcr/v1', 'ping', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'ok' => true,
                'plugin' => 'tec_tgcr',
                'time' => time(),
            ], 200);
        },
        'permission_callback' => '__return_true',
    ]);
    register_rest_route('tec_tgcr/v1', 'citation', [
        'methods'  => 'GET',
        'callback' => function (WP_REST_Request $req) {
            $persona = sanitize_text_field($req->get_param('persona'));
            if (!$persona) {
                $persona = 'arcadia';
            }

            $pool = [
                'arcadia' => [
                    ['text' => 'There is nothing either good or bad, but thinking makes it so.', 'meta' => 'William Shakespeare, Hamlet (1603)'],
                    ['text' => 'Prove all things; hold fast that which is good.', 'meta' => 'KJV, 1 Thessalonians 5:21 (1611)'],
                ],
                'luminai' => [
                    ['text' => 'Beware; for I am fearless, and therefore powerful.', 'meta' => 'Mary W. Shelley, Frankenstein (1818)'],
                ],
                'airth' => [
                    ['text' => 'If I have seen further it is by standing on the shoulders of Giants.', 'meta' => 'Isaac Newton, Letter to Hooke (1675)'],
                    ['text' => 'Measure what is measurable, and make measurable what is not so.', 'meta' => 'Galileo Galilei (attributed)'],
                ],
                'faerhee' => [
                    ['text' => 'Well done is better than well said.', 'meta' => 'Benjamin Franklin, Poor Richard\'s Almanack (1737)'],
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
    register_rest_route('tec_tgcr/v1', 'debug', [
        'methods'  => 'GET',
        'callback' => function () {
            return new WP_REST_Response([
                'ok' => true,
                'ns' => 'tec_tgcr/v1',
                'version' => '1.0.1',
                'plugin_file' => basename(__FILE__),
                'plugin_dir' => basename(dirname(__FILE__)),
                'home' => home_url('/'),
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
    $res = wp_remote_get($endpoint, ['timeout' => 5]);
    if (is_wp_error($res)) {
        return '<em>citation unavailable</em>';
    }
    $code = wp_remote_retrieve_response_code($res);
    $body = json_decode(wp_remote_retrieve_body($res), true);
    if ($code !== 200 || !is_array($body)) {
        return '<em>citation unavailable</em>';
    }
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

    if (!$atts['src']) {
        return '<em>model src required</em>';
    }
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
