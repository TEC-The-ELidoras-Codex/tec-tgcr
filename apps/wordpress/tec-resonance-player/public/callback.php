<?php
// Minimal OAuth callback landing page for Spotify Authorization Code (PKCE-ready)
// For now, we just echo the parameters so you can verify redirect works.
?><!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Spotify Callback • TEC</title>
  <style>
    body{font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif;margin:0;padding:24px;background:#0b1e3b;color:#e6f0ff}
    .card{max-width:840px;margin:0 auto;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:20px}
    code,pre{background:rgba(0,0,0,.35);padding:6px 8px;border-radius:8px}
  </style>
  <script>
    (function(){
      const params = new URLSearchParams(location.search);
      const out = {};
      params.forEach((v,k)=>out[k]=v);
      document.addEventListener('DOMContentLoaded',()=>{
        document.getElementById('dump').textContent = JSON.stringify(out,null,2);
      });
    })();
  </script>
  </head>
<body>
  <div class="card">
    <h1>Spotify Callback</h1>
    <p>Redirect received. If implementing PKCE, your front-end can read these params and exchange the code server-side.</p>
    <pre id="dump">{}<\/pre>
  </div>
</body>
</html>