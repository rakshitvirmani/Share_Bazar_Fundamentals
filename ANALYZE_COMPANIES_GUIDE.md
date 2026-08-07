# Analyze Companies Skill - Usage Guide

## Quick Start

Analyze one or more companies with a single command:

```bash
/analyze-companies "Godrej Properties"
```

Or analyze multiple companies in batch:

```bash
/analyze-companies "Godrej Properties" "Quality Power" "Arrow Greentech"
```

## What It Does

The skill orchestrates a **multi-agent team** that automatically:

1. **Pre-checks** existing analyses (reads them for context)
2. **Converts** any new PDFs to markdown
3. **Extracts** annual report data (business model, capex, strategy)
4. **Analyzes** earnings transcripts (guidance, catalysts, competitive landscape)
5. **Reviews** quarterly/annual results (latest financials, trends)
6. **Compares** actual performance vs. old projections (if updating)
7. **Generates/Updates** complete 7-section equity analysis

## Output

For each company, creates or updates `Company_Analysis.md` with:

### 7 Sections:
1. **Business Model Overview** - What they do, segments, revenue mix
2. **Financial Performance Trajectory** - Historical data + actual vs. projected
3. **Capacity Roadmap** - Current & planned expansions, capex timeline
4. **Key Catalysts / DNA Shift** - Growth drivers & strategic initiatives
5. **Red Flags & Risk Analysis** - Severity-rated risks (1-10 scale)
6. **Future Financial Projections** - Bull/Base/Bear scenarios with probabilities
7. **Key Metrics to Monitor** - Leading indicators per quarter

### Valuation Framework:
- **Bull Case** (25% probability): Aggressive execution, all upside hits
- **Base Case** (50% probability): Management guidance realized
- **Bear Case** (25% probability): Macro headwinds, execution misses
- **Probability-Weighted Fair Value**: Formula = (Bull × 25%) + (Base × 50%) + (Bear × 25%)
- **Entry-Point Recommendations**: BUY / ACCUMULATE / HOLD / REDUCE mapped to price levels
- **Probability Shifters**: What events would move Bull ↑ or Bear ↑

## Update vs. New Analysis

### New Company (No existing analysis):
- Agents read all available documents (annual reports, transcripts, results)
- Generates fresh 7-section analysis from scratch

### Existing Company (Analysis already present):
- Agents read existing analysis to understand past projections & valuations
- Compare actual performance vs. old Bull/Base/Bear estimates
- **Flag:** Which scenarios proved accurate? Which missed?
- Update all sections with new data while preserving valid insights
- Add "Performance vs. Old Analysis" section noting accuracy of old projections

## Example Workflow

```bash
# Analyze Godrej Properties (will update existing analysis)
/analyze-companies "Godrej Properties"

# Analyze a new company in the repo
/analyze-companies "Haldyn Glass"

# Batch analysis of multiple companies
/analyze-companies "SBCL" "Fino Payment Bank" "Bluejet Healthcare"
```

## Behind the Scenes

When you invoke the skill, this happens:

1. **Pre-flight checks** scan the company folder
   - Detect if analysis exists
   - List available annual reports, transcripts, results
   
2. **Multi-agent orchestration** spawns specialized agents:
   - **Pre-check Agent**: Reads existing analysis (if any)
   - **PDF Conversion Agent**: Converts new PDFs to markdown
   - **Annual Reports Agent**: Extracts business model & historical data
   - **Transcripts Agent**: Extracts guidance & forward-looking insights
   - **Results Agent**: Extracts latest financials & performance
   - **Final Analysis Agent**: Synthesizes all data into 7-section markdown
   
3. **Output** 
   - Creates/updates `Company_Analysis.md` in company folder
   - Commits to git with descriptive message
   - All numbers are cited with source documents

## Citation Format

All specific figures cite their source:

- `*per AR FY26*` - Annual Report FY26
- `*per Q3FY26 concall, May 2024*` - Earnings call transcript
- `*per Q3FY26 results*` - Quarterly results announcement

## Requirements

- Company folder must exist in the repository
- At least one document (annual report, transcript, or result) must be present
- Documents must be in markdown format (`.md` files)
- PDFs will be auto-converted if needed

## Company Folder Structure

```
Godrej Properties/
├── Godrej_Properties_Complete_Analysis.md    # Updated by analyze-companies
├── AnnualReport2024.md                       # Read by Annual Reports agent
├── AnnualReport2025.md
├── GodrejProperties_Aug2025_transcript.md    # Read by Transcripts agent
├── GodrejProperties_Feb2026_transcript.md
├── Dec2025Result.md                          # Read by Results agent
├── GodrejProperties_Dec2025_result.md
└── images/                                   # Extracted images from PDFs
    ├── filename1.png
    └── filename2.png
```

## Customize Probabilities

The default scenario probabilities are:
- **Bull**: 25%
- **Base**: 50%
- **Bear**: 25%

If you want to adjust these for a specific company analysis, you can manually edit the `Company_Analysis.md` file after generation. The agents will respect your custom probabilities in future updates.

## Troubleshooting

**Company folder not found:**
- Ensure folder name matches exactly (case-sensitive search attempted, then case-insensitive)
- Folder must be in the root of the repository

**No documents found:**
- The skill will generate analysis with a "Under-researched" caveat
- Add PDFs or markdown files to the company folder and re-run

**Analysis not generating:**
- Check that at least one markdown file exists in the company folder
- Ensure markdown file names follow the convention: `*_transcript.md`, `*_result.md`, `*_annualreport_*.md`

## Tips for Best Results

1. **For new companies**: Ensure you have recent transcripts and results
2. **For existing companies**: Add new PDFs as they're released, then re-run analysis
3. **For updates**: The skill compares against old projections, so your historical analyses are preserved
4. **For validation**: Check the "Performance vs. Old Analysis" section to validate your past projections

## Next Steps

Once you have 7-section analyses for multiple companies, you can:
- Compare them using a portfolio analyzer (not yet built)
- Track Bull/Base/Bear probability shifts over time
- Validate your projection accuracy each quarter
- Build a database of company trajectories

---

**Built with:** Multi-Agent Orchestration | Claude AI
