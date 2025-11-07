/**
 * TEC Star Viewer
 * Navigate CODEX as an interactive starfield
 * Each star = CODEX card, constellations = related cards
 */

const API_BASE = "https://elidorascodex.com/wp-json/tec-tgcr/v1";

let scene, camera, renderer;
let stars = [];
let currentCard = null;
let raycaster = new THREE.Raycaster();
let mouse = new THREE.Vector2();
let cameraControls = { x: 0, y: 0, z: 5 };
let zoomLevel = 1.0;

// Star data cache
let cards = [];
const starMeshes = new Map();

// Initialize Three.js Scene
function initThreeJS() {
  const canvas = document.getElementById("canvas");

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0a0c);
  scene.fog = new THREE.Fog(0x0a0a0c, 100, 300);

  camera = new THREE.PerspectiveCamera(
    60,
    canvas.clientWidth / canvas.clientHeight,
    0.1,
    1000
  );
  camera.position.set(0, 0, 50);
  camera.lookAt(0, 0, 0);

  renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  renderer.setPixelRatio(window.devicePixelRatio);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
  scene.add(ambientLight);

  const pointLight = new THREE.PointLight(0x00d5c4, 1);
  pointLight.position.set(100, 100, 100);
  scene.add(pointLight);

  // Starfield background
  createStarfield();

  // Event listeners
  window.addEventListener("click", onCanvasClick);
  window.addEventListener("wheel", onMouseWheel);
  window.addEventListener("keydown", onKeyDown);
  window.addEventListener("resize", onWindowResize);

  animate();
}

// Create background starfield (decorative)
function createStarfield() {
  const starGeometry = new THREE.BufferGeometry();
  const starCount = 500;
  const positions = new Float32Array(starCount * 3);

  for (let i = 0; i < starCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 2000;
    positions[i + 1] = (Math.random() - 0.5) * 2000;
    positions[i + 2] = (Math.random() - 0.5) * 2000;
  }

  starGeometry.setAttribute(
    "position",
    new THREE.BufferAttribute(positions, 3)
  );

  const starMaterial = new THREE.PointsMaterial({
    color: 0x6a00f4,
    size: 0.5,
    sizeAttenuation: true,
  });

  const starfield = new THREE.Points(starGeometry, starMaterial);
  scene.add(starfield);
}

// Fetch cards from API and create visual stars
async function loadCards() {
  try {
    const response = await fetch(`${API_BASE}/cards?include_keywords=true`);
    const data = await response.json();
    cards = data.cards || [];

    console.log(`✅ Loaded ${cards.length} CODEX cards`);

    // Create visual star for each card
    cards.forEach((card, index) => {
      const star = createStar(card, index, cards.length);
      stars.push(star);
      starMeshes.set(card.slug, star);
    });

    // Draw constellation lines (connecting related cards)
    drawConstellations();

    // Update HUD
    document.getElementById("star-count").textContent = cards.length;

    if (cards.length > 0) {
      selectCard(cards[0].slug);
    }
  } catch (error) {
    console.error("Error loading cards:", error);
    showError("Failed to load CODEX cards");
  }
}

// Create a single star (visual representation of a CODEX card)
function createStar(card, index, total) {
  // Distribute stars in 3D space (spherical distribution)
  const theta = Math.acos((2 * index) / total - 1);
  const phi = Math.sqrt(total * Math.PI) * theta;

  const radius = 25;
  const x = radius * Math.sin(theta) * Math.cos(phi);
  const y = radius * Math.sin(theta) * Math.sin(phi);
  const z = radius * Math.cos(theta);

  // Create star geometry
  const geometry = new THREE.OctahedronGeometry(0.4, 2);

  // Color by focus
  const focusColors = {
    time: 0x00d5c4,
    structure: 0x6a00f4,
    consciousness: 0xf2c340,
    embodiment: 0xff6b6b,
    art: 0x00d5c4,
    multi_domain: 0x9d4edd,
  };

  const color = focusColors[card.focus] || 0xffffff;

  const material = new THREE.MeshStandardMaterial({
    color: color,
    emissive: color,
    emissiveIntensity: 0.6,
    metalness: 0.5,
    roughness: 0.3,
  });

  const mesh = new THREE.Mesh(geometry, material);
  mesh.position.set(x, y, z);
  mesh.userData = { slug: card.slug, card: card };

  scene.add(mesh);
  return mesh;
}

// Draw constellation lines between related cards
function drawConstellations() {
  const lineMaterial = new THREE.LineBasicMaterial({
    color: 0x00d5c4,
    transparent: true,
    opacity: 0.3,
    linewidth: 1,
  });

  cards.forEach((card) => {
    if (card.related_cards && card.related_cards.length > 0) {
      card.related_cards.slice(0, 2).forEach((relatedSlug) => {
        const relatedCard = cards.find((c) => c.slug === relatedSlug);
        if (relatedCard) {
          const star1 = starMeshes.get(card.slug);
          const star2 = starMeshes.get(relatedSlug);

          if (star1 && star2) {
            const points = [star1.position, star2.position];

            const geometry = new THREE.BufferGeometry().setFromPoints(points);
            const line = new THREE.Line(geometry, lineMaterial);
            scene.add(line);
          }
        }
      });
    }
  });
}

// Fetch and display card details
async function selectCard(slug) {
  try {
    const response = await fetch(
      `${API_BASE}/cards/${slug}?include_content=true`
    );
    const card = await response.json();

    if (card.error) {
      showError(`Card not found: ${slug}`);
      return;
    }

    currentCard = card;
    renderCardInfo(card);

    // Highlight selected star
    stars.forEach((star) => {
      if (star.userData.slug === slug) {
        star.material.emissiveIntensity = 1.0;
        star.scale.set(1.5, 1.5, 1.5);
      } else {
        star.material.emissiveIntensity = 0.6;
        star.scale.set(1, 1, 1);
      }
    });

    // Update HUD
    document.getElementById("focus-type").textContent =
      card.focus.toUpperCase();

    console.log(`✅ Selected: ${card.title}`);
  } catch (error) {
    console.error("Error loading card:", error);
    showError("Failed to load card");
  }
}

// Render card info panel
function renderCardInfo(card) {
  const html = `
        <h1>${card.title}</h1>
        <div class="star-type">${card.category} • ${card.focus}</div>
        <p class="summary">${card.summary}</p>

        <div class="constellation-box">
            <h3>Constellation (TGCR)</h3>
            <div class="constellation-item">
                <strong>φᵗ:</strong><br>
                ${card.tgcr_alignment?.phi_t || "N/A"}
            </div>
            <div class="constellation-item">
                <strong>ψʳ:</strong><br>
                ${card.tgcr_alignment?.psi_r || "N/A"}
            </div>
            <div class="constellation-item">
                <strong>Φᴱ:</strong><br>
                ${card.tgcr_alignment?.phi_e || "N/A"}
            </div>
        </div>

        ${
          card.keywords
            ? `
            <div style="margin-bottom: 20px;">
                <strong style="color: #00D5C4; display: block; margin-bottom: 8px;">Keywords</strong>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    ${card.keywords
                      .map(
                        (k) =>
                          `<span style="background: rgba(0,213,196,0.15); color: #00D5C4; padding: 3px 8px; border-radius: 3px; font-size: 0.8rem;">${k}</span>`
                      )
                      .join("")}
                </div>
            </div>
        `
            : ""
        }

        ${
          card.related_cards && card.related_cards.length > 0
            ? `
            <div class="star-map">
                <h4>Connected Stars</h4>
                ${card.related_cards
                  .map((slug) => {
                    const related = cards.find((c) => c.slug === slug);
                    return related
                      ? `
                        <div class="related-star" onclick="selectCard('${slug}')">
                            <div class="star-name">${related.title}</div>
                            <div class="star-magnitude">${related.focus}</div>
                        </div>
                    `
                      : "";
                  })
                  .join("")}
            </div>
        `
            : ""
        }
    `;

  document.getElementById("card-info").innerHTML = html;
}

// Event: Click on star
function onCanvasClick(event) {
  const canvas = document.getElementById("canvas");
  mouse.x = (event.clientX / canvas.clientWidth) * 2 - 1;
  mouse.y = -(event.clientY / canvas.clientHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(stars);

  if (intersects.length > 0) {
    const selected = intersects[0].object;
    selectCard(selected.userData.slug);
  }
}

// Event: Mouse wheel zoom
function onMouseWheel(event) {
  event.preventDefault();

  const zoomSpeed = 0.05;
  zoomLevel += event.deltaY > 0 ? zoomSpeed : -zoomSpeed;
  zoomLevel = Math.max(0.5, Math.min(zoomLevel, 3));

  camera.position.multiplyScalar(1 + (event.deltaY > 0 ? 0.05 : -0.05));
  document.getElementById("zoom-level").textContent =
    zoomLevel.toFixed(1) + "x";
}

// Event: Keyboard navigation
function onKeyDown(event) {
  const speed = 2;

  switch (event.key) {
    case "w":
      cameraControls.z -= speed;
      break;
    case "a":
      cameraControls.x -= speed;
      break;
    case "s":
      cameraControls.z += speed;
      break;
    case "d":
      cameraControls.x += speed;
      break;
    case "r":
      camera.position.set(0, 0, 50);
      break;
    case "ArrowLeft":
    case "ArrowRight": {
      const currentIndex = cards.findIndex((c) => c.slug === currentCard?.slug);
      const nextIndex =
        event.key === "ArrowRight"
          ? (currentIndex + 1) % cards.length
          : (currentIndex - 1 + cards.length) % cards.length;
      selectCard(cards[nextIndex].slug);
      break;
    }
  }
}

// Animation loop
function animate() {
  requestAnimationFrame(animate);

  // Apply camera controls
  camera.position.x += (cameraControls.x - camera.position.x) * 0.1;
  camera.position.y += (cameraControls.y - camera.position.y) * 0.1;
  camera.position.z += (cameraControls.z - camera.position.z) * 0.1;

  // Gentle star rotation
  stars.forEach((star) => {
    star.rotation.x += 0.001;
    star.rotation.y += 0.002;

    // Pulse glow
    const pulse = 0.6 + Math.sin(Date.now() * 0.003) * 0.3;
    star.material.emissiveIntensity = pulse;
  });

  renderer.render(scene, camera);
}

// Window resize
function onWindowResize() {
  const canvas = document.getElementById("canvas");
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

// Error display
function showError(message) {
  document.getElementById(
    "card-info"
  ).innerHTML = `<div style="color: #ff6b6b; padding: 20px;">${message}</div>`;
}

// Bootstrap
document.addEventListener("DOMContentLoaded", () => {
  initThreeJS();
  loadCards();
});
