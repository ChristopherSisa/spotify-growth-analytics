# Spotify-Style Growth Analytics Project

## Overview
This project simulates a performance marketing analytics workflow similar to what a Growth Data Scientist would do at Spotify. Using Python, SQL, and experimentation methods, the project analyzes marketing channel performance and measures incremental impact from increased ad spend.

## Data Generation
Synthetic data was generated to mimic real-world marketing behavior:
- 20,000 users across multiple countries
- Paid media touchpoints (Google Search, Meta, TikTok, Apple Search Ads, YouTube)
- Conversions with associated revenue
- A geo-based experiment with test and control regions

## Tools Used
- Python (NumPy, Pandas, Matplotlib)
- SQLite
- SQL
- Jupyter Notebook

## Analysis Performed

### 1. Channel Performance
Marketing channels were evaluated using:
- Conversion Rate
- Spend
- Revenue
- Cost per Acquisition (CAC)

Channels were ranked by efficiency to identify where marketing spend performed best.

### 2. Experimentation & Incrementality
A geo-based experiment was analyzed using a Difference-in-Differences approach to measure incremental lift from increased performance marketing spend.

**Results:**
- Test regions increased conversion rate from **8.18% → 8.86%**
- Control regions decreased from **8.05% → 7.68%**
- **Incremental lift: +1.05 percentage points**

This indicates that the increased spend drove meaningful incremental growth beyond baseline trends.

## Key Takeaway
Performance marketing investment in test regions resulted in a positive incremental lift in conversions, suggesting efficient spend that could be scaled to similar markets.

## Files
- `generate_data.py` – Generates synthetic marketing data
- `load_to_sqlite.py` – Loads data into SQLite database
- `analysis.ipynb` – Analytics and experiment analysis
- `marketing.db` – SQLite database
- `cac_by_channel.png` – Channel efficiency visualization
- `experiment_pre_post.png` – Experiment results visualization
