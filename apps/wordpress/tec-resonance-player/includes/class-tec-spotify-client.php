<?php
namespace TEC\Resonance;

if (!defined('ABSPATH')) { exit; }

class Spotify_Client {
    private $client_id;
    private $client_secret;
    private $token;
    private $token_expires_at = 0;

    public function __construct($client_id = null, $client_secret = null) {
        // Prefer TEC_* constants, fallback to generic SPOTIFY_* if set
        $cid = '';
        if (\defined('TEC_SPOTIFY_CLIENT_ID')) { $cid = \constant('TEC_SPOTIFY_CLIENT_ID'); }
        elseif (\defined('SPOTIFY_CLIENT_ID')) { $cid = \constant('SPOTIFY_CLIENT_ID'); }

        $cs = '';
        if (\defined('TEC_SPOTIFY_CLIENT_SECRET')) { $cs = \constant('TEC_SPOTIFY_CLIENT_SECRET'); }
        elseif (\defined('SPOTIFY_CLIENT_SECRET')) { $cs = \constant('SPOTIFY_CLIENT_SECRET'); }

        $this->client_id = $client_id ?: $cid;
        $this->client_secret = $client_secret ?: $cs;
    }

    private function ensure_token() {
        if (empty($this->client_id) || empty($this->client_secret)) {
            throw new \Exception('Spotify credentials missing: set TEC_SPOTIFY_CLIENT_ID/TEC_SPOTIFY_CLIENT_SECRET (or SPOTIFY_CLIENT_ID/SPOTIFY_CLIENT_SECRET) in wp-config.php');
        }
        if (time() < $this->token_expires_at - 30 && $this->token) return;
        $resp = \wp_remote_post('https://accounts.spotify.com/api/token', [
            'timeout' => 15,
            'headers' => [ 'Content-Type' => 'application/x-www-form-urlencoded' ],
            'body' => http_build_query([
                'grant_type' => 'client_credentials',
                'client_id' => $this->client_id,
                'client_secret' => $this->client_secret,
            ]),
        ]);
        if (\is_wp_error($resp)) throw new \Exception('Spotify token error: ' . $resp->get_error_message());
        $code = \wp_remote_retrieve_response_code($resp);
        $body = json_decode(\wp_remote_retrieve_body($resp), true);
        if ($code !== 200 || empty($body['access_token'])) {
            $msg = isset($body['error_description']) ? $body['error_description'] : \wp_remote_retrieve_body($resp);
            throw new \Exception('Spotify token failed: ' . $msg);
        }
        $this->token = $body['access_token'];
        $this->token_expires_at = time() + intval($body['expires_in'] ?? 3600);
    }

    public function get_audio_features(array $track_ids) {
        $this->ensure_token();
        $ids = implode(',', array_slice(array_map('trim', $track_ids), 0, 100));
        $url = 'https://api.spotify.com/v1/audio-features?ids=' . rawurlencode($ids);
        $resp = \wp_remote_get($url, [
            'timeout' => 15,
            'headers' => [ 'Authorization' => 'Bearer ' . $this->token ],
        ]);
        if (\is_wp_error($resp)) throw new \Exception('Spotify API error: ' . $resp->get_error_message());
        $code = \wp_remote_retrieve_response_code($resp);
        $body = json_decode(\wp_remote_retrieve_body($resp), true);
        if ($code !== 200) throw new \Exception('Spotify API failed: ' . \wp_remote_retrieve_body($resp));
        return $body['audio_features'] ?? [];
    }
}
