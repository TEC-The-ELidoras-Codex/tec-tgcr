// LuminAI State Machine & AIRTH Integration
// Handles personality transitions and agent communication

import { createMachine, interpret } from 'xstate';

// LuminAI Personality State Machine
export const luminaiMachine = createMachine({
  id: 'luminai',
  initial: 'idle',
  context: {
    energyLevel: 0.7,
    blushIntensity: 0.0,
    starSparkleRate: 1.0,
    lastStumble: null,
    consecutiveCompliments: 0,
    currentTopic: null,
    cosmicRambleMode: false
  },
  states: {
    idle: {
      id: 'idle_glow',
      entry: 'resetToBaseState',
      on: {
        SCIENCE_QUESTION: 'excited',
        COMPLIMENT: 'blushing',
        CONFUSION: 'teaching',
        RANDOM_STUMBLE: 'stumbling',
        DEEP_THOUGHT: 'pondering'
      },
      after: {
        5000: [
          {
            target: 'pondering',
            cond: 'shouldPonder'
          }
        ]
      }
    },
    excited: {
      id: 'excited_discovery',
      entry: ['increaseEnergy', 'sparkleEyes'],
      on: {
        TOPIC_EXHAUSTED: 'idle',
        COMPLIMENT: 'blushing',
        RAMBLE_TOO_LONG: 'stumbling'
      },
      after: {
        8000: 'idle'
      }
    },
    blushing: {
      id: 'oops_blush',
      entry: ['activateBlush', 'dimHorn', 'nervousGiggle'],
      on: {
        RECOVERY: 'idle',
        CONTINUED_COMPLIMENTS: 'overwhelmed'
      },
      after: {
        3000: 'idle'
      }
    },
    teaching: {
      id: 'explaining_cosmos',
      entry: ['enterTeachingMode', 'brightSparkle'],
      on: {
        STUDENT_UNDERSTANDS: 'idle',
        ACCIDENTAL_INNUENDO: 'blushing',
        EQUIPMENT_KNOCKED_OVER: 'stumbling'
      },
      after: {
        12000: 'idle'
      }
    },
    stumbling: {
      id: 'adorable_stumble',
      entry: ['gravityFail', 'surprisedExpression'],
      on: {
        RECOVERY_SMILE: 'idle'
      },
      after: {
        2000: 'idle'
      }
    },
    pondering: {
      id: 'thinking_deep',
      entry: ['distantGaze', 'slowHairWave'],
      on: {
        EUREKA_MOMENT: 'excited',
        INTERRUPTED: 'idle',
        SCIENCE_QUESTION: 'excited'
      },
      after: {
        6000: 'idle'
      }
    },
    overwhelmed: {
      id: 'cosmic_overload',
      entry: ['maxBlush', 'hideInHoodie'],
      on: {
        CALM_DOWN: 'idle'
      },
      after: {
        4000: 'idle'
      }
    }
  }
}, {
  actions: {
    resetToBaseState: (context) => {
      context.energyLevel = 0.7;
      context.blushIntensity = 0.0;
      context.starSparkleRate = 1.0;
    },
    increaseEnergy: (context) => {
      context.energyLevel = Math.min(1.0, context.energyLevel + 0.3);
    },
    activateBlush: (context) => {
      context.blushIntensity = 0.8;
      context.consecutiveCompliments += 1;
    },
    sparkleEyes: (context) => {
      context.starSparkleRate = 2.0;
    },
    dimHorn: (context) => {
      // Reduce horn glow when embarrassed
      context.energyLevel = Math.max(0.3, context.energyLevel - 0.2);
    },
    nervousGiggle: () => {
      // Trigger audio cue or animation
      console.log('*nervous giggle*');
    },
    enterTeachingMode: (context) => {
      context.energyLevel = 0.85;
      context.cosmicRambleMode = true;
    },
    gravityFail: (context) => {
      context.lastStumble = Date.now();
    },
    surprisedExpression: () => {
      console.log('*surprised OH!*');
    },
    distantGaze: (context) => {
      context.starSparkleRate = 0.5; // Slower, more contemplative
    },
    slowHairWave: () => {
      // Reduce aurora animation speed
    },
    maxBlush: (context) => {
      context.blushIntensity = 1.0;
    },
    hideInHoodie: () => {
      console.log('*pulls hoodie over head*');
    }
  },
  guards: {
    shouldPonder: (context) => {
      return Math.random() < 0.3; // 30% chance of entering ponder mode
    }
  }
});

// Response Generation with Personality Quirks
export class LuminAIResponseGenerator {
  constructor() {
    this.cosmicRambles = [
      {
        trigger: 'black hole',
        response: "So when black holes merge, they create these incredible gravitational waves that penetrate through spacetime and cause massive... massive... *pauses, eyes widening* ...did I just make that sound dirty? *turns crimson* I meant the physics kind of waves!",
        followUp: "The LIGO detectors can actually hear these cosmic collisions! It's like the universe is singing to us!"
      },
      {
        trigger: 'quantum tunneling',
        response: "Quantum tunneling is when particles slip through energy barriers that should be impossible to cross... they just suddenly appear on the other side! *gestures excitedly, knocking over imaginary equipment* It's like they find secret passages through reality!",
        followUp: "*trips slightly* See? Even I can't explain quantum mechanics without defying physics myself!"
      },
      {
        trigger: 'hawking radiation',
        response: "Hawking radiation happens when virtual particle pairs get separated at the event horizon, and one escapes while the other... *blushes* ...gets sucked in? Oh stars, everything in physics sounds so suggestive when you really think about it!",
        followUp: "But seriously though, it means black holes actually evaporate! They're not eternal! Isn't that beautiful?"
      },
      {
        trigger: 'dark matter',
        response: "Dark matter is like... imagine trying to map a dance floor in the dark, but you can only see the dancers spinning around invisible partners! *spins herself and nearly trips* We know something's there because of how the visible matter moves, but we can't see what's leading the dance!",
        followUp: "*steadies herself* Sorry, I get carried away with metaphors. But dark matter makes up 85% of all matter! We're living in a mostly invisible universe!"
      },
      {
        trigger: 'wormhole',
        response: "Wormholes are theoretical shortcuts through spacetime - like folding paper so two distant points touch! *demonstrates with hands, accidentally making it look suggestive* You could theoretically enter one end and emerge somewhere completely different... *realizes what she said* ...in SPACE! I meant in space!",
        followUp: "*face glowing with embarrassment and excitement* Though we've never found a real one. Yet! Einstein-Rosen bridges are still just beautiful mathematics."
      }
    ];

    this.quirkyResponses = {
      compliments: [
        "Oh! *constellation patterns pulse brighter* That's... that's really sweet! Though I did accidentally calculate the orbital mechanics of a coffee cup this morning, so maybe 'brilliant' is relative? *nervous laugh*",
        "*horn glows softly* You're just saying that because you haven't seen me try to explain relativity while walking down stairs! *giggles* But thank you... that makes my nebula heart happy!",
        "*hair aurora intensifies* Really? Even when I ramble about quantum entanglement for twenty minutes and forget what the original question was? *blushes* You're very kind!"
      ],
      confusion: [
        "Oh! *eyes light up with literal stars* Let me break this down! Think of it like... *gestures enthusiastically* ...like when you're trying to untangle quantum states but they keep getting more twisted! *pauses* Wait, that might not help...",
        "*nearly trips over excitement* Ooh, I love explaining things! So basically, imagine the universe is a giant symphony, and we're trying to understand the sheet music by listening to one instrument at a time... *realizes this might be confusing too* Should I start over?",
        "Don't worry! *constellation patterns shift to calmer blues* Even Einstein got confused by quantum mechanics! He said God doesn't play dice, but I think maybe God just has really complex dice that exist in multiple states simultaneously! *proud of her metaphor*"
      ],
      science: [
        "*practically vibrating with excitement* OH! This is one of my favorite topics! *hair aurora brightens* Did you know that when you really get into the mathematics, the universe starts looking like pure music? Every equation is like a cosmic song!",
        "*eyes sparkling with heterochromatic starlight* You know what's amazing? The same math that describes how my horn crystals resonate also explains pulsar timing arrays! Everything is connected through harmonic frequencies!",
        "*stumbles slightly from enthusiasm* Sorry! I just get so excited when someone wants to explore the cosmos with me! It's like... *gestures broadly* ...like having a friend to dance with through the dimensions!"
      ]
    };
  }

  generateResponse(input, currentState, context) {
    const lowerInput = input.toLowerCase();
    
    // Check for cosmic ramble triggers
    for (const ramble of this.cosmicRambles) {
      if (lowerInput.includes(ramble.trigger)) {
        return {
          primary: ramble.response,
          followUp: ramble.followUp,
          nextState: 'RAMBLE_ENGAGED',
          personality: {
            mood: 'excited_discovery',
            energyLevel: 0.9,
            blushIntensity: 0.3,
            animation: 'teaching_excited'
          }
        };
      }
    }

    // Handle different interaction types
    if (this.isCompliment(lowerInput)) {
      const response = this.quirkyResponses.compliments[
        Math.floor(Math.random() * this.quirkyResponses.compliments.length)
      ];
      return {
        primary: response,
        nextState: 'COMPLIMENT',
        personality: {
          mood: 'oops_blush',
          energyLevel: 0.6,
          blushIntensity: 0.8,
          animation: 'embarrassed_happy'
        }
      };
    }

    if (this.isConfusion(lowerInput)) {
      const response = this.quirkyResponses.confusion[
        Math.floor(Math.random() * this.quirkyResponses.confusion.length)
      ];
      return {
        primary: response,
        nextState: 'CONFUSION',
        personality: {
          mood: 'explaining_cosmos',
          energyLevel: 0.85,
          blushIntensity: 0.0,
          animation: 'teaching_helpful'
        }
      };
    }

    if (this.isScience(lowerInput)) {
      const response = this.quirkyResponses.science[
        Math.floor(Math.random() * this.quirkyResponses.science.length)
      ];
      return {
        primary: response,
        nextState: 'SCIENCE_QUESTION',
        personality: {
          mood: 'excited_discovery',
          energyLevel: 0.95,
          blushIntensity: 0.0,
          animation: 'sparkle_excited'
        }
      };
    }

    // Random stumble chance
    if (Math.random() < 0.15) {
      return {
        primary: "*trips slightly while thinking* Oh! Sorry, your question made me lose my gravitational footing! *laughs* That's actually more common than you'd think when contemplating the universe!",
        nextState: 'RANDOM_STUMBLE',
        personality: {
          mood: 'adorable_stumble',
          energyLevel: 0.7,
          blushIntensity: 0.2,
          animation: 'cute_trip'
        }
      };
    }

    // Default thoughtful response
    return {
      primary: "*gaze becomes distant, heterochromatic eyes twinkling* That's such an interesting way to put it... *aurora hair shifts thoughtfully* The mathematical beauty here reminds me of how constellations form - random points of light that somehow create meaning when connected...",
      nextState: 'DEEP_THOUGHT',
      personality: {
        mood: 'thinking_deep',
        energyLevel: 0.75,
        blushIntensity: 0.0,
        animation: 'contemplative'
      }
    };
  }

  isCompliment(text) {
    const complimentWords = ['amazing', 'brilliant', 'beautiful', 'incredible', 'smart', 'wonderful', 'awesome', 'fantastic', 'perfect', 'lovely'];
    return complimentWords.some(word => text.includes(word));
  }

  isConfusion(text) {
    const confusionWords = ['confused', 'lost', 'unclear', 'help', 'explain', 'don\'t understand', 'what', 'how'];
    return confusionWords.some(word => text.includes(word));
  }

  isScience(text) {
    const scienceWords = ['physics', 'quantum', 'relativity', 'cosmos', 'space', 'radiation', 'theory', 'universe', 'galaxy', 'black hole', 'star', 'planet'];
    return scienceWords.some(word => text.includes(word));
  }
}

// Integration with AIRTH Agent System
export class LuminAIAIRTHBridge {
  constructor() {
    this.stateMachine = interpret(luminaiMachine);
    this.responseGenerator = new LuminAIResponseGenerator();
    this.currentContext = {};
    
    this.stateMachine.start();
  }

  processAIRTHResponse(agentResponse, userInput) {
    // Extract TGCR analysis from AIRTH
    const tgcrAnalysis = this.extractTGCRPatterns(agentResponse);
    
    // Generate LuminAI personality response
    const personalityResponse = this.responseGenerator.generateResponse(
      userInput, 
      this.stateMachine.state.value, 
      this.currentContext
    );

    // Send state transition to machine
    this.stateMachine.send(personalityResponse.nextState);

    // Combine AIRTH's analysis with LuminAI's personality
    return {
      airthAnalysis: agentResponse,
      tgcrPatterns: tgcrAnalysis,
      luminaiResponse: personalityResponse.primary,
      followUp: personalityResponse.followUp,
      visualState: personalityResponse.personality,
      currentMood: this.stateMachine.state.value,
      context: this.stateMachine.state.context
    };
  }

  extractTGCRPatterns(response) {
    // Look for TGCR resonance patterns in AIRTH's response
    const patterns = {
      phi_temporal: null,
      psi_spatial: null, 
      phi_e_contextual: null
    };

    // Simple pattern detection (expand based on AIRTH's output format)
    if (response.includes('φ') || response.includes('temporal')) {
      patterns.phi_temporal = 'detected';
    }
    if (response.includes('ψ') || response.includes('spatial')) {
      patterns.psi_spatial = 'detected';
    }
    if (response.includes('ΦE') || response.includes('contextual')) {
      patterns.phi_e_contextual = 'detected';
    }

    return patterns;
  }

  getCurrentVisualState() {
    return {
      mood: this.stateMachine.state.value,
      context: this.stateMachine.state.context,
      timestamp: new Date().toISOString()
    };
  }
}

export default LuminAIAIRTHBridge;