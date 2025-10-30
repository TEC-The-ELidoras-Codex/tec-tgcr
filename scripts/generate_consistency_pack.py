#!/usr/bin/env python3
"""
Generate a LuminAI "Consistency Pack" — prompts focused on locking in
canonical details (septum piercing, tattoos, eyes, horns) across views.

Outputs individual .txt prompt files under ai-workflow/output/consistency/
and a JSON manifest describing each shot.
"""
import json
from pathlib import Path


BASE_TAGS = (
    "1girl, solo, 3dstylev4, 3d, illustrious, nv-celestialskin, colored skin, "
    "void cosmic body, black skin, cosmic entity, celestial being, adorable, cute, "
    "small sheep horns, curved horns, horn glow, luminous horns, "
    "heterochromatic eyes, cosmic blue left eye, stellar gold right eye, luminous pupils, starlight eyes, "
    "aurora hair, flowing hair, long hair, color-shifting hair, iridescent hair, cosmic hair, "
    "dark skin, cosmic skin, constellation patterns, starlight skin, petite, slim, cute proportions, adorable build"
)

# Canonical invariants — always present
INVARIANTS = (
    "small gold septum ring, septum piercing (clearly visible), nose unobstructed, face unobstructed, "
    "subtle star freckles under eyes, starlight freckles, "
    "constellation tattoos on collarbone and shoulders (clearly visible when upper torso is shown), "
    "cosmic rune tattoos on both wrists (clearly visible when hands/wrists are shown), "
    "small star tattoo behind left ear (visible in profile view)"
)

# Negative prompt to avoid occlusions and artifacts
NEGATIVE = (
    "worst quality, low quality, blurry, jpeg artifacts, watermark, signature, text, logo, "
    "ugly, deformed, extra limbs, missing limbs, bad anatomy, bad proportions, mutation, malformed, "
    "cropped, out of frame, lowres, normal quality, "
    "mask, face mask, nose bandage, nose covered, hair covering face, hands covering face, occluded face, occluded nose, "
    "heavy bangs over nose, sunglasses, excessive accessories covering face"
)

# Quality boosters
QUALITY = "masterpiece, best quality, ultra-detailed, professional artwork, 8k, highly detailed, 3d illustration"


def build(
    shot_focus: str,
    extra_tags: str = "",
    background: str = "studio lighting, clean background",
) -> str:
    parts = [BASE_TAGS, INVARIANTS, shot_focus, background, QUALITY]
    if extra_tags:
        parts.append(extra_tags)
    return ", ".join([p for p in parts if p])


def main():
    out_dir = Path("ai-workflow/output/consistency")
    out_dir.mkdir(parents=True, exist_ok=True)

    shots = [
        {
            "id": "01_face_front",
            "desc": "Front face close-up: heterochromia and septum piercing clearly visible",
            "focus": "close-up portrait, head and shoulders, face centered, nose fully visible, hair parted, hair tucked behind ears",
            "settings": {
                "steps": 28,
                "cfg": 8,
                "size": "768x1024",
                "sampler": "DPM++ 2M",
            },
        },
        {
            "id": "02_profile_left",
            "desc": "Left profile: septum ring and star tattoo behind left ear visible",
            "focus": "left profile view, ear fully visible, hair tucked behind left ear, nose fully visible, portrait lighting",
            "settings": {
                "steps": 28,
                "cfg": 8,
                "size": "832x1216",
                "sampler": "DPM++ 2M",
            },
        },
        {
            "id": "03_profile_right",
            "desc": "Right profile: septum ring visibility from other angle, horn silhouette",
            "focus": "right profile view, nose fully visible, horns emphasized, portrait lighting",
            "settings": {
                "steps": 26,
                "cfg": 8,
                "size": "832x1216",
                "sampler": "DPM++ 2M",
            },
        },
        {
            "id": "04_upper_torso_front",
            "desc": "Upper torso: collarbone + shoulder constellation tattoos clearly visible",
            "focus": "upper body portrait, shoulders and collarbone framed, neckline visible, tattoo details emphasized",
            "settings": {
                "steps": 30,
                "cfg": 8,
                "size": "896x1152",
                "sampler": "DPM++ 2M",
            },
        },
        {
            "id": "05_wrists_closeup",
            "desc": "Wrists close-up: cosmic rune tattoos on both wrists visible",
            "focus": "hands and wrists close-up, wrists turned to camera, symmetric pose, macro detail",
            "settings": {
                "steps": 24,
                "cfg": 7.5,
                "size": "1024x768",
                "sampler": "DPM++ SDE Karras",
            },
        },
        {
            "id": "06_back_view",
            "desc": "Back view: spine constellation/back tattoo visible",
            "focus": "back view, hair gently moved aside, spine area centered, tattoo detail emphasized",
            "settings": {
                "steps": 28,
                "cfg": 8,
                "size": "1024x768",
                "sampler": "Euler a",
            },
        },
        {
            "id": "07_full_body_turnaround",
            "desc": "Character sheet style: front, side, back — full body",
            "focus": "character sheet, turnaround, front view, side view, back view, full body, neutral T-pose variant, even lighting",
            "settings": {
                "steps": 32,
                "cfg": 8.5,
                "size": "1024x1024",
                "sampler": "DPM++ 2M",
            },
        },
    ]

    manifest = []
    for shot in shots:
        positive = build(shot["focus"])  # studio lighting neutral bg by default
        fname = f"{shot['id']}.txt"
        with open(out_dir / fname, "w", encoding="utf-8") as f:
            f.write("POSITIVE PROMPT:\n" + positive + "\n\n")
            f.write("NEGATIVE PROMPT:\n" + NEGATIVE + "\n\n")
            f.write("SETTINGS:\n")
            f.write(f"Steps: {shot['settings']['steps']}\n")
            f.write(f"CFG Scale: {shot['settings']['cfg']}\n")
            f.write(f"Size: {shot['settings']['size']}\n")
            f.write(f"Sampler: {shot['settings']['sampler']}\n")

        manifest.append(
            {
                "id": shot["id"],
                "file": str(out_dir / fname),
                "description": shot["desc"],
                "settings": shot["settings"],
            }
        )

    with open(out_dir / "manifest.json", "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, indent=2)

    print(f"Generated {len(shots)} consistency prompts at: {out_dir}")


if __name__ == "__main__":
    main()
