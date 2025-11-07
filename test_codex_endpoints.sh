#!/bin/bash
# Test script for CODEX API endpoints (WordPress REST API)
# Run this after deploying to elidorascodex.com

set -e

DOMAIN="${1:-elidorascodex.com}"
PROTOCOL="https"
BASE_URL="$PROTOCOL://$DOMAIN/wp-json/tec-tgcr/v1"

echo "🧪 Testing CODEX API Endpoints"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Domain: $DOMAIN"
echo "Base URL: $BASE_URL"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

test_endpoint() {
    local name="$1"
    local method="$2"
    local endpoint="$3"
    local data="$4"
    
    echo -n "Testing: $name ... "
    
    if [ "$method" = "GET" ]; then
        response=$(curl -s -w "\n%{http_code}" "$BASE_URL$endpoint")
    else
        response=$(curl -s -X POST -w "\n%{http_code}" \
            -H "Content-Type: application/json" \
            -d "$data" \
            "$BASE_URL$endpoint")
    fi
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" = "200" ]; then
        echo -e "${GREEN}✓ 200 OK${NC}"
        echo "  Response preview:"
        echo "$body" | jq '.' 2>/dev/null | head -n5
        echo ""
        return 0
    else
        echo -e "${RED}✗ HTTP $http_code${NC}"
        echo "  Response: $body"
        echo ""
        return 1
    fi
}

# Run tests
echo ""
echo "📍 CODEX Knowledge Endpoints"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
test_endpoint "Health Check" "GET" "/health"
test_endpoint "List Cards" "GET" "/cards"
test_endpoint "List Cards (Search)" "GET" "/cards?search=time"
test_endpoint "Get Card: Chronosphere" "GET" "/cards/codex_chronosphere"
test_endpoint "Map Question" "POST" "/map-question" '{"question":"How does time work?"}'
test_endpoint "Get Manifest" "GET" "/manifest"
test_endpoint "Quick Start" "GET" "/quick-start"

echo ""
echo "📍 Legacy TEC Endpoints"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
test_endpoint "TEC Ping" "GET" "/ping"
test_endpoint "TEC Citation" "GET" "/citation?persona=luminai"
test_endpoint "TEC Debug" "GET" "/debug"

echo ""
echo "✅ All endpoint tests complete!"
echo ""
echo "📋 Next Steps:"
echo "1. If all tests passed ✓, the API is ready for ChatGPT integration"
echo "2. Copy the OpenAPI spec to ChatGPT GPT Actions:"
echo "   - File: config/gpt-actions-research.json"
echo "3. Test ChatGPT's ability to retrieve CODEX knowledge"
