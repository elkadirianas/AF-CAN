# ⚽ AFCON Data Lakehouse & Analytics


## 📖 Project Overview

This project is an end-to-end **Data Engineering & Analytics** solution built to analyze the **African Cup of Nations (AFCON)**.

Moving beyond simple scoreboards, this project implements a **Lakehouse Architecture** on Azure Databricks to process granular event data (passes, shots, fouls, pressure). It features a "Time-Travel" ingestion strategy that simulates the tournament unfolding phase by phase (Group Stage → Knockouts → Final), transforming raw JSON-derived data into advanced tactical KPIs like **Expected Goals (xG)**, **Field Tilt**, and **Player Impact Scores**.


###  how to run the project ? 
This pipeline is designed to be user-friendly and simulates the real-time progression of the tournament.

Import the Pipeline: Clone or upload the files from the Pipeline/ folder into your Databricks Workspace.

Execute the Orchestrator: Open the notebook named 00_run_pipeline_end_to_end.

Simulate Tournament Progress: Simply run this notebook.

Logic: The pipeline automatically detects the current state and ingests the next specific phase (e.g., if Group Stage is done, it loads Round of 16).

View Results: Once the run is complete, navigate to the Databricks Dashboard to see the visuals and KPIs update instantly with the newly ingested data.

Tip: Run it consecutively to simulate the advancement from the opening game to the Final.




## 🏗 Architecture & Methodology

The project follows the **Medallion Architecture** (Bronze, Silver, Gold) to ensure data quality and scalability.

### 1. Data Ingestion (Bronze Layer)
* **Source:** StatsBomb Open Data.
* **Strategy:** Data is ingested incrementally by tournament phase.
* **Format:** Raw CSVs stored in Delta Lake tables.

### 2. Transformation (Silver Layer)
* **Cleaning:** Schema enforcement and type casting.
* **Spatial Parsing:** Complex parsing of player location strings into distinct `X, Y` coordinates for spatial analysis.
* **Deduplication:** Implementation of `Delta Merge` strategies to handle re-runs and duplicates idempotently.

### 3. Business Logic (Gold Layer)
* **Aggregations:** Calculation of advanced metrics.
* **KPIs:**
    * **Field Tilt:** Dominance in the final third.
    * **xG Efficiency:** Goals vs. Expected Goals.
    * **Defensive Intensity:** Pressure events vs. Fouls committed.

---

## 📂 Repository Structure

```text
.
├── DATA/                     # Processed CSVs split by Tournament Phase
│   ├── 1_group_stage_*.csv   # Matches and Events for Group Stage
│   ├── 2_round_of_16_*.csv   # Matches and Events for Round of 16
│   ├── ...                   # Quarter-finals, Semi-finals, 3rd Place
│   └── 6_final_*.csv         # Grand Final data
│
├── Pipeline/                 # Databricks / Spark Notebooks
│   ├── 00_RUN_PIPELINE...    # Orchestrator notebook
│   ├── 01_ingestion...       # Bronze Layer logic
│   ├── 02_silver...          # Silver Layer (Cleaning & Spatial Parsing)
│   └── 03_gold_kpis.ipynb    # Gold Layer (Aggregations & Modeling)
│
├── Splitting_process/        # Pre-processing scripts
│   ├── afcon_events.csv      # Original raw bulk data
│   ├── afcon_matches.csv     # Original raw bulk matches
│   └── splitter.py           # Python script to segregate data by phase
│
└── visuals/                  # Dashboard screenshots and assets


