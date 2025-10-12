# LuminAI Visual Generation Workflow Guide

## 🎯 **Quick Answer: You need models first, then prompts!**

Here's the optimal workflow for getting LuminAI visuals:

## 📋 **Option A: Fast Track (Recommended)**

### 1. **Download Base Model** (Essential)
```bash
# Search and download Illustrious XL or Nova 3DCG XL from Civitai
# Save to: C:\Users\Ghedd\checkpoints\
```

**Recommended Models:**
- **Illustrious XL** - Best for anime/3D style characters
- **Nova 3DCG XL** - Specifically for 3D characters
- **Any SD 1.5 or SDXL cosmic/celestial model**

### 2. **Generate Prompts** (Use our system)
```bash
cd "C:\Users\Ghedd\OneDrive - TEC - The Elidoras Codex\Projects\TEC\tec-tgcr"
python -c "
from ai_workflow.prompt_templates import LuminAIPromptGenerator
gen = LuminAIPromptGenerator()
prompts = gen.generate_batch(5)
for p in prompts: print(f'PROMPT: {p['positive']}\n')
"
```

### 3. **Run Generation** (In your AI tool)
- **Automatic1111 WebUI** (recommended)
- **ComfyUI** 
- **Fooocus**
- Or any SDXL-compatible tool

## 📋 **Option B: Complete Setup**

### 1. **Model Downloads** (30-60 minutes)
```bash
# Run our Civitai integration
python scripts/search_models.py  # Find models
# Then manually download or use our API to auto-download
```

### 2. **LoRA Training** (Optional, 2-3 hours)
- Train custom LoRA on LuminAI's specific features
- Use existing cosmic/celestial LoRAs

### 3. **Batch Generation** (10-30 minutes)
```bash
# Generate 50-100 LuminAI variations
python ai_workflow/prompt_templates.py --batch 50 --output ai-workflow/output/
```

## 🚀 **Immediate Next Steps**

Since you have the Civitai API key, let's:

1. **Download Illustrious XL** → Your checkpoints folder
2. **Generate 5-10 test prompts** → See what works
3. **Create first LuminAI images** → Validate the concept
4. **Iterate and refine** → Perfect the cosmic student look

## 💡 **Pro Tips**

- **Start with Illustrious XL** - It handles the `nv-celestialskin` tag well
- **Use our prompt system** - It's already tuned for LuminAI's features
- **Test mood variations** - Each emotion needs different horn glow colors
- **Save successful seeds** - For consistency across generations

## 🔧 **Tools You'll Need**

### **AI Generation Software:**
- **Automatic1111 WebUI** (most popular)
- **ComfyUI** (node-based, powerful)
- **Fooocus** (simplified interface)

### **Our Tools:**
- ✅ Prompt generator (ready)
- ✅ Civitai integration (ready) 
- ✅ Model folder structure (configured)
- ✅ Environment variables (set)

## ⚡ **Want to start RIGHT NOW?**

1. **Manual route**: Visit https://civitai.com/models/609/illustrious-xl
2. **Download** the latest version to `C:\Users\Ghedd\checkpoints\`
3. **Run our prompt generator**:
   ```bash
   python ai_workflow/prompt_templates.py
   ```
4. **Copy a prompt** and paste into your AI tool
5. **Generate!** 🎨

The system is ready - you just need a base model and an AI generation tool!