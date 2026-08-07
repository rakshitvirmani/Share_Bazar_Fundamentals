# Analyze Companies Skill

Multi-agent equity research analyzer that generates comprehensive 7-section company analysis by orchestrating specialized agents.

## Usage

```bash
/analyze-companies "Company1" "Company2" "Company3"
```

Or single company:
```bash
/analyze-companies "Godrej Properties"
```

## Workflow

For each company folder:

1. **Pre-check Agent** → Check if analysis exists, read for context
2. **PDF Conversion Agent** → Convert new PDFs to markdown if needed
3. **Annual Reports Agent** → Extract business model, capex, strategy
4. **Transcripts Agent** → Extract guidance, catalysts, competitive intel
5. **Results Agent** → Extract latest financials, trends
6. **Final Analysis Agent** → Synthesize all data → generate/update 7-section analysis

## Output

- **New companies**: Creates `Company_Analysis.md` with complete 7-section analysis
- **Existing companies**: Updates `Company_Analysis.md` with:
  - New financial data
  - Updated projections (Bull/Base/Bear)
  - Performance vs. old analysis flagged
  - Revised catalysts and risks

## 7-Section Format

1. **Business Model Overview**
2. **Financial Performance Trajectory** (with actual vs. projected)
3. **Capacity Roadmap**
4. **Key Catalysts / DNA Shift**
5. **Red Flags & Risk Analysis**
6. **Future Financial Projections** (Bull/Base/Bear with probabilities)
7. **Key Metrics to Monitor**

Each analysis includes:
- **Probability-weighted fair value** calculation
- **Entry-point recommendations** (BUY/ACCUMULATE/HOLD/REDUCE)
- **Performance tracker** vs. previous projections
- **Probability shifters** (what moves Bull/Base/Bear odds)

## Features

- Handles single or multiple companies in batch
- Generates analysis from scratch or updates existing
- Compares actual performance vs. old projections
- Extracts images from PDFs automatically
- Preserves markdown structure with proper formatting
- Cites sources inline (e.g., *per Q3FY26 concall*)
