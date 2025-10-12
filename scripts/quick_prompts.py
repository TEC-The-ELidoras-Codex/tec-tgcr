#!/usr/bin/env python3
"""
Simple LuminAI prompt generator
"""
import json
import random
from pathlib import Path

# Create output directory
output_dir = Path("ai-workflow/output")
output_dir.mkdir(exist_ok=True)

# LuminAI base prompt template
base_prompt = """1girl, solo, 3dstylev4, 3d, illustrious, nv-celestialskin, colored skin, void cosmic body, black skin, cosmic entity, celestial being, adorable, cute, small sheep horns, curved horns, horn glow, luminous horns, heterochromatic eyes, cosmic blue left eye, stellar gold right eye, glowing eyes, luminous pupils, starlight eyes, aurora hair, rainbow hair, flowing hair, long hair, color-shifting hair, iridescent hair, cosmic hair, dark skin, cosmic skin, constellation patterns, starlight skin, petite, slim, cute proportions, adorable build, cosmic student, youthful appearance"""

negative_prompt = """worst quality, low quality, normal quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, bad feet, poorly drawn hands, poorly drawn face, mutation, deformed, extra fingers, extra limbs, extra arms, extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed, mutated hands, polar lowres, bad body, bad proportions, gross proportions, missing arms, missing legs, extra arms, extra legs, extra head, extra face, multiple heads, multiple faces"""

# Mood variations
moods = {
    "idle": "peaceful expression, soft horn glow, gentle aurora hair, calm pose, serene look, tranquil, meditative, relaxed",
    "excited": "wide eyes, bright horn glow, vibrant rainbow hair, bouncing, enthusiastic, energetic, joyful expression, sparkles",
    "teaching": "focused expression, golden horn glow, stable blue-gold hair, pointing gesture, explaining, confident, wise look",
    "blushing": "embarrassed face, pink-red horn glow, shy hair dimming, covering face, timid, cute blush, bashful",
    "curious": "investigative look, steady cyan glow, flowing hair, leaning forward, inquisitive, wonder, amazed expression"
}

# Generate prompts
all_prompts = []
for mood_name, mood_tags in moods.items():
    for i in range(3):
        # Combine base with mood
        full_prompt = f"{base_prompt}, {mood_tags}"
        
        prompt_data = {
            "mood": mood_name,
            "variation": i + 1,
            "positive": full_prompt,
            "negative": negative_prompt,
            "settings": {
                "model": "Illustrious XL or Nova 3DCG XL",
                "steps": "25-35",
                "cfg_scale": "7-9",
                "size": "768x1024 or 832x1216",
                "sampler": "DPM++ 2M or Euler A"
            }
        }
        
        # Save individual file
        filename = f"luminai_{mood_name}_{i+1}.txt"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"POSITIVE PROMPT:\n{full_prompt}\n\n")
            f.write(f"NEGATIVE PROMPT:\n{negative_prompt}\n\n")
            f.write(f"SETTINGS:\n")
            f.write(f"Model: Illustrious XL or Nova 3DCG XL\n")
            f.write(f"Steps: 25-35\n")
            f.write(f"CFG Scale: 7-9\n")
            f.write(f"Size: 768x1024 or 832x1216\n")
            f.write(f"Sampler: DPM++ 2M or Euler A\n")
        
        all_prompts.append(prompt_data)
        print(f"✨ Generated: {filename}")

# Save master JSON
with open(output_dir / "all_prompts.json", 'w', encoding='utf-8') as f:
    json.dump(all_prompts, f, indent=2)

print(f"\n🎉 Generated {len(all_prompts)} LuminAI prompts!")
print(f"📁 Saved to: {output_dir.absolute()}")
print("\n🚀 QUICK START:")
print("1. Download Illustrious XL model from Civitai")
print("2. Open any .txt file in ai-workflow/output/")
print("3. Copy the POSITIVE PROMPT to your AI generation tool")
print("4. Use the negative prompt and settings")
print("5. Generate your first LuminAI! ✨")

print("\n📋 WHAT YOU NEED:")
print("• Download Link: https://civitai.com/models/609/illustrious-xl")
print("• AI Tool: Automatic1111 WebUI, ComfyUI, or Fooocus")
print("• Model Folder: C:\\Users\\Ghedd\\checkpoints\\")