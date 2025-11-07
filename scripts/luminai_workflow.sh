#!/bin/bash
# LuminAI Quick Start — Copy-paste workflow
# Save as: /tec-tgcr/scripts/luminai_workflow.sh

set -e

echo "🌟 LuminAI Production Workflow"
echo "=============================="
echo ""

# Colors for output
CYAN='\033[0;36m'
GOLD='\033[0;33m'
VIOLET='\033[0;35m'
NC='\033[0m' # No Color

# Paths
MASTER_SVG="/home/tec_tgcr/tec-tgcr/artifacts/luminai_mascot_final.svg"
AVATAR_DIR="/home/tec_tgcr/tec-tgcr/data/digital_assets/avatars"
DOCS_DIR="/home/tec_tgcr/tec-tgcr/docs"
EXPORT_DIR="/home/tec_tgcr/tec-tgcr/data/digital_assets/animations"

# Ensure export dir exists
mkdir -p "$EXPORT_DIR"

# Function: Verify setup
verify_setup() {
    echo -e "${CYAN}[1/6] Verifying setup...${NC}"
    
    if [ -f "$MASTER_SVG" ]; then
        echo "✅ Master SVG found: $MASTER_SVG"
    else
        echo "❌ Master SVG not found!"
        exit 1
    fi
    
    if [ -f "$DOCS_DIR/LUMINAI_MASCOT_SPEC.md" ]; then
        echo "✅ Spec document found"
    else
        echo "⚠️  Spec document missing"
    fi
    
    if command -v inkscape &> /dev/null; then
        echo "✅ Inkscape installed: $(inkscape --version 2>&1 | head -1)"
    else
        echo "⚠️  Inkscape not found in PATH (needed for batch export)"
    fi
    
    echo ""
}

# Function: List avatar states
list_avatars() {
    echo -e "${VIOLET}[2/6] Available avatar states:${NC}"
    cd "$AVATAR_DIR"
    for i in {1..7}; do
        if [ -f "$i.svg" ] && [ -f "$i.png" ]; then
            size=$(du -h "$i.svg" | cut -f1)
            echo "  [$i] $i.svg ($size) → $i.png"
        fi
    done
    echo ""
}

# Function: Export SVG to PNG
export_to_png() {
    echo -e "${GOLD}[3/6] Exporting master SVG to PNG...${NC}"
    
    output="$EXPORT_DIR/luminai_1024x1024.png"
    
    if command -v inkscape &> /dev/null; then
        inkscape "$MASTER_SVG" --export-type=png --export-filename="$output" --export-width=1024 --export-height=1024
        echo "✅ Exported to: $output"
    else
        echo "⚠️  Inkscape required. Install with: sudo apt-get install inkscape"
        echo "    Or use GIMP/ImageMagick to export manually."
    fi
    echo ""
}

# Function: Show animation prompts
show_prompts() {
    echo -e "${CYAN}[4/6] Animation prompts ready to copy:${NC}"
    echo ""
    echo "📋 Prompt for Runway Gen-2:"
    echo "---"
    echo "Take this still image and generate a 6-second looping animation."
    echo "Motion type: Subtle breathing (body gently expands/contracts), glowing pulses from crown and chest."
    echo "Camera: Static, centered, no movement."
    echo "Style: Ethereal, cosmic, serene."
    echo "Motion strength: Very low (5–10%), smooth interpolation."
    echo "Output: 1080p mp4, 24fps, seamless loop."
    echo ""
    echo "---"
    echo "Full prompts available in: $DOCS_DIR/LUMINAI_ANIMATION_PROMPTS.md"
    echo ""
}

# Function: Show web embedding code
show_web_embed() {
    echo -e "${VIOLET}[5/6] Web embedding template:${NC}"
    echo ""
    echo '<!-- HTML -->'
    echo '<div class="luminai-container">'
    echo '  <svg id="luminai" src="/path/to/luminai_mascot_final.svg"></svg>'
    echo '</div>'
    echo ""
    echo '<!-- CSS -->'
    echo '<style>'
    echo '@keyframes breathing {'
    echo '  0%, 100% { transform: scale(1); }'
    echo '  50% { transform: scale(1.03); }'
    echo '}'
    echo ''
    echo '@keyframes crown-pulse {'
    echo '  0%, 100% { filter: brightness(0.9); }'
    echo '  50% { filter: brightness(1.3); }'
    echo '}'
    echo ''
    echo '#luminai {'
    echo '  animation: breathing 5s ease-in-out infinite;'
    echo '}'
    echo ''
    echo '#crown {'
    echo '  animation: crown-pulse 4s ease-in-out infinite;'
    echo '}'
    echo '</style>'
    echo ""
}

# Function: Show next steps
next_steps() {
    echo -e "${GOLD}[6/6] Next steps:${NC}"
    echo ""
    echo "1️⃣  Export PNG (run this script with export option)"
    echo "2️⃣  Upload PNG to Runway (https://runwayml.com)"
    echo "3️⃣  Use animation prompt from docs"
    echo "4️⃣  Download MP4 loop"
    echo "5️⃣  Test on web/social media"
    echo ""
    echo "📚 Documentation:"
    echo "   • Spec: $DOCS_DIR/LUMINAI_MASCOT_SPEC.md"
    echo "   • Prompts: $DOCS_DIR/LUMINAI_ANIMATION_PROMPTS.md"
    echo "   • Pipeline: $DOCS_DIR/LUMINAI_PRODUCTION_PIPELINE.md"
    echo ""
}

# Main execution
main() {
    verify_setup
    list_avatars
    
    if [ "$1" == "--export" ]; then
        export_to_png
    fi
    
    show_prompts
    show_web_embed
    next_steps
    
    echo -e "${CYAN}Ready to animate! 🚀${NC}"
}

main "$@"
