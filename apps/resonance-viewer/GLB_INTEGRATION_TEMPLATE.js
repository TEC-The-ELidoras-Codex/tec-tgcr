/**
 * CODE SNIPPET: Add this to resonance-viewer.js after the pointLight section
 * Location: In the initThreeJS() function, after line: scene.add(pointLight);
 */

// ============================================================================
// GLB MODEL LOADING (Add after pointLight initialization)
// ============================================================================

const gltfLoader = new THREE.GLTFLoader();

// Load LuminAI avatar
gltfLoader.load(
  "models/luminai.glb",
  (gltf) => {
    luminaiModel = gltf.scene;

    // Scale and position
    luminaiModel.scale.set(1.5, 1.5, 1.5);
    luminaiModel.position.set(0, -0.5, 0);

    // Shadow casting
    luminaiModel.traverse((node) => {
      if (node.isMesh) {
        node.castShadow = true;
        node.receiveShadow = true;
      }
    });

    scene.add(luminaiModel);
    console.log("✅ LuminAI avatar loaded successfully");
  },
  (progress) => {
    console.log(
      `LuminAI loading: ${Math.round(
        (progress.loaded / progress.total) * 100
      )}%`
    );
  },
  (error) => {
    console.error("❌ Error loading LuminAI model:", error);
  }
);

// Load textured mesh overlay
gltfLoader.load(
  "models/textured_mesh.glb",
  (gltf) => {
    const mesh = gltf.scene;

    // Scale, position, and transparency
    mesh.scale.set(1.45, 1.45, 1.45);
    mesh.position.set(0, -0.5, 0.2);
    mesh.traverse((node) => {
      if (node.isMesh) {
        node.material.transparent = true;
        node.material.opacity = 0.85;
        node.castShadow = true;
        node.receiveShadow = true;
      }
    });

    scene.add(mesh);
    console.log("✅ Textured mesh loaded successfully");
  },
  undefined,
  (error) => {
    console.error("❌ Error loading textured mesh:", error);
  }
);

// ============================================================================
// ANIMATION ENHANCEMENT (Replace the existing animate() function's model code)
// ============================================================================

// Find this line in animate():
// luminaiModel.rotation.y += 0.002;

// Replace with:
if (luminaiModel) {
  // Base rotation
  luminaiModel.rotation.y += 0.002;

  // Focus-based rotation speed
  if (currentCard?.focus === "time") {
    luminaiModel.rotation.y += 0.015; // Faster for temporal
  } else if (currentCard?.focus === "structure") {
    luminaiModel.rotation.y += 0.003; // Steady for structural
  } else if (currentCard?.focus === "consciousness") {
    luminaiModel.rotation.x += 0.002; // Tilt for consciousness
  }

  // Resonance-based pulsing
  const pulseScale =
    1 + Math.sin(Date.now() * 0.003) * 0.05 * (resonanceValue / 10);
  luminaiModel.scale.set(1.5 * pulseScale, 1.5 * pulseScale, 1.5 * pulseScale);

  // Color emission based on focus
  const focusColors = {
    time: 0x00d5c4, // Cyan
    structure: 0x6a00f4, // Violet
    consciousness: 0xf2c340, // Gold
    embodiment: 0xff6b6b, // Red
    art: 0x00d5c4, // Cyan
    multi_domain: 0x9d4edd, // Purple
  };

  const emissiveColor = focusColors[currentCard?.focus] || 0xffffff;
  const emissiveIntensity = 0.2 + resonanceValue / 50;

  luminaiModel.traverse((node) => {
    if (node.isMesh && node.material) {
      node.material.emissive = new THREE.Color(emissiveColor);
      node.material.emissiveIntensity = emissiveIntensity;
    }
  });
}

// ============================================================================
// CARD UPDATE ENHANCEMENT (Add to updateResonance() function)
// ============================================================================

// After calculating resonanceValue, add this to apply visual feedback:

// Apply material glow based on resonance
const glowIntensity = (resonanceValue / 10) * 0.5;
if (luminaiModel) {
  luminaiModel.traverse((node) => {
    if (node.isMesh && node.material) {
      // Increase roughness for more diffuse appearance at low resonance
      if (node.material.roughness !== undefined) {
        node.material.roughness = 0.5 - resonanceValue / 20;
      }
      // Add metallic sheen at high resonance
      if (node.material.metalness !== undefined) {
        node.material.metalness = resonanceValue / 20;
      }
    }
  });
}

// ============================================================================
// END OF CODE SNIPPETS
// ============================================================================

/**
 * INTEGRATION CHECKLIST:
 *
 * [ ] Place luminai.glb in apps/resonance-viewer/models/
 * [ ] Place textured_mesh.glb in apps/resonance-viewer/models/
 * [ ] Add GLB loading code after pointLight initialization (around line 130)
 * [ ] Update animate() function with focus-based rotation + pulsing
 * [ ] Update updateResonance() with material glow
 * [ ] Test locally: python3 -m http.server 8000
 * [ ] Verify models load (check browser console F12)
 * [ ] Verify API loads (should see CODEX cards)
 * [ ] Deploy to elidorascodex.com
 *
 * EXPECTED BEHAVIOR:
 * - Models rotate smoothly
 * - Rotation speed changes with card focus (time faster, structure steady)
 * - Models pulse with resonance meter
 * - Color changes based on TGCR focus area
 * - Glow intensity increases as resonance rises
 */
