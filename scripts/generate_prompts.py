#!/usr/bin/env python3
"""
Generate LuminAI prompts and save to files
"""
import sys
import json
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / 'src'))

# Import the prompt generator
sys.path.append('ai-workflow')
exec(open('ai-workflow/prompt_templates.py').read())

def generate_sample_prompts():
    """Generate sample prompts for immediate use"""
    generator = LuminAIPromptGenerator()
    
    print("🌟 Generating LuminAI Character Prompts...\n")
    
    # Generate prompts for each mood
    output_dir = Path("ai-workflow/output")
    output_dir.mkdir(exist_ok=True)
    
    moods = ["idle", "excited", "teaching", "blushing", "curious"]
    all_prompts = []
    
    for mood in moods:
        print(f"✨ Generating {mood.title()} state prompts...")
        batch = generator.generate_batch(3, mood_filter=[mood])
        
        for i, prompt_data in enumerate(batch):
            filename = f"luminai_{mood}_{i+1}.txt"
            filepath = output_dir / filename
            
            # Write prompt to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"POSITIVE PROMPT:\n{prompt_data['positive']}\n\n")
                f.write(f"NEGATIVE PROMPT:\n{prompt_data['negative']}\n\n")
                f.write("SETTINGS:\n")
                f.write("Model: Illustrious XL or Nova 3DCG XL\n")
                f.write("Steps: 25-35\n")
                f.write("CFG Scale: 7-9\n")
                f.write("Size: 768x1024 or 832x1216\n")
                f.write("Sampler: DPM++ 2M or Euler A\n")
            
            print(f"  📝 Saved: {filename}")
            
    
    # Save master JSON
    with open(output_dir / "all_prompts.json", 'w', encoding='utf-8') as f:
        json.dump(all_prompts, f, indent=2)
    
    print(f"\n🎉 Generated {len(all_prompts)} prompts!")
    print(f"📁 Saved to: {output_dir.absolute()}")
    print("\n🚀 QUICK START:")
    print("1. Download Illustrious XL model")
    print("2. Open any .txt file in ai-workflow/output/")
    print("3. Copy the POSITIVE PROMPT to your AI tool")
    print("4. Generate LuminAI! ✨")

if __name__ == "__main__":
    generate_sample_prompts()