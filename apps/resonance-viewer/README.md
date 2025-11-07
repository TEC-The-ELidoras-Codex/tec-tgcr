# TEC Resonance Viewer

Interactive 3D CODEX card viewer with real-time resonance visualization.

## Features

✅ **Live API Integration** — Queries TEC API at `elidorascodex.com/wp-json/tec-tgcr/v1/`
✅ **Card Browser** — Navigate CODEX cards with keyboard (← →) or click related cards
✅ **TGCR Visualization** — Displays φᵗ, ψʳ, Φᴱ alignment for each card
✅ **Resonance Meter** — Real-time metric showing card engagement level
✅ **3D Scene** — Three.js rendering with lighting, fog, and smooth animations

## Architecture

```
resonance-viewer/
├── index.html              # UI layout + styling
├── resonance-viewer.js     # Main app logic + API client
├── models/
│   ├── luminai.glb         # LuminAI avatar geometry (your build)
│   ├── textured_mesh.glb   # Textured mesh overlay
│   └── chrono_aura.glb     # Chronosphere indicator sphere (optional)
└── README.md
```

## Integration: Adding Your GLB Models

### Step 1: Copy Models

```bash
# From your OneDrive Linux Share
cp "C:\Users\Ghedd\OneDrive\Linux_Share\LuminAI_modeldraft1120\*.glb" apps/resonance-viewer/models/
cp "C:\Users\Ghedd\OneDrive\Linux_Share\textured_mesh.glb" apps/resonance-viewer/models/
```

### Step 2: Update resonance-viewer.js

In the `initThreeJS()` function, add model loading:

```javascript
// Load LuminAI avatar
const gltfLoader = new THREE.GLTFLoader();

gltfLoader.load('models/luminai.glb', (gltf) => {
    luminaiModel = gltf.scene;
    luminaiModel.scale.set(1, 1, 1);
    luminaiModel.position.set(0, 0, 0);
    scene.add(luminaiModel);

    console.log('✅ LuminAI loaded');
});

// Optional: Load textured mesh overlay
gltfLoader.load('models/textured_mesh.glb', (gltf) => {
    const mesh = gltf.scene;
    mesh.scale.set(0.95, 0.95, 0.95);
    mesh.position.z = 0.1;
    scene.add(mesh);

    console.log('✅ Textured mesh loaded');
});
```

### Step 3: Resonance Animation

The `animate()` function already pulses the model based on resonance:

```javascript
// Pulse intensity = resonance value
const pulseScale = 1 + Math.sin(Date.now() * 0.003) * 0.02 * (resonanceValue / 10);
luminaiModel.scale.set(pulseScale, pulseScale, pulseScale);
```

You can add more animations:

```javascript
// Example: Rotate based on φᵗ (temporal attention)
if (currentCard?.tgcr_alignment?.phi_t) {
    luminaiModel.rotation.z += 0.01 * (resonanceValue / 10);
}

// Example: Color shift based on focus
if (currentCard?.focus === 'time') {
    // Apply cyan glow
} else if (currentCard?.focus === 'structure') {
    // Apply violet glow
}
```

## API Endpoints Used

- `GET /cards` — List all CODEX cards
- `GET /cards/{slug}` — Get card details with TGCR alignment
- `POST /guidance/map` — Map questions to cards (future)
- `GET /cards/{slug}/sections` — Get card sections (future)

## Deployment

### Local Testing

```bash
cd apps/resonance-viewer
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Deploy to WordPress.com (as plugin asset)

```bash
# Add resonance viewer to theme or custom plugin
# Serve from elidorascodex.com/resonance-viewer/
```

### Deploy as Standalone App

```bash
# Use Vercel, Netlify, or GitHub Pages
# Ensure CORS is enabled on elidorascodex.com
```

## CORS Configuration

If running locally and hitting API errors, enable CORS:

Add to WordPress plugin (`tec-codex-api-plugin.php`):

```php
add_action( 'rest_api_init', function() {
    header( 'Access-Control-Allow-Origin: *' );
    header( 'Access-Control-Allow-Methods: GET, POST, OPTIONS' );
    header( 'Access-Control-Allow-Headers: Content-Type, Authorization' );
} );
```

## Next Steps

1. ✅ Copy your GLB files to `models/`
2. 📝 Update `resonance-viewer.js` with model loading code
3. 🎨 Customize animations for each TGCR dimension
4. 🚀 Deploy to elidorascodex.com
5. 🔗 Link from ChatGPT Resonance GPT as action

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Credits

- **API**: TEC Knowledge API
- **3D Engine**: Three.js
- **Models**: LuminAI (your build)
- **Data**: CODEX TGCR Framework

---

**Light learns by listening.** — TEC
