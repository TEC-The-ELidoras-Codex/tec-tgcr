"""
Blender rigging helper for Lumina GLB

Usage (from Windows PowerShell):
  blender -b -P scripts/blender/rig_lumina.py -- \
    --glb "C:/path/to/Lumina.glb" \
    --output "C:/path/to/output/lumina_rigged" \
    --no_join

Notes:
- Must be executed inside Blender's Python (bpy is required).
- Requires the Rigify add-on (script enables it automatically).
- Produces: .blend, rigged .glb, and .fbx in the output directory.

This script attempts a pragmatic auto-fit of a Human metarig to the
imported character by aligning the metarig to the mesh bounding box.
You should fine-tune the metarig in Blender if needed, then rerun
parenting/rig generation.
"""

import os
import sys
import argparse

try:
    import bpy  # type: ignore
except Exception:  # pragma: no cover
    print("This script must be run from Blender (bpy not found).", file=sys.stderr)
    sys.exit(2)


def parse_args():
    # Blender passes args as: blender ... -- python_script.py -- <args>
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1 :]
    else:
        argv = []

    parser = argparse.ArgumentParser(description="Auto-rig a GLB with Rigify")
    parser.add_argument("--glb", required=True, help="Path to input .glb file")
    parser.add_argument(
        "--output",
        required=False,
        default=None,
        help="Output path prefix (without extension). Defaults next to input as *_rigged",
    )
    parser.add_argument(
        "--no_join",
        action="store_true",
        help="Do not join imported mesh objects before rigging",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="Uniform scale to apply to imported mesh (default 1.0)",
    )
    return parser.parse_args(argv)


def enable_rigify():
    prefs = bpy.context.preferences
    addons = prefs.addons
    if "rigify" not in addons:
        bpy.ops.preferences.addon_enable(module="rigify")


def import_glb(path: str):
    assert os.path.isfile(path), f"GLB not found: {path}"
    bpy.ops.import_scene.gltf(filepath=path)
    imported = [obj for obj in bpy.context.selected_objects]
    return imported


def select_only(objs):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    if objs:
        bpy.context.view_layer.objects.active = objs[0]


def objects_by_type(objects, type_name):
    return [o for o in objects if o.type == type_name]


def join_meshes(mesh_objs):
    if not mesh_objs:
        return None
    select_only(mesh_objs)
    if len(mesh_objs) > 1:
        bpy.ops.object.join()
    return bpy.context.view_layer.objects.active


def apply_object_transforms(obj):
    select_only([obj])
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


def add_human_metarig():
    # Add human metarig at origin
    bpy.ops.object.armature_human_metarig_add()
    rig = bpy.context.view_layer.objects.active
    rig.name = "Lumina_Metarig"
    return rig


def fit_rig_to_mesh_bbox(rig, mesh_obj):
    # Rough fit: scale/position metarig to mesh bounding box
    import mathutils  # type: ignore

    # Compute mesh world-space bounds
    bbox_corners = [
        mesh_obj.matrix_world @ mathutils.Vector(corner)
        for corner in mesh_obj.bound_box
    ]
    xs = [v.x for v in bbox_corners]
    ys = [v.y for v in bbox_corners]
    zs = [v.z for v in bbox_corners]
    min_v = mathutils.Vector((min(xs), min(ys), min(zs)))
    max_v = mathutils.Vector((max(xs), max(ys), max(zs)))
    size = max_v - min_v
    center = (min_v + max_v) / 2.0

    # Place rig at center, scale to height
    rig.location = center
    height = max(size.z, 1e-3)
    # Human metarig default height approx ~1.7m; compute scale factor
    scale_factor = height / 1.7
    rig.scale = (scale_factor, scale_factor, scale_factor)

    # Ensure transforms are applied to the rig object to avoid parenting issues
    apply_object_transforms(rig)


def parent_with_automatic_weights(mesh_obj, armature_obj):
    # Select mesh first, then armature; set parent with automatic weights
    select_only([mesh_obj, armature_obj])
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.parent_set(type="ARMATURE_AUTO")


def generate_rigify(armature_obj):
    # Assumes armature_obj is a metarig with Rigify bones
    select_only([armature_obj])
    bpy.ops.pose.rigify_generate()
    # The generated rig is usually named "rig"
    rig = bpy.data.objects.get("rig")
    return rig


def save_and_export(output_prefix: str):
    out_dir = os.path.dirname(output_prefix)
    os.makedirs(out_dir, exist_ok=True)

    # Save .blend
    blend_path = f"{output_prefix}.blend"
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)

    # Export GLB
    glb_path = f"{output_prefix}.glb"
    bpy.ops.export_scene.gltf(
        filepath=glb_path,
        export_format="GLB",
        export_yup=True,
        export_apply=True,
        export_animations=True,
        use_selection=False,
    )

    # Export FBX
    fbx_path = f"{output_prefix}.fbx"
    bpy.ops.export_scene.fbx(
        filepath=fbx_path, use_selection=False, apply_scale_options="FBX_SCALE_ALL"
    )

    return blend_path, glb_path, fbx_path


def main():
    args = parse_args()
    glb_path = os.path.abspath(args.glb)
    if args.output:
        output_prefix = os.path.abspath(args.output)
    else:
        base, ext = os.path.splitext(glb_path)
        output_prefix = base + "_rigged"

    print(f"[LuminaRig] Importing GLB: {glb_path}")
    imported_objs = import_glb(glb_path)

    # Optionally scale everything
    if abs(args.scale - 1.0) > 1e-6:
        for o in imported_objs:
            o.scale = (args.scale, args.scale, args.scale)
            apply_object_transforms(o)

    mesh_objs = objects_by_type(imported_objs, "MESH")
    if not mesh_objs:
        raise RuntimeError("No mesh objects found in imported GLB.")

    if args.no_join:
        # Pick the largest mesh as primary for bbox fit
        mesh_primary = max(
            mesh_objs, key=lambda m: sum((m.dimensions[i] for i in range(3)))
        )
    else:
        mesh_primary = join_meshes(mesh_objs)

    # Ensure object mode
    if bpy.ops.object.mode_set.poll():
        try:
            bpy.ops.object.mode_set(mode="OBJECT")
        except Exception:
            pass

    apply_object_transforms(mesh_primary)

    print("[LuminaRig] Enabling Rigify...")
    enable_rigify()

    print("[LuminaRig] Adding human metarig...")
    metarig = add_human_metarig()

    print("[LuminaRig] Fitting metarig to mesh bounds...")
    fit_rig_to_mesh_bbox(metarig, mesh_primary)

    print("[LuminaRig] Generating Rigify control rig...")
    control_rig = generate_rigify(metarig)
    if control_rig:
        print(
            "[LuminaRig] Parenting mesh to generated control rig with automatic weights..."
        )
        parent_with_automatic_weights(mesh_primary, control_rig)
    else:
        print(
            "[LuminaRig] Warning: Generated rig not found; parenting to metarig as fallback."
        )
        parent_with_automatic_weights(mesh_primary, metarig)

    print("[LuminaRig] Saving & exporting rigged model...")
    blend, glb, fbx = save_and_export(output_prefix)
    print(
        f"[LuminaRig] Saved: {blend}\n[ LuminaRig] Exported GLB: {glb}\n[ LuminaRig] Exported FBX: {fbx}"
    )


if __name__ == "__main__":
    main()
