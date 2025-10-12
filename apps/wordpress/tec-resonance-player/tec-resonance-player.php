<?php
/**
 * Plugin Name: TEC Resonance Player (API)
 * Description: Adds a secure REST endpoint for resonance analysis using Spotify Client Credentials and a /spotify/callback route. Pair with the Resonance Player front-end.
 * Version: 0.1.0
 * Author: TEC • The Elidoras Codex
 */

if (!defined('ABSPATH')) { exit; }

// Constants can be set in wp-config.php for security (recommended)
// define('TEC_SPOTIFY_CLIENT_ID', '');
// define('TEC_SPOTIFY_CLIENT_SECRET', '');
// Optionally point to an external ARCADIA back-end; if set, /resonance will proxy to it
// define('TEC_ARCADIA_URL', 'https://your-arcadia.example/resonance');

// Autoload minimal classes
require_once __DIR__ . '/includes/class-tec-spotify-client.php';
require_once __DIR__ . '/includes/class-tec-resonance-rest.php';

// Pretty URL for /spotify/callback -> plugin callback template
add_action('init', function () {
    add_rewrite_tag('%tec_spotify_cb%', '1');
    add_rewrite_rule('^spotify/callback/?$', 'index.php?tec_spotify_cb=1', 'top');
});

register_activation_hook(__FILE__, function () {
    // Ensure rewrite takes effect after plugin activation
    flush_rewrite_rules();
});

register_deactivation_hook(__FILE__, function () {
    flush_rewrite_rules();
});

// Route the callback to a minimal handler page
add_action('template_redirect', function () {
    if (get_query_var('tec_spotify_cb')) {
        status_header(200);
        nocache_headers();
        include __DIR__ . '/public/callback.php';
        exit;
    }
});

// Register REST route
add_action('rest_api_init', function () {
    \TEC\Resonance\Resonance_Rest::register_routes();
});

// Optional shortcode: [tec_resonance_player_hint]
// Provides a small hint block with the correct REST URL for debugging/embedding
add_shortcode('tec_resonance_player_hint', function () {
    $rest_url = esc_html( get_rest_url(null, 'tec/v1/resonance') );
    ob_start();
    ?>
    <div class="tec-resonance-hint" style="padding:12px;border:1px solid rgba(0,0,0,.1);border-radius:8px;">
      <strong>TEC Resonance API:</strong>
      <code><?php echo $rest_url; ?></code>
      <div style="opacity:.8;font-size:12px;margin-top:6px;">POST JSON {"trackIds":["<22-char id>"]}</div>
    </div>
    <?php
    return ob_get_clean();
});
