# Local Testing Guide for Resonance Viewers

## Quick Start

### Prerequisites

- Python 3.8+
- Modern browser (Chrome, Firefox, Safari, Edge)
- Terminal/PowerShell access

### Test Both Viewers Locally

```bash
# Navigate to apps directory
cd ~/tec-tgcr/apps

# Start local HTTP server
python3 -m http.server 8000

# In browser, visit:
# http://localhost:8000/resonance-viewer/
# http://localhost:8000/star-viewer/
```

**Note**: Both viewers will fetch live data from `https://elidorascodex.com/wp-json/tec-tgcr/v1/`

---

## Resonance Viewer Testing Checklist

### ✅ Initialization

- [ ] Canvas loads, shows cyan glow point light
- [ ] Browser console shows: `✅ Loaded [N] CODEX cards`
- [ ] "codex_chronosphere" card displays on right panel

### ✅ API Integration

- [ ] Card info shows:
  - Title (e.g., "Chronosphere: Temporal Navigation in TGCR")
  - Category + Focus
  - TGCR alignment (φᵗ, ψʳ, Φᴱ)
  - Keywords list
  - Related cards

### ✅ Animation

- [ ] Resonance sphere pulsing (smooth, not jerky)
- [ ] Rotation smooth and continuous
- [ ] No errors in browser console

### ✅ Controls (Keyboard)

- [ ] **Arrow Up/Down**: Navigate between cards
- [ ] **Space**: Log current resonance score
- [ ] **Q**: Increase animation speed
- [ ] **E**: Decrease animation speed

### ✅ GLB Integration (Once Models Added)

- [ ] `models/luminai.glb` loads as avatar
- [ ] `models/textured_mesh.glb` loads and rotates
- [ ] Both models visible against resonance sphere background
- [ ] Animations respond to card selection

---

## Star Viewer Testing Checklist

### ✅ Initialization

- [ ] Starfield canvas loads (deep navy background)
- [ ] Background stars visible (violet, decorative)
- [ ] Browser console shows: `✅ Loaded [N] CODEX cards`
- [ ] HUD displays: star count, zoom level, focus type

### ✅ API Integration

- [ ] Each card appears as a star (glowing octahedron)
- [ ] Stars color-coded by focus:
  - Cyan (#00D5C4) = time
  - Violet (#6A00F4) = structure
  - Gold (#F2C340) = consciousness
  - Pink (#FF6B6B) = embodiment
- [ ] Constellation lines connect related cards (cyan lines, low opacity)

### ✅ Interaction

- [ ] **Click on star**: Card details load in right panel
- [ ] **Arrow keys** (left/right): Navigate between cards
- [ ] **Scroll wheel**: Zoom in/out (zoom level HUD updates)
- [ ] **WASD keys**: Pan camera around starfield
- [ ] **R key**: Reset camera to origin

### ✅ Card Information Panel

- [ ] Selected star scales up (1.5x larger)
- [ ] Card title, category, focus display
- [ ] TGCR alignment visible (φᵗ, ψʳ, Φᴱ)
- [ ] Keywords rendered as cyan badges
- [ ] "Connected Stars" section shows related cards
- [ ] Clicking related star selects that star (constellation navigation)

### ✅ Animation

- [ ] All stars gently rotating (spin x + spin y)
- [ ] Glow pulsing smoothly (Math.sin based)
- [ ] No frame drops or stuttering
- [ ] No console errors

---

## Debugging Tips

### Star Viewer - Stars Not Appearing

1. Check browser console for CORS errors
2. Verify API endpoint: `curl https://elidorascodex.com/wp-json/tec-tgcr/v1/cards`
3. Check that cards array is populated: `console.log(cards)` in dev tools
4. Verify Three.js loaded: `console.log(THREE)` should show version

### Resonance Viewer - Models Not Rendering

1. Copy GLB files to `apps/resonance-viewer/models/`

   ```bash
   mkdir -p apps/resonance-viewer/models
   # Copy luminai.glb and textured_mesh.glb from OneDrive
   ```

2. Uncomment GLB_INTEGRATION_TEMPLATE.js code in resonance-viewer.js
3. Check console for loader errors
4. Verify file paths: `console.log(window.location)` in dev tools

### Both Viewers - Slow Performance

1. Check GPU usage: Browser Dev Tools → Performance tab
2. Reduce star count temporarily: Edit `starCount` in star-viewer.js
3. Disable constellation lines: Comment out `drawConstellations()` call
4. Check network latency: Open Dev Tools → Network tab, reload

### API Connection Refused

1. Verify elidorascodex.com is reachable: `curl -I https://elidorascodex.com`
2. Check WordPress plugin status: Login to elidorascodex.com → Plugins
3. Verify plugin is activated: Should show "TEC - The Elidoras Codex"
4. Test endpoint directly: `curl https://elidorascodex.com/wp-json/tec-tgcr/v1/cards`

---

## Performance Baseline

On modern hardware (Ryzen 5+, RTX 2070+):

| Metric | Target | Acceptable |
|--------|--------|------------|
| Frame Rate | 60 fps | 30+ fps |
| Load Time | <2s | <5s |
| Star Count | 8 total (CODEX) | - |
| Memory | <50MB | <150MB |
| GPU Utilization | 15-25% | <50% |

---

## Integration Steps (Before Live Deployment)

### Step 1: Copy GLB Models

```bash
mkdir -p apps/resonance-viewer/models
# Copy from OneDrive:
cp /path/to/LuminAI_modeldraft1120/*.glb apps/resonance-viewer/models/
cp /path/to/textured_mesh.glb apps/resonance-viewer/models/
```

### Step 2: Integrate GLB Code

1. Open `apps/resonance-viewer/resonance-viewer.js`
2. Find: `// INSERT GLB INTEGRATION CODE HERE`
3. Copy relevant sections from `apps/resonance-viewer/GLB_INTEGRATION_TEMPLATE.js`
4. Paste into resonance-viewer.js after the lighting setup

### Step 3: Test Locally

```bash
cd apps/resonance-viewer
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Step 4: Test Star Viewer

```bash
cd apps/star-viewer
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Step 5: Test Navigation

- [ ] Both viewers load
- [ ] API data fetches successfully
- [ ] Cards display correctly
- [ ] All interactions responsive
- [ ] No console errors

### Step 6: Build Priority 1 3D Assets (Optional)

If you want animated TGCR symbols:

1. Open Blender
2. Create 4 simple geometric models (see `apps/3D_ASSETS_SPEC.md`)
3. Export as glTF 2.0 (.glb) to `apps/star-viewer/models/tgcr/`
4. Update star-viewer.js to load and position them

---

## Deployment to elidorascodex.com

Once verified locally:

### Option 1: Direct Upload to WordPress

1. Login to WordPress.com admin
2. Navigate: Tools → File Manager
3. Upload both `apps/resonance-viewer/` and `apps/star-viewer/` directories
4. Access via: `https://elidorascodex.com/resonance-viewer/`

### Option 2: Git Deploy (if repository connected)

```bash
git push origin research/resonance-agent
# Configure GitHub Actions to deploy to elidorascodex.com
```

### Option 3: Manual SFTP (if SFTP access available)

```bash
# From local machine:
scp -r apps/resonance-viewer/ user@elidorascodex.com:/var/www/html/
scp -r apps/star-viewer/ user@elidorascodex.com:/var/www/html/
```

---

## Verification Checklist (Before Going Live)

- [ ] Resonance Viewer: Models render, card selection works
- [ ] Star Viewer: Constellation loads, click navigation smooth
- [ ] Both: Real-time API queries from live endpoint
- [ ] Both: No console errors in production
- [ ] Both: Responsive on desktop (1920x1080, 1280x720)
- [ ] Both: Frame rate consistent 30+ fps
- [ ] API: All 8 endpoints responding
- [ ] Docs: `SETUP.md`, `README.md` accurate and linked

---

## Next Steps

1. **This Hour**: Test both viewers locally at `http://localhost:8000`
2. **Today**: Copy GLB models from OneDrive; integrate into Resonance Viewer
3. **This Week**: Build Priority 1 3D assets (if desired)
4. **End of Week**: Deploy both viewers to elidorascodex.com
5. **Next Week**: Link from ChatGPT Resonance GPT as interactive 3D portal

**Questions?** Check browser console for detailed error messages, or review Star Viewer JS source (~403 lines with comments).
