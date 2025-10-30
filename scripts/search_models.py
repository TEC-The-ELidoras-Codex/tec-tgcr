#!/usr/bin/env python3
"""
Quick model search script for LuminAI
"""
import sys

sys.path.insert(0, "src")

from tec_tgcr.integrations.civitai import CivitaiClient


def search_luminai_models():
    client = CivitaiClient()

    print("🔍 Searching for LuminAI-compatible models on Civitai...\n")

    # Search for base models
    search_terms = [
        "Illustrious XL",
        "Nova 3DCG XL",
        "3D celestial",
        "cosmic character",
    ]

    for term in search_terms:
        print(f"📦 Searching: {term}")
        try:
            models = client.search_models(term, limit=3)
            for model in models:
                print(f"   ✨ {model['name']}")
                print(f"   📊 {model['stats']['downloadCount']:,} downloads")
                print(f"   🔗 https://civitai.com/models/{model['id']}")
                print()
        except Exception as e:
            print(f"   ❌ Error: {e}")
        print("-" * 50)


if __name__ == "__main__":
    search_luminai_models()
