# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A personal equity research repository for publicly-listed companies (primarily Indian mid-cap, small-cap, and micro-cap stocks; also includes select US-listed companies). Each company gets its own folder containing:
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

## Valuation Framework – Probability-Weighted Analysis (Mandatory)

**For EVERY company analysis, Section 6 (Future Financial Projections) MUST include:**

### Fair Value Scenarios with Explicit Probabilities:

Create a table with:
- **Bull Case** (typically 20–30% probability): Aggressive execution, all upside catalysts hit, best-case margins/growth
- **Base Case** (typically 50–60% probability): Management guidance realized, normal execution, aligned with historical track record
- **Bear Case** (typically 15–25% probability): Macro headwinds, execution misses, competitive pressure, margin compression

For each scenario, calculate:
- FY27E PAT (or latest full-year estimate)
- Justified P/E multiple (based on growth rate and risk profile)
- Implied Market Cap & Per-Share Fair Value

### Probability-Weighted Fair Value Calculation:

**Formula:** `(Bull Price × Bull %) + (Base Price × Base %) + (Bear Price × Bear %)`

**Example:**
- Bull: ₹400/share × 25% = ₹100
- Base: ₹292/share × 50% = ₹146
- Bear: ₹216/share × 25% = ₹54
- **Weighted Fair Value = ₹300/share**

### Entry-Point Recommendation Table:

Map current/assumed CMP to actionable recommendations:
- **Below 10% discount to weighted FV**: BUY
- **0–10% discount**: ACCUMULATE
- **0–5% premium**: HOLD
- **Above 5% premium**: REDUCE

Calculate expected return at each price level to weighted fair value.

### Probability Shifters:

Explicitly state what events/metrics would shift probabilities between scenarios:
- **Bull probability ↑** if: [specific catalysts, e.g., "Digital growth >20% YoY", "Margin >11%"]
- **Bear probability ↑** if: [specific headwinds, e.g., "Revenue growth <5%", "Customer loss"]

### FY30+ Terminal Value:

Include long-term fair value (FY30 onwards):
- Calculate FY30E PAT using normalized assumptions
- Apply terminal value multiple (e.g., 15–18x P/E for mature businesses)
- Discount back to present value (optional, for DCF context)

---

**Investment Verdict Template (Section 7):**

1. **Lead with Weighted Fair Value & Entry Recommendations** (keyed to current CMP)
2. **Detail Bull Case** (with 25% probability example): What needs to go right
3. **Detail Base Case** (with 50% probability example): Most likely path
4. **Detail Bear Case** (with 25% probability example): What could go wrong
5. **Clear Rating**: BUY/ACCUMULATE/HOLD/REDUCE (matched to probability-weighted price)

## Working with PDFs to Generate Analysis

### Critical First Step: Convert ALL PDFs to Markdown BEFORE Reading

**WORKFLOW:**
1. **Identify all PDF files** in the company folder
2. **Convert every PDF to Markdown** using the pymupdf4llm tool (via ~/.claude/skills/pdf-to-markdown/.venv/bin/python)
3. **Only then start reading** the markdown files to extract data

**Why this order matters:**
- Ensures all documents are available in text format before analysis begins
- Avoids re-reading the same PDF multiple times
- Enables efficient grep/search across markdown files
- Prevents missing documents due to extraction order
- Allows parallel processing of large PDFs

**Conversion Command Template:**
```bash
~/.claude/skills/pdf-to-markdown/.venv/bin/python ~/.claude/skills/pdf-to-markdown/scripts/pdf_to_md.py "[PDF_PATH]"
```

**For multiple PDFs in a folder, create a batch script** (see past sessions for examples)

---

### Then Read & Extract from Markdown Files

When PDFs are converted to markdown, read them to extract data. The PDFs fall into three categories — extract different things from each:

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
