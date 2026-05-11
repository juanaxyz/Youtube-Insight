# YouTube Insight
## About Dataset
• rank: Position of the YouTube channel based on the number of subscribers
• Youtuber: Name of the YouTube channel
• subscribers: Number of subscribers to the channel
• video views: Total views across all videos on the channel
• category: Category or niche of the channel
• Title: Title of the YouTube channel
• uploads: Total number of videos uploaded on the channel
• Country: Country where the YouTube channel originates
• Abbreviation: Abbreviation of the country
• channel_type: Type of the YouTube channel
• video_views_rank: Ranking of the channel based on total video views
• country_rank: Ranking of the channel based on the number of subscribers within its country
• channel_type_rank: Ranking of the channel based on its type video_views_for_the_last_30_days: Total video views in the last 30 days
• lowest_monthly_earnings: Lowest estimated monthly earnings from the channel
• highest_monthly_earnings: Highest estimated monthly earnings from the channel
• lowest_yearly_earnings: Lowest estimated yearly earnings from the channel
• highest_yearly_earnings: Highest estimated yearly earnings from the channel
• subscribers_for_last_30_days: Number of new subscribers gained in the last 30 days
• created_year: Year when the YouTube channel was created
• created_month: Month when the YouTube channel was created
• created_date: Exact date of the YouTube channel's creation
• Gross tertiary education enrollment (%): Percentage of the population enrolled in tertiary education in the country
• Population: Total population of the country
• Unemployment rate: Unemployment rate in the country
• Urban_population: Percentage of the population living in urban areas
• Latitude: Latitude coordinate of the country's location
• Longitude: Longitude coordinate of the country's location


## Project structure
```
youtube‑insight/
│
├─ data/
│   └─ Global YouTube Statistics.csv   # dataset (provided by you)
│
├─ notebooks/
│   ├─ 01_preprocess.ipynb            # cleaning & feature engineering
│   └─ 02_visualization.ipynb        # 20 insight → PNG figures
│
├─ requirements.txt                  # Python dependencies
├─ AGENTS.md                         # project‑wide instructions for OpenCode
└─ README.md                         # this file
```

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_preprocess.ipynb   # run all cells
jupyter notebook notebooks/02_visualization.ipynb   # run all cells
```
All generated figures will be saved in `notebooks/figures/`.

## What the notebooks do
- **01_preprocess.ipynb** loads the raw CSV, cleans NaNs, converts numeric columns, creates engineered features (average earnings, earnings per view, upload frequency, subscriber‑to‑earnings, CPM, year/month start) and stores the cleaned data as Parquet.
- **02_visualization.ipynb** reads the processed Parquet file and produces 20 static PNG visualizations that answer the insight questions you listed.


