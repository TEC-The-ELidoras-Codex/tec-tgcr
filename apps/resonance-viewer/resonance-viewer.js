/**
 * TEC Resonance Viewer
 * 3D interactive CODEX card viewer with Resonance visualization
 * Connects to TEC API at elidorascodex.com/wp-json/tec-tgcr/v1/
 */

const API_BASE = "https://elidorascodex.com/wp-json/tec-tgcr/v1";

let scene, camera, renderer;
let luminaiModel = null;
let currentCard = null;
let resonanceValue = 0;

// Card database (will be fetched from API)
let cards = [];

// Three.js Setup
function initThreeJS() {
  const canvas = document.getElementById("canvas");
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0a0c);
  scene.fog = new THREE.Fog(0x0a0a0c, 50, 150);

  camera = new THREE.PerspectiveCamera(
    75,
    canvas.clientWidth / canvas.clientHeight,
    0.1,
    1000
  );
  camera.position.set(0, 1.5, 3);
  camera.lookAt(0, 1, 0);

  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.shadowMap.enabled = true;

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0x6a00f4, 1.2);
  directionalLight.position.set(5, 8, 5);
  directionalLight.castShadow = true;
  directionalLight.shadow.mapSize.width = 2048;
  directionalLight.shadow.mapSize.height = 2048;
  scene.add(directionalLight);

  const pointLight = new THREE.PointLight(0x00d5c4, 0.6);
  pointLight.position.set(-5, 3, 5);
  scene.add(pointLight);

  // Resonance indicator sphere (background)
  const resonanceSphere = new THREE.IcosahedronGeometry(8, 4);
  const resonanceMaterial = new THREE.MeshStandardMaterial({
    color: 0x1a2d4d,
    emissive: 0x6a00f4,
    emissiveIntensity: 0.1,
    wireframe: true,
    transparent: true,
    opacity: 0.1,
  });
  const resonanceMesh = new THREE.Mesh(resonanceSphere, resonanceMaterial);
  scene.add(resonanceMesh);

  // Handle window resize
  window.addEventListener("resize", onWindowResize);

  // Start animation loop
  animate();
}

function onWindowResize() {
  const canvas = document.getElementById("canvas");
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

function animate() {
  requestAnimationFrame(animate);

  // Gentle rotation
  if (luminaiModel) {
    luminaiModel.rotation.y += 0.002;

    // Pulse based on resonance
    const pulseScale =
      1 + Math.sin(Date.now() * 0.003) * 0.02 * (resonanceValue / 10);
    luminaiModel.scale.set(pulseScale, pulseScale, pulseScale);
  }

  renderer.render(scene, camera);
}

// Fetch CODEX cards from API
async function loadCards() {
  try {
    const response = await fetch(`${API_BASE}/cards?include_keywords=true`);
    const data = await response.json();
    cards = data.cards || [];
    console.log("✅ Loaded", cards.length, "CODEX cards");

    if (cards.length > 0) {
      loadCard(cards[0].slug);
      renderCardList();
    }
  } catch (error) {
    console.error("Error loading cards:", error);
    showError("Failed to load CODEX cards");
  }
}

// Load specific card details from API
async function loadCard(slug) {
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
    updateResonance(card);

    console.log("✅ Loaded card:", card.title);
  } catch (error) {
    console.error("Error loading card:", error);
    showError("Failed to load card");
  }
}

// Render card information panel
function renderCardInfo(card) {
  const cardInfo = document.getElementById("card-info");

  const html = `
        <h1>${card.title}</h1>
        <div class="category">${card.category} • ${card.focus}</div>
        <p class="summary">${card.summary}</p>

        <div class="tgcr-box">
            <h3>TGCR Alignment</h3>
            <div class="tgcr-item">
                <strong>φᵗ (Temporal Attention):</strong><br>
                ${card.tgcr_alignment?.phi_t || "N/A"}
            </div>
            <div class="tgcr-item">
                <strong>ψʳ (Structural Cadence):</strong><br>
                ${card.tgcr_alignment?.psi_r || "N/A"}
            </div>
            <div class="tgcr-item">
                <strong>Φᴱ (Contextual Potential):</strong><br>
                ${card.tgcr_alignment?.phi_e || "N/A"}
            </div>
        </div>

        <div class="keywords">
            ${(card.keywords || [])
              .map((k) => `<div class="keyword">${k}</div>`)
              .join("")}
        </div>

        ${
          card.primary_questions
            ? `
            <div class="tgcr-box">
                <h3>Primary Questions</h3>
                ${card.primary_questions
                  .map((q) => `<div class="tgcr-item">• ${q}</div>`)
                  .join("")}
            </div>
        `
            : ""
        }

        ${
          card.related_cards && card.related_cards.length > 0
            ? `
            <div class="card-list">
                <h4>Related Cards</h4>
                ${card.related_cards
                  .map((slug) => {
                    const related = cards.find((c) => c.slug === slug);
                    return related
                      ? `
                        <div class="card-item" onclick="loadCard('${slug}')">
                            <div class="card-item-title">${related.title}</div>
                            <div class="card-item-focus">${related.focus}</div>
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

  cardInfo.innerHTML = html;
}

// Render list of all cards
function renderCardList() {
  const cardList = document
    .getElementById("card-info")
    .querySelector(".card-list");
  if (!cardList) return;

  const html = cards
    .map(
      (card) => `
        <div class="card-item" onclick="loadCard('${card.slug}')">
            <div class="card-item-title">${card.title}</div>
            <div class="card-item-focus">${card.focus}</div>
        </div>
    `
    )
    .join("");

  cardList.innerHTML = html;
}

// Calculate and display resonance based on card data
function updateResonance(card) {
  // Simple resonance calculation based on TGCR alignment presence
  const hasPhiT = card.tgcr_alignment?.phi_t ? 1 : 0;
  const hasPsiR = card.tgcr_alignment?.psi_r ? 1 : 0;
  const hasPhiE = card.tgcr_alignment?.phi_e ? 1 : 0;
  const hasKeywords = (card.keywords?.length || 0) > 0 ? 1 : 0;
  const hasRelated = (card.related_cards?.length || 0) > 0 ? 1 : 0;

  resonanceValue = (hasPhiT + hasPsiR + hasPhiE + hasKeywords + hasRelated) * 2;

  const fill = document.getElementById("resonance-fill");
  const value = document.getElementById("resonance-value");

  fill.style.width = resonanceValue * 10 + "%";
  value.textContent = resonanceValue.toFixed(1);

  console.log(`Resonance for ${card.title}: ${resonanceValue.toFixed(1)}/10`);
}

// Show error message
function showError(message) {
  const cardInfo = document.getElementById("card-info");
  cardInfo.innerHTML = `<div style="color: #ff6b6b; padding: 20px;">${message}</div>`;
}

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  initThreeJS();
  loadCards();
});

// Keyboard navigation
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
    const currentIndex = cards.findIndex((c) => c.slug === currentCard?.slug);
    let nextIndex;

    if (e.key === "ArrowRight") {
      nextIndex = (currentIndex + 1) % cards.length;
    } else {
      nextIndex = (currentIndex - 1 + cards.length) % cards.length;
    }

    loadCard(cards[nextIndex].slug);
  }
});
