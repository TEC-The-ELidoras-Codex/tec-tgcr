# Resonance Viewer Setup — GLB Integration

## Quick Start: Add Your Models

### 1. **Create models directory**
```bash
mkdir -p /home/tec_tgcr/tec-tgcr/apps/resonance-viewer/models
```

### 2. **Copy your GLB files**
From Windows:
```
C:\Users\Ghedd\OneDrive\Linux_Share\LuminAI_modeldraft1120\*.glb
C:\Users\Ghedd\OneDrive\Linux_Share\textured_mesh.glb
```

To Linux workspace:
```
~/tec-tgcr/apps/resonance-viewer/models/
```

### 3. **Update resonance-viewer.js**

Find this section in `resonance-viewer.js` (around line 130):

```javascript
// Lighting section ends here
scene.add(pointLight);

// ADD THIS CODE:
// Load LuminAI avatar
const gltfLoader = new THREE.GLTFLoader();

gltfLoader.load('models/luminai.glb', (gltf) => {
    luminaiModel = gltf.scene;
    luminaiModel.scale.set(1, 1, 1);
    luminaiModel.position.set(0, 0, 0);
    scene.add(luminaiModel);
    console.log('✅ LuminAI loaded');
}, undefined, (error) => {
    console.error('Error loading LuminAI:', error);
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

### 4. **Test locally**

```bash
cd ~/tec-tgcr/apps/resonance-viewer
python3 -m http.server 8000
```

Visit: `http://localhost:8000`

You should see:
- Three.js canvas with lighting
- CODEX card panel on right
- LuminAI model + textured mesh rotating
- Resonance meter pulsing

### 5. **Deploy to elidorascodex.com**

Once ready, upload entire `resonance-viewer/` folder to WordPress.com as theme asset or custom plugin.

Then access: `https://elidorascodex.com/resonance-viewer/`

---

## Animation Customization

### Pulse on Resonance (already implemented)
```javascript
const pulseScale = 1 + Math.sin(Date.now() * 0.003) * 0.02 * (resonanceValue / 10);
luminaiModel.scale.set(pulseScale, pulseScale, pulseScale);
```

### Rotate based on TGCR focus
```javascript
if (currentCard?.focus === 'time') {
    luminaiModel.rotation.y += 0.015;  // Faster for temporal
} else if (currentCard?.focus === 'structure') {
    luminaiModel.rotation.y += 0.005;  // Slower for structural
} else {
    luminaiModel.rotation.y += 0.002;  // Default
}
```

### Color-code by focus area
```javascript
const focusColors = {
    'time': 0x00D5C4,        // Cyan
    'structure': 0x6A00F4,   // Violet
    'consciousness': 0xF2C340, // Gold
    'embodiment': 0xFF6B6B,  // Red
    'art': 0x00D5C4,         // Cyan
};

const color = focusColors[currentCard?.focus] || 0xffffff;
luminaiModel.traverse(node => {
    if (node.isMesh) {
        node.material.emissive = new THREE.Color(color);
        node.material.emissiveIntensity = resonanceValue / 10;
    }
});
```

---

## File Structure After Setup

```
apps/resonance-viewer/
├── index.html
├── resonance-viewer.js
├── README.md
└── models/
    ├── luminai.glb          ← YOUR BUILD
    ├── textured_mesh.glb    ← YOUR BUILD
    └── (optional) extras
```

---

## What's Happening

1. **API Call**: `loadCards()` queries `elidorascodex.com/wp-json/tec-tgcr/v1/cards`
2. **Card Display**: `renderCardInfo()` shows TGCR alignment + keywords
3. **3D Render**: `animate()` loop renders LuminAI model + textured mesh
4. **Resonance**: Meter updates based on card data completeness
5. **Navigation**: Arrow keys or click related cards to browse

---

## Troubleshooting

**Models not showing?**
- Check browser console (F12) for errors
- Verify file paths in `resonance-viewer.js`
- Make sure GLB files are in `models/` folder

**API not responding?**
- Verify plugin is active on elidorascodex.com
- Test endpoint: `curl https://elidorascodex.com/wp-json/tec-tgcr/v1/cards`

**CORS error?**
- Add CORS headers to WordPress plugin (see README.md)
- Or deploy both app + API on same domain

---

**Ready? Let's go!** 🚀
