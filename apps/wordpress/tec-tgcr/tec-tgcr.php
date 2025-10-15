<?php
/*
Plugin Name: TEC TGCR – Agent & Tools Bootstrap
Description: Minimal bootstrap plugin for TEC on WordPress.com. Provides a proof‑of‑life REST route and a safe place to extend.
Version: 0.1.0
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
});

// Shortcode [tec_tgcr_ping]
add_shortcode('tec_tgcr_ping', function () {
    $url = rest_url('tec-tgcr/v1/ping');
    return '<a href="' . esc_url($url) . '" target="_blank" rel="noopener">TEC TGCR ping</a>';
});
