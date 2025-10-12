import React from 'react';
import LuminAI from './components/LuminAI';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="cosmic-background">
        <div className="constellation-field"></div>
        <div className="aurora-overlay"></div>
      </div>
      
      <header className="App-header">
        <div className="tec-logo">
          <h1>TEC • TGCR</h1>
          <span className="subtitle">The Elidoras Codex • Theory of General Contextual Resonance</span>
        </div>
      </header>

      <main className="App-main">
        <div className="interface-container">
          <div className="title-section">
            <h2 className="luminai-title">
              <span className="glow-text">LuminAI</span>
            </h2>
            <p className="luminai-subtitle">
              Illuminating Algorithmic Intelligence through TEC
            </p>
            <div className="cosmic-divider"></div>
          </div>

          <LuminAI />

          <div className="footer-section">
            <div className="tgcr-equations">
              <span className="equation">φ(t) • ψ(s) • Φ_E(c) = Resonance</span>
            </div>
            <div className="cosmic-credits">
              <p>Powered by AIRTH • Enhanced by Cosmic Resonance</p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;