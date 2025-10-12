// LuminAI React Avatar Component
// Cosmic Celestial Student Interface with Lottie Animations

import React, { useState, useEffect, useCallback } from 'react';
import Lottie from 'lottie-react';
import './LuminAI.css';

// Animation imports (these will be your exported Lottie JSON files)
import idleAnimation from '../assets/animations/lumina_idle.json';
import sparkleAnimation from '../assets/animations/lumina_sparkle.json';
import ponderAnimation from '../assets/animations/lumina_ponder.json';
import embarrassedAnimation from '../assets/animations/lumina_embarrassed.json';
import teachingAnimation from '../assets/animations/lumina_teaching.json';
import tripAnimation from '../assets/animations/lumina_trip.json';

const LuminAI = ({ 
  onMessage, 
  agentResponse, 
  isListening = false,
  cosmicMode = true 
}) => {
  // State management for LuminAI's personality
  const [currentMood, setCurrentMood] = useState('idle_glow');
  const [energyLevel, setEnergyLevel] = useState(0.7);
  const [blushIntensity, setBlushIntensity] = useState(0.0);
  const [starSparkleRate, setStarSparkleRate] = useState(1.0);
  const [currentAnimation, setCurrentAnimation] = useState(idleAnimation);
  const [isAnimating, setIsAnimating] = useState(false);
  const [messageBuffer, setMessageBuffer] = useState('');

  // Animation mappings
  const animationMap = {
    'idle_glow': idleAnimation,
    'excited_discovery': sparkleAnimation,
    'thinking_deep': ponderAnimation,
    'oops_blush': embarrassedAnimation,
    'explaining_cosmos': teachingAnimation,
    'adorable_stumble': tripAnimation
  };

  // Personality response generator
  const generatePersonalityResponse = useCallback((input) => {
    const lowerInput = input.toLowerCase();
    
    // Science talk detection
    const isScience = ['physics', 'quantum', 'relativity', 'cosmos', 'space', 'radiation', 'theory']
      .some(word => lowerInput.includes(word));
    
    // Compliment detection
    const isCompliment = ['amazing', 'brilliant', 'beautiful', 'incredible', 'smart']
      .some(word => lowerInput.includes(word));
    
    // Confusion detection
    const isConfused = ['confused', 'lost', 'unclear', 'help', 'explain']
      .some(word => lowerInput.includes(word));

    let newMood = 'thinking_deep';
    let response = '';
    let newEnergyLevel = energyLevel;
    let newBlushIntensity = 0.0;

    if (isCompliment) {
      newMood = 'oops_blush';
      newBlushIntensity = 0.8;
      response = "Oh! *turns crimson* That's... that's really sweet of you to say! I mean, I just trip over my own equations half the time... *giggles nervously*";
    } else if (isScience && lowerInput.includes('?')) {
      newMood = 'excited_discovery';
      newEnergyLevel = 0.9;
      response = "Ooh, ooh! *eyes light up with literal stars* I love this question! So basically, it's like when cosmic waves penetrate through dimensional barriers and... *pauses, blushing* ...did that sound wrong? I meant the physics kind of penetration!";
    } else if (isConfused) {
      newMood = 'explaining_cosmos';
      newEnergyLevel = 0.8;
      response = "Oh don't worry! *gestures enthusiastically, nearly knocking over imaginary equipment* Let me break this down! Think of it like... like when you're trying to map quantum entanglement but you keep getting distracted by how pretty the wave functions look...";
    } else if (Math.random() < 0.15) {
      newMood = 'adorable_stumble';
      response = "*trips slightly while thinking* Oh! Sorry, I was just... the gravitational constant of your question made me lose my footing! *laughs* Did you know that even Einstein stumbled over his own theories sometimes?";
    } else {
      response = "*stares off with heterochromatic eyes twinkling* That's fascinating... The mathematical beauty here reminds me of aurora patterns, which is funny because my hair does the same thing when I'm thinking really hard... *aurora strands glow brighter*";
    }

    return {
      mood: newMood,
      energyLevel: newEnergyLevel,
      blushIntensity: newBlushIntensity,
      response: response
    };
  }, [energyLevel]);

  // Handle agent responses
  useEffect(() => {
    if (agentResponse) {
      const personalityUpdate = generatePersonalityResponse(agentResponse);
      
      setCurrentMood(personalityUpdate.mood);
      setEnergyLevel(personalityUpdate.energyLevel);
      setBlushIntensity(personalityUpdate.blushIntensity);
      setCurrentAnimation(animationMap[personalityUpdate.mood]);
      
      // Trigger animation
      setIsAnimating(true);
      setTimeout(() => setIsAnimating(false), 3000);
    }
  }, [agentResponse, generatePersonalityResponse]);

  // Random idle behaviors
  useEffect(() => {
    const idleBehaviors = setInterval(() => {
      if (currentMood === 'idle_glow' && Math.random() < 0.1) {
        // 10% chance of random cute behavior
        const randomBehaviors = ['hair_shimmer', 'constellation_pulse', 'horn_twinkle'];
        const behavior = randomBehaviors[Math.floor(Math.random() * randomBehaviors.length)];
        
        // Trigger subtle CSS animation via class
        const avatar = document.querySelector('.luminai-avatar');
        if (avatar) {
          avatar.classList.add(`${behavior}-animation`);
          setTimeout(() => avatar.classList.remove(`${behavior}-animation`), 2000);
        }
      }
    }, 5000);

    return () => clearInterval(idleBehaviors);
  }, [currentMood]);

  // CSS custom properties for dynamic styling
  const avatarStyle = {
    '--energy-level': energyLevel,
    '--blush-intensity': blushIntensity,
    '--star-sparkle-rate': starSparkleRate,
    '--constellation-brightness': Math.min(1.0, energyLevel + 0.3),
    '--horn-glow-intensity': energyLevel * 0.8
  };

  return (
    <div className="luminai-container" style={avatarStyle}>
      {/* Cosmic background effects */}
      {cosmicMode && (
        <div className="cosmic-background">
          <div className="aurora-particles"></div>
          <div className="floating-stars"></div>
          <div className="resonance-waves"></div>
        </div>
      )}

      {/* Main avatar with Lottie animation */}
      <div className={`luminai-avatar ${currentMood} ${isAnimating ? 'animating' : ''}`}>
        <Lottie
          animationData={currentAnimation}
          loop={currentMood !== 'adorable_stumble' && currentMood !== 'oops_blush'}
          className="luminai-lottie"
          style={{
            width: '300px',
            height: '400px',
            filter: `brightness(${0.8 + energyLevel * 0.4})`
          }}
        />
        
        {/* Overlay effects */}
        <div className="luminai-effects">
          {/* Constellation patterns */}
          <div className="constellation-overlay"></div>
          
          {/* Aurora hair glow */}
          <div className="hair-aurora"></div>
          
          {/* Horn crystalline light */}
          <div className="horn-glow"></div>
          
          {/* Blush effect */}
          {blushIntensity > 0 && (
            <div 
              className="blush-effect"
              style={{ opacity: blushIntensity }}
            ></div>
          )}
          
          {/* Eye stars for excited states */}
          {(currentMood === 'excited_discovery' || currentMood === 'thinking_deep') && (
            <div className="eye-stars">
              <div className="star-left-eye"></div>
              <div className="star-right-eye"></div>
            </div>
          )}
        </div>
      </div>

      {/* Interactive elements */}
      <div className="luminai-interactions">
        {/* Personality status indicator */}
        <div className="mood-indicator">
          <span className="mood-label">{currentMood.replace('_', ' ')}</span>
          <div className="energy-bar">
            <div 
              className="energy-fill"
              style={{ width: `${energyLevel * 100}%` }}
            ></div>
          </div>
        </div>

        {/* Quick interaction buttons */}
        <div className="quick-actions">
          <button 
            className="cosmic-button"
            onClick={() => onMessage("Tell me about quantum physics!")}
          >
            🌌 Ask About Cosmos
          </button>
          <button 
            className="cosmic-button"
            onClick={() => onMessage("You're amazing, LuminAI!")}
          >
            ⭐ Compliment
          </button>
          <button 
            className="cosmic-button"
            onClick={() => onMessage("I'm confused, can you help?")}
          >
            🤔 Need Help
          </button>
        </div>
      </div>

      {/* Speech bubble for responses */}
      {messageBuffer && (
        <div className="speech-bubble">
          <div className="bubble-content">
            {messageBuffer}
          </div>
          <div className="bubble-tail"></div>
        </div>
      )}
    </div>
  );
};

export default LuminAI;