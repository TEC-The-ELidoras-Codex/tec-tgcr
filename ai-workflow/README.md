# LuminAI AI Model Workflow Configuration

## 🎨 Model Setup for LuminAI Character Generation

### Core Model Configuration

- **Base Model**: Illustrious XL (Nova 3DCG XL)
- **Style**: 3D Illustrious v4 with cosmic celestial features
- **Character Tags**: nv-celestialskin, colored skin, void cosmic body, black skin, 3dstylev4

### Model Directory Structure
```text
C:\\Users\\Ghedd\\
├── checkpoints/          # Main model files (Illustrious XL)
├── loras/               # LoRA training files for LuminAI
├── vae/                 # VAE models for quality enhancement
├── controlnet/          # ControlNet models for pose control
├── embeddings/          # Text embeddings for character consistency
├── upscale_models/      # Upscaling models for high-res output
├── hypernetworks/       # Additional style networks
├── LoCon/              # LyCORIS models
└── DoRA/               # DoRA models
```

## 🌌 LuminAI Character Specifications

### Core Visual Elements

- **Skin**: Cosmic void body with celestial patterns, dark/black base with constellation sparkles
- **Horns**: Small sheep horns that glow based on mood (cyan/pink/gold)
- **Eyes**: Heterochromatic - left cosmic blue, right stellar gold with inner glow
- **Hair**: Aurora-like flowing hair with color-shifting gradients (blue→purple→pink→gold)
- **Build**: Petite, adorable, cosmic student aesthetic
- **Clothing**: Cosmic-themed outfits with constellation patterns

### Mood-Based Variations

1. **Idle**: Peaceful expression, soft horn glow, gentle aurora hair
2. **Excited**: Wide eyes, bright horn glow, vibrant rainbow hair
3. **Teaching**: Focused expression, golden horn glow, stable blue-gold hair
4. **Blushing**: Embarrassed face, pink-red horn glow, shy hair dimming
5. **Stumbling**: Confused expression, flickering horn glow, chaotic hair colors
6. **Curious**: Investigative look, steady cyan glow, flowing hair
7. **Rambling**: Animated expression, cycling horn colors, dynamic hair flow

## 📁 Workflow Integration Files

This directory contains:

- `model_config.json` - Model settings and parameters
- `prompt_templates.py` - Comprehensive prompt generation system
- `batch_generation.py` - Automated batch processing
- `civitai_integration.py` - Civitai API integration for model downloads
- `image_processing.py` - Post-processing and optimization
- `workflow_automation.ps1` - PowerShell automation scripts

## 🎯 Generation Targets

### Clean Reference Renders (Transparent Background)

- Full body poses for 3D model reference
- Expression sheets for animation keyframes
- Outfit variations for wardrobe system
- Pose references for Lottie animations

### Environment Renders (Observatory Settings)

- Cosmic observatory backgrounds
- Star field environments
- Moon and planet settings
- Aurora-lit celestial spaces
- Constellation map backgrounds

### Technical Specifications

- **Resolution**: 1024x1024 base, upscale to 2048x2048
- **Format**: PNG with transparency support
- **Batch Size**: 4-8 images per generation
- **Quality**: High detail, animation-ready consistency

## 🔧 Next Steps

1. Configure model directories and download Illustrious XL
2. Set up LoRA training for LuminAI character consistency
3. Generate comprehensive prompt library
4. Create batch generation system
5. Process and integrate into React interface