# Spotify-Style Growth Analytics Project

## Overview
This project simulates a performance marketing and growth analytics workflow similar to what a Data Scientist would do at Spotify. It analyzes marketing channel performance and measures incremental lift from increased ad spend using experimentation techniques.

## Data
Synthetic data was generated to mimic real-world marketing behavior:
- 20,000 users across multiple countries
- Paid marketing channels (Google Search, Meta, TikTok, Apple Search Ads, YouTube)
- Conversion and revenue data
- Geo-based experiment with test and control regions

## Tools Used
- Python (NumPy, Pandas, Matplotlib)
- SQLite
- SQL
- Jupyter Notebook

## Analysis

### Channel Performance
Marketing channels were evaluated using:
- Conversion rate
- Spend
- Revenue
- Cost per Acquisition (CAC)

Channels were ranked by efficiency to identify where marketing spend performed best.

### Incrementality Experiment
A geo-based experiment was analyzed using a Difference-in-Differences approach.

**Results:**
- Test regions increased conversion rate from **8.18% → 8.86%**
- Control regions decreased from **8.05% → 7.68%**
- **Incremental lift: +1.05 percentage points**

This indicates that increased performance marketing spend drove meaningful incremental growth beyond baseline trends.

## Files
- `generate_data.py` – Generates synthetic marketing data
- `load_to_sqlite.py` – Loads data into SQLite
- `analysis.ipynb` – Analysis and experimentation
- `marketing.db` – SQLite database
- `cac_by_channel.png` – Channel efficiency visualization
- `experiment_pre_post.png` – Experiment results visualization
