# TEC 3D Asset Library

**Build these assets for the Star Viewer + Resonance Viewer**

## Core Assets

### 1. **TGCR Dimension Markers** (Essential)

Each TGCR variable needs a 3D symbol:

```
φᵗ (Temporal Attention)
├── Shape: Rotating helix/spiraled cone
├── Color: Cyan (#00D5C4)
├── Animation: Spin based on time
├── Files: phi_t_helix.glb, phi_t_wireframe.glb
└── Scale: 1.0 unit

ψʳ (Structural Cadence)
├── Shape: 3-torus with memory loops
├── Color: Violet (#6A00F4)
├── Animation: Pulsing geometry, looping paths
├── Files: psi_r_torus.glb, psi_r_lattice.glb
└── Scale: 1.2 units

Φᴱ (Contextual Potential)
├── Shape: Fractal spire / energy field
├── Color: Gold (#F2C340)
├── Animation: Growing/receding aura
├── Files: phi_e_spire.glb, phi_e_field.glb
└── Scale: 0.8 units
```

### 2. **Star Particle System**

```
Star_Base.glb
├── Geometry: Octahedron (8 points = resonance)
├── Size: 0.5 units
├── Color: White (0xFFFFFF)
├── Emission: Yes (glows by default)
└── Variants: 3 sizes for magnitude depth

Star_Glow.glb
├── Sphere halo around star
├── Transparent with falloff
└── Scales with focus/resonance
```

### 3. **Constellation Lines**

```
Constellation_Line.glb
├── Geometry: Thin cylindrical mesh
├── Color: Cyan with fade
├── Width: 0.02 units
└── Usage: Connect related CODEX cards
```

### 4. **LuminAI Avatar** (You have this)

```
luminai.glb (your build)
├── Geometry: Your character model
├── Scale: ~1.5 units for resonance-viewer
├── Rig: Optional (can be static or animated)
└── Textures: Should include all materials
```

### 5. **Textured Mesh Overlay** (You have this)

```
textured_mesh.glb (your build)
├── Geometry: Secondary detail layer
├── Opacity: 0.85 for blend
├── Scale: 1.45 units (slightly larger than avatar)
└── Purpose: Add visual complexity
```

### 6. **Environmental Assets**

```
Chronosphere_Ring.glb
├── Shape: Torus with moving particles
├── Color: Cyan gradient
├── Animation: Rotates around center
└── Represents: Time threshold visualization

Resonance_Sphere.glb
├── Shape: Wireframe icosahedron
├── Color: Violet (0x6A00F4)
├── Animation: Expands/contracts with resonance
└── Represents: Overall system energy

Resonance_Particles.glb
├── Particles flowing in patterns
├── Colors: Mix of cyan + violet
├── Animation: Orbits around focal point
└── Represents: Information cascade
```

---

## Build Specifications

### Blender Export Settings

```
Format: glTF 2.0 (.glb)
├── Include Animations: YES (if rigged)
├── Include Materials: YES
├── Include Textures: YES
├── Compression: Draco (optional but recommended)
└── Scale: 1 unit = 1 Blender unit
```

### Naming Convention

```
Asset_[TYPE]_[VERSION].glb

Examples:
- phi_t_helix_v1.glb
- psi_r_torus_v1.glb
- luminai_avatar_v2.glb
- constellation_line_v1.glb
- star_base_v1.glb
```

### Material Setup (Blender to glTF)

```
Standard Material
├── Base Color: Your color (sRGB)
├── Metallic: 0.0 (unless specific effect)
├── Roughness: 0.5 (semi-matte default)
├── Emission: Yes (color + strength)
└── Alpha Blend: For transparency

Example - Cyan Star:
├── Base: #00D5C4
├── Emission: #00D5C4 @ 1.0 strength
├── Metallic: 0.1
└── Roughness: 0.6
```

---

## File Organization

```
apps/star-viewer/models/
├── tgcr/
│   ├── phi_t_helix.glb
│   ├── psi_r_torus.glb
│   ├── phi_e_spire.glb
│   └── README.md (TGCR asset spec)
├── particles/
│   ├── star_base.glb
│   ├── star_glow.glb
│   └── resonance_particles.glb
├── environment/
│   ├── chronosphere_ring.glb
│   ├── resonance_sphere.glb
│   └── constellation_line.glb
└── avatars/
    ├── luminai.glb (your build)
    └── textured_mesh.glb (your build)

apps/resonance-viewer/models/
├── luminai.glb
├── textured_mesh.glb
└── aura_effects/ (optional glow/particle overlays)
```

---

## Integration Code Examples

### Load TGCR Symbol in Star Viewer

```javascript
const loader = new THREE.GLTFLoader();

loader.load('models/tgcr/phi_t_helix.glb', (gltf) => {
    const phiT = gltf.scene;
    phiT.position.set(x, y, z);
    phiT.scale.set(1, 1, 1);
    scene.add(phiT);

    // Animate rotation
    function animatePhiT() {
        phiT.rotation.z += 0.01;
        requestAnimationFrame(animatePhiT);
    }
    animatePhiT();
});
```

### Star Particle Instantiation

```javascript
function createStar(position, magnitude, focus) {
    loader.load('models/particles/star_base.glb', (gltf) => {
        const star = gltf.scene;
        star.position.copy(position);

        // Scale by magnitude
        const scale = 0.3 + (magnitude * 0.2);
        star.scale.set(scale, scale, scale);

        // Color by focus
        const focusColors = {
            'time': 0x00D5C4,
            'structure': 0x6A00F4,
            'consciousness': 0xF2C340,
            'embodiment': 0xFF6B6B,
            'art': 0x00D5C4,
        };

        star.traverse(node => {
            if (node.isMesh) {
                node.material.emissive = new THREE.Color(focusColors[focus]);
            }
        });

        scene.add(star);
        return star;
    });
}
```

### Connect Stars with Constellation Lines

```javascript
function drawConstellation(star1Position, star2Position) {
    loader.load('models/environment/constellation_line.glb', (gltf) => {
        const line = gltf.scene;

        // Position between two stars
        const midpoint = star1Position.clone().lerp(star2Position, 0.5);
        line.position.copy(midpoint);

        // Scale to distance
        const distance = star1Position.distanceTo(star2Position);
        line.scale.z = distance;

        // Look from point 1 to point 2
        line.lookAt(star2Position);

        scene.add(line);
    });
}
```

---

## Animation Examples

### Resonance Sphere Pulse

```javascript
function animateResonanceSphere(sphere, resonanceValue) {
    const targetScale = 1 + (resonanceValue / 10) * 0.3;
    const currentScale = sphere.scale.x;

    sphere.scale.set(
        currentScale + (targetScale - currentScale) * 0.05,
        currentScale + (targetScale - currentScale) * 0.05,
        currentScale + (targetScale - currentScale) * 0.05
    );
}
```

### Chronosphere Ring Rotation

```javascript
function animateChronosphere(sphere) {
    sphere.rotation.x += 0.005;
    sphere.rotation.z += 0.003;
}
```

### Particle Flow Animation

```javascript
function animateParticleFlow(particles, time) {
    particles.traverse(node => {
        if (node.isMesh) {
            node.position.y += Math.sin(time * 0.003) * 0.01;
            node.rotation.z += 0.01;
        }
    });
}
```

---

## What to Build First

### Priority 1 (Essential for star-viewer)

- [ ] Star_Base.glb (octahedron, 0.5 units)
- [ ] Phi_T_Helix.glb (rotating spiral, cyan)
- [ ] Psi_R_Torus.glb (3-torus, violet)
- [ ] Phi_E_Spire.glb (fractal tower, gold)

### Priority 2 (Nice-to-have)

- [ ] Constellation_Line.glb (connecting edges)
- [ ] Resonance_Sphere.glb (outer envelope)
- [ ] Chronosphere_Ring.glb (timeline indicator)

### Priority 3 (Enhancement)

- [ ] Star_Glow.glb (halo effect)
- [ ] Resonance_Particles.glb (flowing energy)
- [ ] Aura effects (optional overlays)

---

## Testing Assets

Once built, test loading them:

```bash
# Local Three.js viewer
python3 -m http.server 8000
# Visit http://localhost:8000/apps/star-viewer/
```

Then in browser console:

```javascript
// Verify asset loads
const loader = new THREE.GLTFLoader();
loader.load('models/tgcr/phi_t_helix.glb', (gltf) => {
    console.log('✅ Asset loaded:', gltf.scene);
    scene.add(gltf.scene);
});
```

---

## Color Reference

```
Cyan (#00D5C4)     — φᵗ, time, temporal
Violet (#6A00F4)   — ψʳ, structure, cadence
Gold (#F2C340)     — Φᴱ, potential, energy
Navy (#0B1E3B)     — Background, depth
Shadow (#0A0A0C)   — Deep shadow
White (#FFFFFF)    — Stars, highlights
Red (#FF6B6B)      — Embodiment
```

---

## Next Steps

1. Create basic geometric versions first (Blender primitives)
2. Export as GLB v2.0
3. Test in Three.js viewer
4. Refine materials + animations
5. Build final artistic versions

**Ready to build?** 🎨
