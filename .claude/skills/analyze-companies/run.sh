#!/bin/bash

# Analyze Companies Skill - Entry Point
# Orchestrates multi-agent company analysis workflow

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd /Users/rvirmani/Documents/Projects/Share_Bazar_Fundamentals

# Run pre-flight checks with Python utility
if [ $# -eq 0 ]; then
    echo "Usage: analyze-companies 'Company1' 'Company2' ..."
    echo ""
    echo "Example:"
    echo "  analyze-companies 'Godrej Properties' 'Quality Power' 'Arrow Greentech'"
    exit 1
fi

# Run Python pre-flight checks
python3 "$SKILL_DIR/analyze_companies.py" "$@"

# Output coordinator instructions
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "SPAWNING MULTI-AGENT COORDINATOR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Print coordinator instructions
cat "$SKILL_DIR/coordinator.md"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✓ Coordinator instructions loaded above"
echo "✓ Begin orchestration with companies: $@"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
