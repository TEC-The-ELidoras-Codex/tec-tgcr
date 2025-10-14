<?php
/**
 * Plugin Name: TEC LuminAI Agent
 * Description: Server-side agent proxy and lightweight chat UI for TEC. Exposes /wp-json/tec/v1/agent to call OpenAI or Azure OpenAI using keys stored in wp-config.php. Shortcode: [tec_luminai_agent]
 * Version: 0.1.0
 * Author: The Elidoras Codex
 */

if (!defined('ABSPATH')) { exit; }

// Constants you can set in wp-config.php (examples in README.md)
// define('TEC_OPENAI_API_KEY', '');
// define('TEC_OPENAI_API_BASE', 'https://api.openai.com/v1');
// define('TEC_OPENAI_MODEL', 'gpt-4o-mini');
// Azure OpenAI optional:
// define('AZURE_OPENAI_ENDPOINT', '');
// define('AZURE_OPENAI_KEY', '');
// define('AZURE_OPENAI_VERSION', '2024-05-01-preview');
// define('AZURE_OPENAI_DEPLOYMENT_NAME', '');

require_once __DIR__ . '/includes/class-tec-luminai-agent.php';

// REST route (guarded for non-WP static analyzers)
if (function_exists('add_action') && function_exists('register_rest_route')) {
  call_user_func('add_action', 'rest_api_init', function () {
    call_user_func('register_rest_route', 'tec/v1', '/agent', [
      'methods'  => 'POST',
      'callback' => ['TEC_LuminAI_Agent', 'handle_request'],
      'permission_callback' => ['TEC_LuminAI_Agent', 'permission_check'],
    ]);
  });
}

// Shortcode UI
if (function_exists('add_shortcode')) call_user_func('add_shortcode', 'tec_luminai_agent', function ($atts) {
  $atts = function_exists('shortcode_atts') ? call_user_func('shortcode_atts', [
        'placeholder' => 'Ask Lumina…',
        'button' => 'Send',
  ], $atts, 'tec_luminai_agent') : array_merge([
    'placeholder' => 'Ask Lumina…',
    'button' => 'Send',
  ], is_array($atts) ? $atts : []);

    ob_start();
    ?>
    <div id="tec-luminai-agent" style="--tec-bg:#0b1e3b;--tec-teal:#00d5c4;--tec-gold:#f2c340;max-width:720px;margin:1rem auto;padding:1rem;border:1px solid #e5e7eb;border-radius:12px;background:#fff">
      <div id="tec-agent-log" style="height:280px;overflow:auto;border:1px solid #eee;border-radius:8px;padding:.75rem;margin-bottom:.75rem;background:#fafafa"></div>
      <div style="display:flex;gap:.5rem">
  <textarea id="tec-agent-input" rows="2" style="flex:1;resize:vertical" placeholder="<?php echo function_exists('esc_attr') ? call_user_func('esc_attr', $atts['placeholder']) : htmlspecialchars($atts['placeholder'], ENT_QUOTES); ?>"></textarea>
  <button id="tec-agent-send" style="background:var(--tec-teal);color:#003;border:none;padding:.5rem 1rem;border-radius:8px;cursor:pointer"><?php echo function_exists('esc_html') ? call_user_func('esc_html', $atts['button']) : htmlspecialchars($atts['button'], ENT_QUOTES); ?></button>
      </div>
      <small style="display:block;margin-top:.5rem;color:#666">Server-side: keys are stored safely in wp-config.php. Endpoint: /wp-json/tec/v1/agent</small>
    </div>
    <script>
      (function(){
        const log = document.getElementById('tec-agent-log');
        const input = document.getElementById('tec-agent-input');
        const send = document.getElementById('tec-agent-send');
        const restUrl = <?php
          $url = function_exists('rest_url') ? call_user_func('rest_url', 'tec/v1/agent') : '/wp-json/tec/v1/agent';
          echo json_encode($url);
        ?>;
        function add(role, text){
          const el = document.createElement('div');
          el.style.margin = '.25rem 0';
          el.innerHTML = '<strong>'+role+':</strong> ' + (text||'');
          log.appendChild(el); log.scrollTop = log.scrollHeight;
        }
        async function callAgent(prompt){
          try {
            const resp = await fetch(restUrl, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ messages: [{ role: 'user', content: String(prompt||'') }] })
            });
            const data = await resp.json();
            const txt = (data && data.reply) ? data.reply : JSON.stringify(data);
            add('Lumina', txt);
          } catch (e) {
            add('Error', String(e));
          }
        }
        send.addEventListener('click', ()=>{ const q = input.value.trim(); if(q){ add('You', q); input.value=''; callAgent(q); }});
        input.addEventListener('keydown', (e)=>{ if(e.key==='Enter' && (e.ctrlKey||e.metaKey)){ e.preventDefault(); send.click(); } });
      })();
    </script>
    <?php
    return ob_get_clean();
});
