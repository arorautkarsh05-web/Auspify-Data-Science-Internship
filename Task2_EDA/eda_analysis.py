import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "Task1_Data_Cleaning" / "netflix_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "Task2_EDA"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

print("Dataset Shape:", df.shape)

# 1. Movies vs TV Shows
print("\nContent Type Count:")
print(df["type"].value_counts())

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "content_type.png")
plt.show()

# 2. Top 10 Countries
countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_countries = countries[countries != "Unknown"].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_countries.png")
plt.show()

# 3. Content released by year
yearly_content = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(12, 5))
yearly_content.plot()
plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "release_year_trend.png")
plt.show()

# 4. Top 10 Genres
genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_genres = genres[genres != "Unknown"].value_counts().head(10)

print("\nTop 10 Genres:")
print(top_genres)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_genres.png")
plt.show()

# 5. Movie duration distribution
movie_duration = df.loc[
    df["type"] == "Movie", "duration_value"
].dropna()

plt.figure(figsize=(10, 5))
sns.histplot(movie_duration, bins=30, kde=True)
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "movie_duration.png")
plt.show()

print("\nEDA completed successfully!")
print("Charts saved in:", OUTPUT_DIR)