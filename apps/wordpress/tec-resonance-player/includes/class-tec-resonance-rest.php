<?php
namespace TEC\Resonance;

if (!defined('ABSPATH')) { exit; }

class Resonance_Rest {
    public static function register_routes() {
        register_rest_route('tec/v1', '/resonance', [
            'methods' => 'POST',
            'callback' => [__CLASS__, 'handle_resonance'],
            'permission_callback' => '__return_true', // Public – only returns computed features
            'args' => [
                'trackIds' => [ 'required' => true ],
            ],
        ]);
    }

    public static function handle_resonance($request) {
        $params = $request->get_json_params();
        $ids = isset($params['trackIds']) && is_array($params['trackIds']) ? array_values(array_filter($params['trackIds'])) : [];
        if (empty($ids)) {
            return new \WP_REST_Response(['error' => 'trackIds required'], 400);
        }

        // If ARCADIA is configured, proxy and return
        if (\defined('TEC_ARCADIA_URL') && TEC_ARCADIA_URL) {
            $resp = \wp_remote_post(TEC_ARCADIA_URL, [
                'timeout' => 20,
                'headers' => ['Content-Type' => 'application/json'],
                'body' => wp_json_encode(['trackIds' => $ids]),
            ]);
            if (\is_wp_error($resp)) {
                return new \WP_REST_Response(['error' => $resp->get_error_message()], 500);
            }
            $code = \wp_remote_retrieve_response_code($resp);
            $body = json_decode(\wp_remote_retrieve_body($resp), true);
            return new \WP_REST_Response($body, $code ?: 200);
        }

        // Else compute locally via Spotify audio features
        try {
            $client = new Spotify_Client();
            $features = $client->get_audio_features($ids);
            $out = [];
            foreach ($features as $f) {
                if (!$f) { $out[] = null; continue; }
                // Map Spotify features to OXY/DOP/ADR (example heuristic)
                // Values 0-100
                $energy = floatval($f['energy'] ?? 0);
                $valence = floatval($f['valence'] ?? 0);
                $dance = floatval($f['danceability'] ?? 0);
                $tempo = floatval($f['tempo'] ?? 0);
                $acoustic = floatval($f['acousticness'] ?? 0);
                $inst = floatval($f['instrumentalness'] ?? 0);

                // Simple projection; tailor later
                $OXY = round( clamp01(0.55*val($valence) + 0.25*val($dance) + 0.2*inv($acoustic)) * 100 );
                $DOP = round( clamp01(0.6*val($energy) + 0.25*norm($tempo, 60, 160) + 0.15*inv($inst)) * 100 );
                $ADR = round( clamp01(0.5*inv($valence) + 0.3*val($energy) + 0.2*norm($tempo, 80, 200)) * 100 );

                $out[] = [
                    'trackId' => $f['id'] ?? null,
                    'features' => $f,
                    'resonance' => [ 'OXY' => $OXY, 'DOP' => $DOP, 'ADR' => $ADR ],
                ];
            }
            return new \WP_REST_Response(['out' => $out], 200);
        } catch (\Exception $e) {
            return new \WP_REST_Response(['error' => $e->getMessage()], 500);
        }
    }
}

// Helper functions (global namespace safe wrappers)
if (!function_exists('TEC\\Resonance\\clamp01')) {
    function clamp01($x) { return max(0.0, min(1.0, $x)); }
}
if (!function_exists('TEC\\Resonance\\val')) {
    function val($x) { return max(0.0, min(1.0, floatval($x))); }
}
if (!function_exists('TEC\\Resonance\\inv')) {
    function inv($x) { $v = val($x); return 1.0 - $v; }
}
if (!function_exists('TEC\\Resonance\\norm')) {
    function norm($x, $min, $max) {
        $x = floatval($x); $min = floatval($min); $max = floatval($max);
        if ($max <= $min) return 0.0;
        $n = ($x - $min) / ($max - $min);
        return clamp01($n);
    }
}
