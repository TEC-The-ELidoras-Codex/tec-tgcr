"""
Blender headless pipeline: import a GLB, add a simple idle animation (breathing sway), export GLB.
Run with Blender (headless):
  blender -b -P scripts/blender_headless_idle.py -- --input path/to/input.glb --output ai-workflow/output/lumina_idle.glb
"""
import argparse
import math
import sys

try:
    import bpy  # type: ignore
except Exception:
    print("This script must be run inside Blender (bpy unavailable)")
    sys.exit(1)


def parse_args():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1 :]
    else:
        argv = []
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--frames", type=int, default=120)
    p.add_argument("--fps", type=int, default=30)
    return p.parse_args(argv)


def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def import_glb(path):
    bpy.ops.import_scene.gltf(filepath=path)
    # return the root collection
    return bpy.context.scene.collection


def ensure_action(obj_name: str):
    # ensure an action exists on the first armature or object with animation data
    obj = bpy.data.objects.get(obj_name)
    if not obj:
        return None
    if not obj.animation_data:
        obj.animation_data_create()
    if not obj.animation_data.action:
        obj.animation_data.action = bpy.data.actions.new(name=f"{obj.name}_idle")
    return obj.animation_data.action


def add_idle_animation(frames=120, fps=30):
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = frames
    scene.render.fps = fps

    # Find a likely root object (first mesh or armature)
    candidates = [o for o in bpy.context.scene.objects if o.type in {"MESH", "ARMATURE"}]
    if not candidates:
        print("No mesh/armature found; skipping animation")
        return
    root = candidates[0]

    # Simple breathing: scale on Z with a gentle sine; slight sway on X rotation
    root.keyframe_insert(data_path="scale", frame=1, index=-1)
    root.keyframe_insert(data_path="rotation_euler", frame=1, index=-1)

    for f in range(1, frames + 1, max(1, frames // 30)):
        t = f / fps
        breath = 1.0 + 0.01 * math.sin(2 * math.pi * t / 3.0)
        sway = 0.02 * math.sin(2 * math.pi * t / 4.0)
        root.scale = (1.0, 1.0, breath)
        root.rotation_euler[0] = sway
        root.keyframe_insert(data_path="scale", frame=f, index=-1)
        root.keyframe_insert(data_path="rotation_euler", frame=f, index=-1)

    # Set interpolation to SINE for smoothness
    if root.animation_data and root.animation_data.action:
        for fcurve in root.animation_data.action.fcurves:
            for kp in fcurve.keyframe_points:
                kp.interpolation = 'SINE'


def export_glb(path):
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', export_animations=True)


def main():
    args = parse_args()
    clear_scene()
    import_glb(args.input)
    add_idle_animation(frames=args.frames, fps=args.fps)
    export_glb(args.output)
    print("Exported:", args.output)


if __name__ == "__main__":
    main()
