"""
YouTube Insights Visualization Script
Generates 20 key insights from YouTube dataset and saves all visualizations as PNG files
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
from datetime import datetime

warnings.filterwarnings("ignore")

# Set style for better-looking plots
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")

# Set random seed for reproducibility
np.random.seed(42)

# Create output directory for saving plots
output_dir = "youtube_insights_output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")

print("=" * 80)
print("YOUTUBE STATISTICS VISUALIZATION")
print("=" * 80)
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Load the dataset
print("Loading dataset...")
file_path = "./data/Global_YouTube_Statistics_Cleaned.csv"

try:
    df = pd.read_csv(file_path, encoding="latin-1")
    print(f"✓ Data loaded successfully with shape: {df.shape}")
    print(f"  Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")
except FileNotFoundError:
    print(f"❌ Error: File not found at {file_path}")
    print("Please make sure the CSV file is in the correct location.")
    exit(1)

# Display basic information
print("Dataset Overview:")
print("-" * 40)
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())
print("\n")

# ============================================================================
# INSIGHT 1: Negara dengan Channel YouTube Terbanyak
# ============================================================================
print("[1/20] Generating Insight 1: Countries with Most YouTube Channels...")
country_counts = df.groupby("country").size().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
country_counts.head(10).plot(kind="bar", color="steelblue")
plt.title(
    "Top 10 Countries by Number of YouTube Channels", fontsize=16, fontweight="bold"
)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Number of Channels", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(
    f"{output_dir}/01_countries_most_channels.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 01_countries_most_channels.png")
print(
    f"  Top country: {country_counts.index[0]} with {country_counts.iloc[0]} channels\n"
)

# ============================================================================
# INSIGHT 2: Kategori Channel Paling Populer
# ============================================================================
print("[2/20] Generating Insight 2: Most Popular Channel Categories...")
category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 8))
colors = plt.cm.Set3(range(len(category_counts.head(10))))
category_counts.head(10).plot(
    kind="pie", autopct="%1.1f%%", colors=colors, startangle=90
)
plt.title("Top 10 YouTube Channel Categories", fontsize=16, fontweight="bold")
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{output_dir}/02_popular_categories.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 02_popular_categories.png")
print(
    f"  Most popular: {category_counts.index[0]} ({category_counts.iloc[0]} channels)\n"
)

# ============================================================================
# INSIGHT 3: Top 10 Channel dengan Subscriber Terbanyak
# ============================================================================
print("[3/20] Generating Insight 3: Top 10 Channels with Most Subscribers...")
top_channels = (
    df[["youtuber", "subscribers"]].sort_values("subscribers", ascending=False).head(10)
)

plt.figure(figsize=(12, 8))
plt.barh(range(len(top_channels)), top_channels["subscribers"].values, color="coral")
plt.yticks(range(len(top_channels)), top_channels["youtuber"].values)
plt.xlabel("Subscribers", fontsize=12)
plt.title("Top 10 Channels by Subscribers", fontsize=16, fontweight="bold")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(
    f"{output_dir}/03_top_channels_subscribers.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 03_top_channels_subscribers.png")
print(
    f"  #1: {top_channels.iloc[0]['youtuber']} with {top_channels.iloc[0]['subscribers']:,.0f} subscribers\n"
)

# ============================================================================
# INSIGHT 4: Hubungan Subscriber dengan Video Views
# ============================================================================
print(
    "[4/20] Generating Insight 4: Relationship between Subscribers and Video Views..."
)
plt.figure(figsize=(10, 6))
plt.scatter(df["subscribers"], df["video_views"], alpha=0.5, s=30, color="purple")
plt.title(
    "Relationship between Subscribers and Video Views", fontsize=16, fontweight="bold"
)
plt.xlabel("Subscribers", fontsize=12)
plt.ylabel("Video Views", fontsize=12)
plt.ticklabel_format(style="scientific", axis="both", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(f"{output_dir}/04_subscribers_vs_views.png", dpi=300, bbox_inches="tight")
plt.close()

correlation = df["subscribers"].corr(df["video_views"])
print(f"✓ Saved: 04_subscribers_vs_views.png")
print(f"  Correlation: {correlation:.3f}\n")

# ============================================================================
# INSIGHT 5: Pengaruh Jumlah Upload terhadap Subscriber
# ============================================================================
print("[5/20] Generating Insight 5: Influence of Upload Count on Subscribers...")
plt.figure(figsize=(10, 6))
plt.scatter(df["uploads"], df["subscribers"], alpha=0.5, s=30, color="green")
plt.title("Influence of Upload Count on Subscribers", fontsize=16, fontweight="bold")
plt.xlabel("Number of Uploads", fontsize=12)
plt.ylabel("Subscribers", fontsize=12)
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(f"{output_dir}/05_uploads_vs_subscribers.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 05_uploads_vs_subscribers.png\n")

# ============================================================================
# INSIGHT 6: Channel dengan Penghasilan Tahunan Tertinggi
# ============================================================================
print("[6/20] Generating Insight 6: Channels with Highest Annual Earnings...")
top_earnings = (
    df[["youtuber", "highest_yearly_earnings"]]
    .sort_values("highest_yearly_earnings", ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 8))
plt.bar(
    range(len(top_earnings)),
    top_earnings["highest_yearly_earnings"].values,
    color="gold",
)
plt.xticks(
    range(len(top_earnings)), top_earnings["youtuber"].values, rotation=45, ha="right"
)
plt.ylabel("Annual Earnings ($)", fontsize=12)
plt.title("Top 10 Channels by Annual Earnings", fontsize=16, fontweight="bold")
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(f"{output_dir}/06_top_annual_earnings.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 06_top_annual_earnings.png")
print(
    f"  Highest earner: {top_earnings.iloc[0]['youtuber']} (${top_earnings.iloc[0]['highest_yearly_earnings']:,.0f})\n"
)

# ============================================================================
# INSIGHT 7: Negara dengan Total Subscriber Terbesar
# ============================================================================
print("[7/20] Generating Insight 7: Countries with Total Largest Subscribers...")
country_subs = df.groupby("country")["subscribers"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
country_subs.head(10).plot(kind="bar", color="teal")
plt.title("Countries with Total Largest Subscribers", fontsize=16, fontweight="bold")
plt.xlabel("Country", fontsize=12)
plt.ylabel("Total Subscribers", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(
    f"{output_dir}/07_countries_total_subscribers.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 07_countries_total_subscribers.png")
print(
    f"  Top country: {country_subs.index[0]} with {country_subs.iloc[0]:,.0f} total subscribers\n"
)

# ============================================================================
# INSIGHT 8: Rata-rata Views Berdasarkan Kategori
# ============================================================================
print("[8/20] Generating Insight 8: Average Views by Category...")
category_avg_views = (
    df.groupby("category")["video_views"].mean().sort_values(ascending=False)
)

plt.figure(figsize=(12, 8))
category_avg_views.head(10).plot(kind="bar", color="orange")
plt.title("Average Views by Category", fontsize=16, fontweight="bold")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Average Video Views", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(f"{output_dir}/08_avg_views_by_category.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 08_avg_views_by_category.png")
print(
    f"  Highest avg views: {category_avg_views.index[0]} ({category_avg_views.iloc[0]:,.0f} views)\n"
)

# ============================================================================
# INSIGHT 9: Pertumbuhan Subscriber dalam 30 Hari Terakhir
# ============================================================================
print("[9/20] Generating Insight 9: Subscriber Growth in Last 30 Days...")
growth = (
    df[["youtuber", "subscribers_for_last_30_days"]]
    .sort_values("subscribers_for_last_30_days", ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 8))
plt.bar(
    range(len(growth)), growth["subscribers_for_last_30_days"].values, color="crimson"
)
plt.xticks(range(len(growth)), growth["youtuber"].values, rotation=45, ha="right")
plt.ylabel("Subscriber Growth (30 days)", fontsize=12)
plt.title("Subscriber Growth in Last 30 Days", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(
    f"{output_dir}/09_subscriber_growth_30days.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 09_subscriber_growth_30days.png")
print(
    f"  Fastest growing: {growth.iloc[0]['youtuber']} (+{growth.iloc[0]['subscribers_for_last_30_days']:,.0f})\n"
)

# ============================================================================
# INSIGHT 10: Distribusi Jumlah Upload Video
# ============================================================================
print("[10/20] Generating Insight 10: Distribution of Video Upload Counts...")
plt.figure(figsize=(10, 6))
plt.hist(df["uploads"].dropna(), bins=50, alpha=0.7, color="navy", edgecolor="black")
plt.title("Distribution of Video Upload Counts", fontsize=16, fontweight="bold")
plt.xlabel("Number of Uploads", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()
plt.savefig(f"{output_dir}/10_upload_distribution.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 10_upload_distribution.png")
print(
    f"  Mean uploads: {df['uploads'].mean():,.0f}, Median: {df['uploads'].median():,.0f}\n"
)

# ============================================================================
# INSIGHT 11: Tahun Pembuatan Channel dan Subscriber
# ============================================================================
print("[11/20] Generating Insight 11: Channel Creation Year vs Subscribers...")
plt.figure(figsize=(10, 6))
plt.scatter(df["created_year"], df["subscribers"], alpha=0.5, s=30, color="brown")
plt.title("Channel Creation Year vs Subscribers", fontsize=16, fontweight="bold")
plt.xlabel("Creation Year", fontsize=12)
plt.ylabel("Subscribers", fontsize=12)
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(
    f"{output_dir}/11_creation_year_vs_subscribers.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 11_creation_year_vs_subscribers.png\n")

# ============================================================================
# INSIGHT 12: Jenis Channel yang Paling Dominan
# ============================================================================
print("[12/20] Generating Insight 12: Dominant Channel Types...")
channel_type_counts = df["channel_type"].value_counts()

plt.figure(figsize=(10, 8))
colors = plt.cm.Pastel1(range(len(channel_type_counts.head(10))))
channel_type_counts.head(10).plot(
    kind="pie", autopct="%1.1f%%", colors=colors, startangle=90
)
plt.title("Dominant Channel Types", fontsize=16, fontweight="bold")
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{output_dir}/12_dominant_channel_types.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 12_dominant_channel_types.png")
print(
    f"  Most dominant: {channel_type_counts.index[0]} ({channel_type_counts.iloc[0]} channels)\n"
)

# ============================================================================
# INSIGHT 13: Perbandingan Penghasilan Bulanan Channel
# ============================================================================
print("[13/20] Generating Insight 13: Monthly Earnings Comparison...")
top_monthly = (
    df[["youtuber", "highest_monthly_earnings"]]
    .sort_values("highest_monthly_earnings", ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 8))
plt.bar(
    range(len(top_monthly)),
    top_monthly["highest_monthly_earnings"].values,
    color="darkgreen",
)
plt.xticks(
    range(len(top_monthly)), top_monthly["youtuber"].values, rotation=45, ha="right"
)
plt.ylabel("Highest Monthly Earnings ($)", fontsize=12)
plt.title("Monthly Earnings Comparison (Top 10)", fontsize=16, fontweight="bold")
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(
    f"{output_dir}/13_monthly_earnings_comparison.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 13_monthly_earnings_comparison.png\n")

# ============================================================================
# INSIGHT 14: Channel dengan Video Views Terbesar
# ============================================================================
print("[14/20] Generating Insight 14: Channels with Most Video Views...")
top_views = (
    df[["youtuber", "video_views"]].sort_values("video_views", ascending=False).head(10)
)

plt.figure(figsize=(12, 8))
plt.barh(range(len(top_views)), top_views["video_views"].values, color="dodgerblue")
plt.yticks(range(len(top_views)), top_views["youtuber"].values)
plt.xlabel("Video Views", fontsize=12)
plt.title("Channels with Most Video Views", fontsize=16, fontweight="bold")
plt.gca().invert_yaxis()
plt.ticklabel_format(style="scientific", axis="x", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(f"{output_dir}/14_channels_most_views.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 14_channels_most_views.png")
print(
    f"  Most views: {top_views.iloc[0]['youtuber']} ({top_views.iloc[0]['video_views']:,.0f} views)\n"
)

# ============================================================================
# INSIGHT 15: Upload Sedikit tetapi Subscriber Tinggi
# ============================================================================
print("[15/20] Generating Insight 15: Few Uploads but High Subscribers...")
plt.figure(figsize=(10, 6))
plt.scatter(df["uploads"], df["subscribers"], alpha=0.5, s=30, color="magenta")
plt.title("Few Uploads but High Subscribers", fontsize=16, fontweight="bold")
plt.xlabel("Number of Uploads", fontsize=12)
plt.ylabel("Subscribers", fontsize=12)
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(
    f"{output_dir}/15_uploads_vs_subscribers_quality.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 15_uploads_vs_subscribers_quality.png\n")

# ============================================================================
# INSIGHT 16: Distribusi Tahun Pembuatan Channel
# ============================================================================
print("[16/20] Generating Insight 16: Distribution of Channel Creation Year...")
plt.figure(figsize=(10, 6))
plt.hist(
    df["created_year"].dropna(),
    bins=30,
    alpha=0.7,
    color="darkviolet",
    edgecolor="black",
)
plt.title("Distribution of Channel Creation Year", fontsize=16, fontweight="bold")
plt.xlabel("Year Created", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()
plt.savefig(
    f"{output_dir}/16_creation_year_distribution.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 16_creation_year_distribution.png\n")

# ============================================================================
# INSIGHT 17: Pengaruh Kategori terhadap Penghasilan
# ============================================================================
print("[17/20] Generating Insight 17: Influence of Category on Earnings...")
category_earnings = (
    df.groupby("category")["highest_yearly_earnings"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 8))
category_earnings.head(10).plot(kind="bar", color="darkred")
plt.title("Influence of Category on Earnings", fontsize=16, fontweight="bold")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Average Annual Earnings ($)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(
    f"{output_dir}/17_category_influence_earnings.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 17_category_influence_earnings.png")
print(
    f"  Highest earning category: {category_earnings.index[0]} (${category_earnings.iloc[0]:,.0f} avg)\n"
)

# ============================================================================
# INSIGHT 18: Video Views dalam 30 Hari Terakhir
# ============================================================================
print("[18/20] Generating Insight 18: Video Views in Last 30 Days...")
trending = (
    df[["youtuber", "video_views_for_the_last_30_days"]]
    .sort_values("video_views_for_the_last_30_days", ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 8))
plt.plot(
    range(len(trending)),
    trending["video_views_for_the_last_30_days"].values,
    marker="o",
    linewidth=2,
    markersize=8,
    color="darkorange",
)
plt.xticks(range(len(trending)), trending["youtuber"].values, rotation=45, ha="right")
plt.ylabel("Views (Last 30 Days)", fontsize=12)
plt.title(
    "Video Views in Last 30 Days (Trending Channels)", fontsize=16, fontweight="bold"
)
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/18_views_last_30days.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"✓ Saved: 18_views_last_30days.png")
print(
    f"  Most trending: {trending.iloc[0]['youtuber']} ({trending.iloc[0]['video_views_for_the_last_30_days']:,.0f} views)\n"
)

# ============================================================================
# INSIGHT 19: Hubungan Upload dan Video Views
# ============================================================================
print("[19/20] Generating Insight 19: Relationship between Uploads and Video Views...")
plt.figure(figsize=(10, 6))
plt.scatter(df["uploads"], df["video_views"], alpha=0.5, s=30, color="cyan")
plt.title(
    "Relationship between Uploads and Video Views", fontsize=16, fontweight="bold"
)
plt.xlabel("Number of Uploads", fontsize=12)
plt.ylabel("Video Views", fontsize=12)
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(f"{output_dir}/19_uploads_vs_views.png", dpi=300, bbox_inches="tight")
plt.close()

correlation_uploads_views = df["uploads"].corr(df["video_views"])
print(f"✓ Saved: 19_uploads_vs_views.png")
print(f"  Correlation: {correlation_uploads_views:.3f}\n")

# ============================================================================
# INSIGHT 20: Negara dengan Penghasilan Channel Tertinggi
# ============================================================================
print("[20/20] Generating Insight 20: Countries with Highest Channel Earnings...")
country_earnings = (
    df.groupby("country")["highest_yearly_earnings"].sum().sort_values(ascending=False)
)

plt.figure(figsize=(12, 8))
country_earnings.head(10).plot(kind="bar", color="indigo")
plt.title("Countries with Highest Channel Earnings", fontsize=16, fontweight="bold")
plt.xlabel("Country", fontsize=12)
plt.ylabel("Total Annual Earnings ($)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.ticklabel_format(style="scientific", axis="y", scilimits=(0, 0))
plt.tight_layout()
plt.savefig(
    f"{output_dir}/20_countries_highest_earnings.png", dpi=300, bbox_inches="tight"
)
plt.close()
print(f"✓ Saved: 20_countries_highest_earnings.png")
print(
    f"  Top earning country: {country_earnings.index[0]} (${country_earnings.iloc[0]:,.0f} total)\n"
)

# ============================================================================
# Summary
# ============================================================================
print("=" * 80)
print("VISUALIZATION COMPLETE!")
print("=" * 80)
print(f"\n✓ All 20 insights have been generated successfully!")
print(f"✓ All visualizations saved to: {output_dir}/")
print(f"✓ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\nGenerated files:")
print("-" * 40)

for i in range(1, 21):
    filename = [f for f in os.listdir(output_dir) if f.startswith(f"{i:02d}_")]
    if filename:
        print(f"  {filename[0]}")

print("\n" + "=" * 80)
print("You can now view all the PNG files in the '{}' folder!".format(output_dir))
print("=" * 80)
