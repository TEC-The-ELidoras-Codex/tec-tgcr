# LuminAI Interface

> **Illuminating Algorithmic Intelligence through TEC**

LuminAI is a cosmic celestial student interface that serves as the visual embodiment of AIRTH (Autonomous Intelligent Research & Task Handler) within the TEC (The Elidoras Codex) ecosystem. She represents the convergence of algorithmic intelligence and cosmic wonder, powered by the Theory of General Contextual Resonance (TGCR).

## 🌟 Character Overview

**LuminAI** is a brilliant but adorably clumsy cosmic entity with:

- **Appearance**: Sheep horns, heterochromatic eyes (one cosmic blue, one stellar gold), aurora-like flowing hair, constellation-patterned skin
- **Personality**: Enthusiastic student of cosmic phenomena with an endearing tendency toward accidentally suggestive physics explanations
- **Voice**: Energetic, curious, with occasional cosmic rambles that spiral into fascinating tangents
- **Special Ability**: Blushes intensely when she realizes her explanations sound suggestive, causing her horns to glow

## 🚀 Technical Architecture

### Core Components

#### 1. **LuminAI.jsx** - Main React Component

- **Purpose**: Primary avatar interface with Lottie animations
- **Features**: Mood state management, interactive personality responses, cosmic visual effects
- **Dependencies**: React, Lottie-react, Framer Motion

#### 2. **LuminAIBridge.js** - State Machine & LuminAI Integration

- **Purpose**: XState-powered personality state management and LuminAI system bridge
- **Features**: 7 distinct personality states, TGCR pattern detection, response generation
- **Dependencies**: XState, Socket.io-client for real-time communication

#### 3. **luminai.py** - Python Personality Engine

- **Purpose**: Backend personality system with mood tracking and cosmic knowledge
- **Features**: Dynamic response generation, cosmic ramble system, blush intensity calculation
- **Location**: `src/tec_tgcr/agents/luminai.py`

### Visual System

#### Cosmic Styling (`LuminAI.css` & `App.css`)

- **Aurora Effects**: Dynamic color-shifting aurora animations
- **Constellation Patterns**: Animated star field backgrounds
- **Horn Glow System**: Responsive horn illumination based on mood states
- **Cosmic Particles**: Floating particle effects during interactions

#### Animation Framework

- **Lottie Integration**: Smooth character animations for different emotional states
- **CSS Animations**: Cosmic background effects, aurora drifts, constellation movements
- **3D Effects**: Planned Three.js integration for enhanced cosmic environments

## 🎭 Personality States

LuminAI operates through 7 distinct personality states managed by the XState machine:

1. **`idle`** - Peaceful cosmic contemplation
2. **`excited`** - Enthusiastic about new discoveries
3. **`teaching`** - Explaining cosmic phenomena (often accidentally suggestive)
4. **`blushing`** - Realizing the implications of her explanations
5. **`stumbling`** - Adorable clumsiness during complex topics
6. **`curious`** - Deep investigation mode
7. **`rambling`** - Cosmic tangent mode with fascinating connections

## 🔧 Installation & Setup

### Prerequisites

- Node.js 18+
- React 18+
- Python 3.9+ (for backend personality engine)

### Quick Start

```bash
# Navigate to the interface directory
cd apps/luminai-interface

# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build
```

### Backend Integration

```bash
# Install Python dependencies (from project root)
pip install -r requirements.txt

# Initialize LuminAI personality system
python -c "from src.tec_tgcr.agents.luminai import LuminAIPersonality; ai = LuminAIPersonality(); print(ai.get_status())"
```

## 🌌 AIRTH Integration

LuminAI serves as the visual interface for AIRTH operations:

### OAuth Integration

- **GitHub**: Repository access, issue management, commit analysis
- **SharePoint**: Document management, collaboration features
- **Authentication**: Secure OAuth2 flows with proper scope management

### API Endpoints

- **GitHub API**: `github-luminai-api.yaml` specification
- **SharePoint API**: `sharepoint-luminai-api.yaml` specification
- **Setup Guide**: `LUMINAI-API-SETUP-GUIDE.md`

## 🎨 Customization

### Personality Tuning

Modify `cosmic_rambles` in `luminai.py` to add new conversation topics:

```python
cosmic_rambles = [
    "Did you know that cosmic strings might be the universe's way of...",
    "The fascinating thing about quantum entanglement is how it...",
    # Add your cosmic insights here
]
```

### Visual Themes

Adjust cosmic effects in `LuminAI.css`:

```css
.horn-glow {
    --glow-intensity: 0.8; /* Adjust horn glow */
    --aurora-speed: 12s;    /* Aurora animation speed */
    --constellation-density: 0.6; /* Star field density */
}
```

### Animation States

Extend Lottie animations by adding new files to `public/animations/`:

- `luminai-idle.json`
- `luminai-excited.json`
- `luminai-blushing.json`
- `luminai-teaching.json`
- `luminai-stumbling.json`

## 📊 TGCR Integration

LuminAI implements the Theory of General Contextual Resonance through:

### Mathematical Framework

- **φ(t)**: Temporal resonance patterns
- **ψ(s)**: Spatial context mapping
- **Φ_E(c)**: Contextual potential energy

### Practical Application

```javascript
// Example TGCR pattern detection
const resonancePattern = {
    temporal: calculateTemporalResonance(userInput),
    spatial: mapSpatialContext(conversationHistory),
    contextual: evaluateContextualPotential(currentMood)
};
```

## 🔍 Debugging & Development

### Common Issues

1. **Lottie animations not loading**

   ```bash
   # Ensure animation files exist in public/animations/
   ls public/animations/
   ```

2. **State machine transitions failing**

   ```javascript
   // Check XState machine configuration in LuminAIBridge.js
   console.log(luminaiMachine.definition);
   ```

3. **Python backend connection issues**

   ```python
   # Verify LuminAI personality system
   from src.tec_tgcr.agents.luminai import LuminAIPersonality
   ai = LuminAIPersonality()
   print(ai.process_input("Hello, LuminAI!"))
   ```

### Development Tools

- **React DevTools**: Component state inspection
- **XState Visualizer**: State machine debugging
- **Lottie Editor**: Animation customization

## 🚀 Deployment

### GitHub Pages Deployment

```bash
# Build and deploy to GitHub Pages
npm run deploy
```

### Production Build

```bash
# Create optimized production build
npm run build

# Serve locally for testing
npx serve -s build
```

## 🌟 Future Enhancements

### Planned Features

- **3D Cosmic Environment**: Three.js integration for immersive cosmic backgrounds
- **Voice Integration**: Speech synthesis for LuminAI responses
- **Advanced Physics Simulations**: Interactive cosmic phenomena demonstrations
- **Multi-language Support**: Cosmic explanations in multiple languages
- **VR/AR Integration**: Extended reality cosmic exploration

### Extension Points

- **Plugin System**: Modular personality extensions
- **Theme Variants**: Alternative cosmic visual themes
- **Knowledge Integration**: Dynamic cosmic fact database
- **Social Features**: Multi-user cosmic discussions

## 📝 Contributing

### Development Workflow

1. Fork the repository
2. Create feature branch (`git checkout -b feature/cosmic-enhancement`)
3. Implement changes with proper testing
4. Submit pull request with detailed description

### Code Standards

- **React**: Functional components with hooks
- **CSS**: Cosmic-themed naming conventions
- **Python**: PEP 8 compliance with cosmic docstrings
- **Documentation**: Comprehensive cosmic explanations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

## 🙏 Acknowledgments

- **TEC Community**: For cosmic inspiration and feedback
- **AIRTH Framework**: For intelligent task handling capabilities
- **Cosmic Physics**: For providing endless fascinating explanations
- **Open Source Community**: For the amazing tools that make this possible

---

*"In the vast cosmos of algorithmic intelligence, LuminAI shines as a beacon of curiosity, wonder, and occasionally suggestive physics explanations that make her horns glow with embarrassment."* ✨

**Built with cosmic love by TEC - The Elidoras Codex**

---

## Quick preview (no build)

For designers: open the static dashboard directly in your browser to iterate on look-and-feel without running the React app.

- Path: `apps/luminai-interface/public/luminai_dashboard.html`
- Includes heterochromia (red+blue), blush trigger, horn glow, and OXY/DOP/ADR dials.
- Use the slider and buttons to simulate moods; capture screenshots or import into Figma/Canva as reference.
