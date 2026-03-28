# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A personal equity research repository for Indian publicly-listed mid-cap, small-cap and micro-cap stocks. Each company gets its own folder containing:
1. A Markdown analysis file — the primary research document
2. Supporting PDFs — earnings call transcripts, investor presentations, regulatory filings

There is no build system, no code, and no dependencies. This is a document repository managed with Git.

## Repository Structure

```
Share_Bazar_Fundamentals/
└── [Company_Name]/
    ├── [Company]_Analysis.md     # Core research note (see format below)
    └── [MonthYear].pdf           # Earnings transcripts and filings
```

## Analysis Document Format

Each Markdown analysis file follows this structure (in order):

1. **Business Model Overview** — what the company does, key segments, revenue mix
2. **Financial Performance Trajectory** — historical quarterly/annual data in table form
3. **Capacity Roadmap** — current vs. planned capacity, capex timeline
4. **Key Catalysts / DNA Shift** — structural growth drivers specific to this company
5. **Red Flags & Risk Analysis** — risks with severity ratings (X/10 scale)
6. **Future Financial Projections** — FY26E / FY27E / FY28E estimates
7. **Key Metrics to Monitor** — leading indicators and what to track each quarter

## Conventions to Follow When Adding/Updating Analysis

- **Projections use FY suffix**: FY26E, FY27E, FY28E (E = Estimate)
- **Severity ratings**: Red flags are rated on a 1–10 scale (10 = highest risk)
- **Financial units**: State clearly (Cr = Crore INR, unless otherwise noted)
- **Dates on filenames**: Use `Mar2026`, `Q3FY26` style for naming analysis files
- **PDF naming**: Match the earnings call month/quarter — `Q3FY26_Concall.pdf`, `Nov2025.pdf`

## Working with PDFs to Generate Analysis

When PDFs are present in a company's folder, read them all before writing or updating the analysis. The PDFs fall into three categories — extract different things from each:

**Annual Reports**

- Revenue breakdown by segment, geography, and product line
- EBITDA, PAT, ROCE, ROE (3–5 year trend)
- Debt levels, working capital cycle, cash flow from operations
- Capex history and stated future capex plans
- Management Discussion & Analysis (MD&A) section for strategic direction
- Key accounting policies or auditor observations worth flagging

**Conference Call / Concall Transcripts**

- Management guidance on revenue, margins, and order book for upcoming quarters
- Commentary on pricing power, demand environment, and competitive landscape
- Any forward guidance on capacity additions or geographic expansion
- Specific numbers cited by management (order book size, utilization %, margin targets)
- Any red flags raised by analysts during Q&A

**Company Announcements / Exchange Filings**

- Regulatory approvals, new orders, plant commissioning updates
- Promoter shareholding changes or pledging activity
- Related-party transactions or board changes worth noting

After reading all PDFs, produce or update the `[Company]_Analysis.md` using the 7-section format. Cite the source document inline when using specific figures (e.g., `*per Q3FY26 concall*`, `*AR FY25*`).

## Adding a New Company

1. Create a folder: `[Company_Name]/`
2. Place all available PDFs into the folder
3. Read every PDF, then create `[Company_Name]_Analysis.md` following the 7-section format
4. Commit with a descriptive message: `"[Company Name] analysis added"` or `"[Company Name] Q3FY26 update"`

## Key Existing Analyses (for reference style)

- **Waaree Energies** — most comprehensive example; covers complex multi-segment business with detailed risk severity ratings
- **DEE Development** — good example of order book tracking and facility utilization metrics
- **Accent Microcell** — good example of capacity expansion roadmap format
