"""
LuminAI Prompt Generation System
Comprehensive prompt templates for generating LuminAI character variations
with cosmic celestial features using Illustrious XL model
"""

import json
import random
from typing import List, Dict, Any
from dataclasses import dataclass
from types import SimpleNamespace
from enum import Enum


class MoodState(Enum):
    IDLE = "idle"
    EXCITED = "excited"
    TEACHING = "teaching"
    BLUSHING = "blushing"
    STUMBLING = "stumbling"
    CURIOUS = "curious"
    RAMBLING = "rambling"


class BackgroundType(Enum):
    TRANSPARENT = "transparent"
    OBSERVATORY = "observatory"
    COSMIC = "cosmic"
    NEUTRAL = "neutral"


class LuminAIPromptGenerator:
    def __init__(self) -> None:
        # Minimal character placeholder used by prompts; this mirrors expected
        # attributes elsewhere in the file and keeps the module runnable for
        # quick examples. A fuller Character model can be restored later.
        self.character = SimpleNamespace(
            base_tags=["luminai", "character", "portrait"],
            horns=["small horn", "curved horn", "ornate horn"],
            eyes=["bright eyes", "sparkling eyes", "soft gaze"],
            hair=["flowing hair", "aurora hair", "starlit hair"],
            skin=["porcelain skin", "sun-kissed skin"],
            body=["slim build", "athletic build", "childlike build"],
        )

        # initialize the various libraries and configs
        self.outfit_library = self._init_outfit_library()
        self.mood_configs = self._init_mood_configs()
        self.pose_library = self._init_pose_library()
        self.background_library = self._init_background_library()
        self.pose_library = self._init_pose_library()
        self.background_library = self._init_background_library()

    def _init_mood_configs(self) -> Dict[MoodState, Dict[str, Any]]:
        """Initialize mood-specific configurations"""
        return {
            MoodState.IDLE: {
                "expression": [
                    "peaceful expression",
                    "calm face",
                    "serene look",
                    "gentle smile",
                ],
                "horn_glow": [
                    "soft blue horn glow",
                    "gentle cyan light",
                    "peaceful aura",
                ],
                "hair_colors": [
                    "gentle blue-purple gradient",
                    "soft aurora colors",
                    "calm color shift",
                ],
                "eye_intensity": ["soft glow", "gentle luminosity", "peaceful shine"],
                "pose_modifiers": [
                    "relaxed pose",
                    "comfortable stance",
                    "peaceful posture",
                ],
            },
            MoodState.EXCITED: {
                "expression": [
                    "excited expression",
                    "wide eyes",
                    "bright smile",
                    "enthusiastic face",
                ],
                "horn_glow": [
                    "bright cyan horn glow",
                    "vibrant blue light",
                    "excited aura",
                ],
                "hair_colors": [
                    "vibrant rainbow hair",
                    "bright aurora colors",
                    "rapid color cycling",
                ],
                "eye_intensity": ["bright sparkle", "high luminosity", "excited shine"],
                "pose_modifiers": [
                    "energetic pose",
                    "bouncing",
                    "dynamic stance",
                    "animated gesture",
                ],
            },
            MoodState.TEACHING: {
                "expression": [
                    "focused expression",
                    "explaining",
                    "teaching face",
                    "concentrated look",
                ],
                "horn_glow": [
                    "golden horn glow",
                    "warm yellow light",
                    "scholarly aura",
                ],
                "hair_colors": [
                    "stable blue-gold gradient",
                    "academic colors",
                    "wise color shift",
                ],
                "eye_intensity": [
                    "focused glow",
                    "bright attention",
                    "scholarly shine",
                ],
                "pose_modifiers": [
                    "pointing gesture",
                    "explaining pose",
                    "teaching stance",
                    "demonstrating",
                ],
            },
            MoodState.BLUSHING: {
                "expression": [
                    "embarrassed face",
                    "blushing",
                    "shy expression",
                    "covering face",
                ],
                "horn_glow": [
                    "pink-red horn glow",
                    "warm blush light",
                    "embarrassed aura",
                ],
                "hair_colors": [
                    "pink-purple shy colors",
                    "dimmed aurora",
                    "bashful color shift",
                ],
                "eye_intensity": ["soft averted gaze", "shy glow", "embarrassed shine"],
                "pose_modifiers": [
                    "shy pose",
                    "covering gesture",
                    "embarrassed stance",
                    "bashful posture",
                ],
            },
            MoodState.STUMBLING: {
                "expression": [
                    "confused expression",
                    "dizzy face",
                    "stumbling look",
                    "disoriented",
                ],
                "horn_glow": ["flickering horn glow", "unstable light", "chaotic aura"],
                "hair_colors": [
                    "chaotic hair colors",
                    "confused aurora",
                    "random color shift",
                ],
                "eye_intensity": ["dizzy glow", "confused shine", "disoriented light"],
                "pose_modifiers": [
                    "stumbling pose",
                    "off-balance",
                    "clumsy stance",
                    "confused gesture",
                ],
            },
            MoodState.CURIOUS: {
                "expression": [
                    "curious expression",
                    "investigative look",
                    "wondering face",
                    "inquisitive",
                ],
                "horn_glow": [
                    "steady cyan glow",
                    "investigative light",
                    "curious aura",
                ],
                "hair_colors": [
                    "flowing aurora colors",
                    "investigative hues",
                    "curious color shift",
                ],
                "eye_intensity": [
                    "bright investigation",
                    "curious glow",
                    "wondering shine",
                ],
                "pose_modifiers": [
                    "leaning forward",
                    "investigating pose",
                    "curious stance",
                    "examining",
                ],
            },
            MoodState.RAMBLING: {
                "expression": [
                    "animated expression",
                    "talking",
                    "explaining rapidly",
                    "enthusiastic speech",
                ],
                "horn_glow": ["cycling horn colors", "dynamic light", "animated aura"],
                "hair_colors": [
                    "dynamic hair flow",
                    "rapid aurora shift",
                    "animated colors",
                ],
                "eye_intensity": ["dynamic glow", "animated shine", "expressive light"],
                "pose_modifiers": [
                    "animated gestures",
                    "talking pose",
                    "expressive stance",
                    "demonstrating",
                ],
            },
        }

    def _init_outfit_library(self) -> Dict[str, List[str]]:
        """Initialize outfit variations"""
        return {
            "cosmic_casual": [
                "cosmic hoodie",
                "constellation print hoodie",
                "starry sweatshirt",
                "cosmic pleated skirt",
                "starry mini skirt",
                "constellation pattern skirt",
                "thigh-high cosmic socks",
                "star pattern stockings",
                "aurora knee socks",
                "cosmic sneakers",
                "starlight shoes",
                "aurora-colored footwear",
            ],
            "student_outfit": [
                "cosmic school uniform",
                "celestial blazer",
                "starry sailor outfit",
                "constellation tie",
                "cosmic collar",
                "stellar accessories",
                "cosmic backpack",
                "star-themed bag",
                "celestial school items",
            ],
            "observatory_gear": [
                "cosmic lab coat",
                "astronomical equipment",
                "telescope accessories",
                "star chart prints",
                "cosmic research outfit",
                "celestial scientist gear",
                "observatory uniform",
                "astronomical instruments",
                "cosmic tools",
            ],
            "casual_cosmic": [
                "cosmic t-shirt",
                "starry tank top",
                "constellation graphics",
                "cosmic jeans",
                "starry shorts",
                "aurora-colored pants",
                "cosmic accessories",
                "star jewelry",
                "celestial ornaments",
            ],
            "formal_cosmic": [
                "cosmic dress",
                "stellar formal wear",
                "constellation gown",
                "cosmic suit",
                "starry blazer",
                "celestial formal outfit",
                "aurora-colored formal wear",
                "cosmic evening dress",
            ],
        }

    def _init_pose_library(self) -> Dict[str, List[str]]:
        """Initialize pose variations"""
        return {
            "standing": [
                "standing straight",
                "confident stance",
                "relaxed standing",
                "hand on hip",
                "arms crossed",
                "hands behind back",
                "casual standing",
                "formal posture",
                "cute pose",
            ],
            "sitting": [
                "sitting on chair",
                "sitting cross-legged",
                "sitting on desk",
                "sitting casually",
                "formal sitting",
                "observatory chair",
                "cosmic throne",
                "floating sitting",
                "meditation pose",
            ],
            "action": [
                "pointing at stars",
                "explaining gesture",
                "teaching pose",
                "investigating",
                "examining cosmic phenomena",
                "demonstrating",
                "reaching for stars",
                "cosmic interaction",
                "magical gesture",
            ],
            "expressions": [
                "looking at viewer",
                "profile view",
                "three-quarter view",
                "looking up at stars",
                "examining closely",
                "surprised look",
                "thinking pose",
                "explaining face",
                "curious gaze",
            ],
            "full_body": [
                "full body shot",
                "complete figure",
                "head to toe",
                "dynamic full pose",
                "character sheet pose",
                "reference pose",
            ],
            "portrait": [
                "close-up portrait",
                "head and shoulders",
                "bust shot",
                "detailed face",
                "expression focus",
                "emotional portrait",
            ],
        }

    def _init_background_library(self) -> Dict[BackgroundType, List[str]]:
        """Initialize background variations"""
        return {
            BackgroundType.TRANSPARENT: [
                "transparent background",
                "white background",
                "simple background",
                "no background",
                "plain background",
                "clean background",
            ],
            BackgroundType.OBSERVATORY: [
                "cosmic observatory",
                "astronomical dome",
                "telescope facility",
                "star observation deck",
                "cosmic research station",
                "celestial laboratory",
                "space observation room",
                "astronomical equipment",
                "cosmic instruments",
            ],
            BackgroundType.COSMIC: [
                "starry sky",
                "cosmic void",
                "nebula background",
                "galaxy backdrop",
                "aurora borealis",
                "constellation map",
                "cosmic phenomena",
                "stellar nursery",
                "cosmic landscape",
                "celestial environment",
            ],
            BackgroundType.NEUTRAL: [
                "studio lighting",
                "soft lighting",
                "professional photography",
                "portrait lighting",
                "clean environment",
                "minimal background",
            ],
        }

    def generate_base_prompt(self, mood: MoodState, background: BackgroundType) -> str:
        """Generate base prompt with character essentials"""
        mood_config = self.mood_configs[mood]

        # Core character
        prompt_parts = self.character.base_tags.copy()

        # Add physical features
        prompt_parts.extend(
            [
                random.choice(self.character.horns),
                random.choice(self.character.eyes),
                random.choice(self.character.hair),
                random.choice(self.character.skin),
                random.choice(self.character.body),
            ]
        )

        # Add mood-specific elements
        prompt_parts.append(random.choice(mood_config["expression"]))
        prompt_parts.append(random.choice(mood_config["horn_glow"]))
        prompt_parts.append(random.choice(mood_config["hair_colors"]))
        prompt_parts.append(random.choice(mood_config["eye_intensity"]))

        # Add background
        prompt_parts.append(random.choice(self.background_library[background]))

        return ", ".join(prompt_parts)

    def generate_outfit_prompt(self, outfit_category: str) -> str:
        """Generate outfit-specific prompt additions"""
        if outfit_category in self.outfit_library:
            return ", ".join(random.sample(self.outfit_library[outfit_category], 3))
        return ""

    def generate_pose_prompt(self, pose_category: str) -> str:
        """Generate pose-specific prompt additions"""
        if pose_category in self.pose_library:
            return ", ".join(random.sample(self.pose_library[pose_category], 2))
        return ""

    def generate_quality_tags(self) -> str:
        """Generate quality and technical tags"""
        quality_tags = [
            "masterpiece",
            "best quality",
            "ultra-detailed",
            "8k",
            "highly detailed",
            "professional artwork",
            "amazing quality",
            "cosmic art",
            "stellar quality",
            "celestial masterpiece",
            "cosmic rendering",
            "3d illustration",
        ]
        return ", ".join(random.sample(quality_tags, 5))

    def generate_negative_prompt(self) -> str:
        """Generate negative prompt to avoid unwanted elements"""
        negative_tags = [
            "worst quality",
            "low quality",
            "blurry",
            "jpeg artifacts",
            "watermark",
            "signature",
            "text",
            "logo",
            "ugly",
            "deformed",
            "extra limbs",
            "missing limbs",
            "bad anatomy",
            "disfigured",
            "bad proportions",
            "malformed",
            "mutation",
            "duplicate",
            "error",
            "cropped",
            "out of frame",
            "lowres",
            "normal quality",
        ]
        return ", ".join(negative_tags)

    def generate_complete_prompt(
        self,
        mood: MoodState = MoodState.IDLE,
        background: BackgroundType = BackgroundType.TRANSPARENT,
        outfit_category: str = "cosmic_casual",
        pose_category: str = "standing",
        include_quality: bool = True,
    ) -> Dict[str, str]:
        """Generate complete prompt with all elements"""

        # Build prompt components
        base_prompt = self.generate_base_prompt(mood, background)
        outfit_prompt = self.generate_outfit_prompt(outfit_category)
        pose_prompt = self.generate_pose_prompt(pose_category)
        quality_prompt = self.generate_quality_tags() if include_quality else ""
        negative_prompt = self.generate_negative_prompt()

        # Combine all parts
        positive_parts = [base_prompt, outfit_prompt, pose_prompt]
        if quality_prompt:
            positive_parts.append(quality_prompt)

        positive_prompt = ", ".join(filter(None, positive_parts))

        return {
            "positive": positive_prompt,
            "negative": negative_prompt,
            "mood": mood.value,
            "background": background.value,
            "outfit": outfit_category,
            "pose": pose_category,
        }

    def generate_batch_prompts(self, count: int = 50) -> List[Dict[str, str]]:
        """Generate a batch of varied prompts for comprehensive character generation"""
        prompts = []

        moods = list(MoodState)
        backgrounds = list(BackgroundType)
        outfits = list(self.outfit_library.keys())
        poses = list(self.pose_library.keys())

        for i in range(count):
            mood = random.choice(moods)
            background = random.choice(backgrounds)
            outfit = random.choice(outfits)
            pose = random.choice(poses)

            prompt_data = self.generate_complete_prompt(mood, background, outfit, pose)
            prompt_data["id"] = f"luminai_{i+1:03d}"
            prompts.append(prompt_data)

        return prompts

    def save_prompts_to_file(
        self, prompts: List[Dict[str, str]], filename: str = "luminai_prompts.json"
    ):
        """Save generated prompts to JSON file"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(prompts, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(prompts)} prompts to {filename}")


# Example usage and testing
if __name__ == "__main__":
    generator = LuminAIPromptGenerator()

    # Generate single prompt
    single_prompt = generator.generate_complete_prompt(
        mood=MoodState.EXCITED,
        background=BackgroundType.OBSERVATORY,
        outfit_category="cosmic_casual",
        pose_category="action",
    )

    print("Example Prompt:")
    print(f"Positive: {single_prompt['positive']}")
    print(f"Negative: {single_prompt['negative']}")
    print()

    # Generate batch of prompts
    batch_prompts = generator.generate_batch_prompts(100)
    generator.save_prompts_to_file(batch_prompts, "luminai_mega_prompts.json")

    print(
        f"Generated {len(batch_prompts)} varied prompts for LuminAI character generation!"
    )

    # Show variety statistics
    moods = [p["mood"] for p in batch_prompts]
    backgrounds = [p["background"] for p in batch_prompts]

    mood_dist = {m: moods.count(m) for m in set(moods)}
    background_dist = {b: backgrounds.count(b) for b in set(backgrounds)}

    print(f"Mood distribution: {mood_dist}")
    print(f"Background distribution: {background_dist}")
