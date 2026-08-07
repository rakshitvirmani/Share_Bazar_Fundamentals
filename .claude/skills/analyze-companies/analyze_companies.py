#!/usr/bin/env python3
"""
Multi-agent equity research analyzer.
Orchestrates specialized agents to analyze companies and generate/update 7-section analysis.
"""

import os
import sys
from pathlib import Path

def main():
    """Main entry point for analyze-companies skill."""

    # Parse input - company names from arguments
    companies = sys.argv[1:] if len(sys.argv) > 1 else []

    if not companies:
        print("Usage: analyze_companies.py 'Company1' 'Company2' ...")
        print("\nExample: analyze_companies.py 'Godrej Properties' 'Quality Power'")
        sys.exit(1)

    base_dir = Path("/Users/rvirmani/Documents/Projects/Share_Bazar_Fundamentals")
    os.chdir(base_dir)

    print(f"\n{'='*60}")
    print(f"EQUITY RESEARCH ANALYZER - Multi-Agent Mode")
    print(f"{'='*60}")
    print(f"\nAnalyzing {len(companies)} company/companies:")
    for c in companies:
        print(f"  • {c}")
    print(f"\n{'='*60}\n")

    # For each company, initiate analysis workflow
    for company_name in companies:
        analyze_single_company(base_dir, company_name)

    print(f"\n{'='*60}")
    print(f"Analysis Complete")
    print(f"{'='*60}\n")

def analyze_single_company(base_dir: Path, company_name: str):
    """
    Orchestrate analysis for a single company.
    This function will be called by Claude Code which will spawn agents.
    """

    # Normalize company name to match folder naming
    company_path = find_company_folder(base_dir, company_name)

    if not company_path:
        print(f"✗ Company folder not found: {company_name}")
        return

    print(f"\n📊 Analyzing: {company_path.name}")
    print(f"   Path: {company_path}")

    # Check if analysis exists
    analysis_file = find_analysis_file(company_path)

    if analysis_file:
        print(f"   ✓ Existing analysis found: {analysis_file.name}")
        print(f"     → Will update with new data and compare performance")
    else:
        print(f"   → Generating new analysis from scratch")

    # List available documents
    documents = list_available_documents(company_path)
    print(f"\n   Available documents:")
    if documents['annual_reports']:
        print(f"     • Annual Reports: {len(documents['annual_reports'])}")
        for f in documents['annual_reports'][:2]:
            print(f"       - {f.name}")
    if documents['transcripts']:
        print(f"     • Transcripts: {len(documents['transcripts'])}")
        for f in documents['transcripts'][:2]:
            print(f"       - {f.name}")
    if documents['results']:
        print(f"     • Results: {len(documents['results'])}")
        for f in documents['results'][:2]:
            print(f"       - {f.name}")

    print(f"\n   → Launching analysis agents...")
    print(f"     [Pre-check] → [PDF Convert] → [Annual Reports]")
    print(f"     [Transcripts] → [Results] → [Final Analysis]")
    print(f"\n   ⟳ Analysis in progress... (check Claude Code for agent output)")

def find_company_folder(base_dir: Path, company_name: str) -> Path | None:
    """Find company folder by name (case-insensitive, partial match)."""

    # Direct match first
    direct_path = base_dir / company_name
    if direct_path.is_dir():
        return direct_path

    # Case-insensitive search
    company_lower = company_name.lower().replace(" ", "")
    for folder in base_dir.iterdir():
        if not folder.is_dir() or folder.name.startswith('.'):
            continue
        if folder.name.lower().replace(" ", "") == company_lower:
            return folder

    # Partial match
    for folder in base_dir.iterdir():
        if not folder.is_dir() or folder.name.startswith('.'):
            continue
        if company_lower in folder.name.lower().replace(" ", ""):
            return folder

    return None

def find_analysis_file(company_path: Path) -> Path | None:
    """Find existing analysis markdown file."""

    for pattern in ['*Analysis.md', '*analysis.md', '*_Analysis.md']:
        matches = list(company_path.glob(pattern))
        if matches:
            return matches[0]

    return None

def list_available_documents(company_path: Path) -> dict:
    """List available markdown documents by type."""

    annual_reports = []
    transcripts = []
    results = []

    for md_file in company_path.glob("*.md"):
        name_lower = md_file.name.lower()

        # Skip analysis files
        if 'analysis' in name_lower:
            continue

        if 'annualreport' in name_lower or 'annual' in name_lower:
            annual_reports.append(md_file)
        elif 'transcript' in name_lower:
            transcripts.append(md_file)
        elif 'result' in name_lower:
            results.append(md_file)

    return {
        'annual_reports': sorted(annual_reports),
        'transcripts': sorted(transcripts),
        'results': sorted(results)
    }

if __name__ == '__main__':
    main()
