import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

# Configure the dashboard
st.set_page_config(
    page_title="Netflix Business Insights",
    page_icon="🎬",
    layout="wide"
)

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "Task1_Data_Cleaning" / "netflix_cleaned.csv"

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv(DATA_FILE)
    data["date_added"] = pd.to_datetime(
        data["date_added"], errors="coerce"
    )
    return data

df = load_data()

# Dashboard title
st.title("🎬 Netflix Business Insights Dashboard")
st.markdown(
    "Explore Netflix's content library through interactive data visualizations."
)

# Sidebar filters
st.sidebar.header("Dashboard Filters")

content_types = st.sidebar.multiselect(
    "Select Content Type",
    options=sorted(df["type"].dropna().unique()),
    default=sorted(df["type"].dropna().unique())
)

min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())

year_range = st.sidebar.slider(
    "Select Release Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Apply filters
filtered_df = df[
    df["type"].isin(content_types)
    & df["release_year"].between(year_range[0], year_range[1])
]

# Key performance indicators
total_titles = len(filtered_df)
total_movies = (filtered_df["type"] == "Movie").sum()
total_tv_shows = (filtered_df["type"] == "TV Show").sum()
unique_release_years = filtered_df["release_year"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", f"{total_titles:,}")
col2.metric("Movies", f"{total_movies:,}")
col3.metric("TV Shows", f"{total_tv_shows:,}")
col4.metric("Release Years", unique_release_years)

st.divider()

# Content type distribution
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Content Type Distribution")

    type_counts = filtered_df["type"].value_counts().reset_index()
    type_counts.columns = ["Content Type", "Titles"]

    fig_type = px.pie(
        type_counts,
        names="Content Type",
        values="Titles",
        hole=0.4,
        title="Movies vs TV Shows"
    )

    st.plotly_chart(fig_type, width="stretch")

# Release year trend
with right_col:
    st.subheader("Release Year Trend")

    yearly_counts = (
        filtered_df.groupby("release_year")
        .size()
        .reset_index(name="Titles")
        .sort_values("release_year")
    )

    fig_year = px.line(
        yearly_counts,
        x="release_year",
        y="Titles",
        markers=True,
        title="Titles by Release Year"
    )

    st.plotly_chart(fig_year, use_container_width=True)

st.divider()

# Top genres
st.subheader("Top 10 Genres")

genres = (
    filtered_df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_genres = genres[genres != "Unknown"].value_counts().head(10)

genre_df = top_genres.rename_axis("Genre").reset_index(name="Titles")

fig_genres = px.bar(
    genre_df,
    x="Titles",
    y="Genre",
    orientation="h",
    title="Most Common Genres"
)

fig_genres.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig_genres, use_container_width=True)

# Top countries
st.subheader("Top 10 Countries")

countries = (
    filtered_df["country"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_countries = countries[countries != "Unknown"].value_counts().head(10)

country_df = top_countries.rename_axis("Country").reset_index(name="Titles")

fig_countries = px.bar(
    country_df,
    x="Country",
    y="Titles",
    title="Countries with the Most Titles"
)

st.plotly_chart(fig_countries, use_container_width=True)

# Data preview
with st.expander("View Filtered Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# Business insights
st.subheader("Business Insights")

if not filtered_df.empty:
    if not type_counts.empty:
        dominant_type = type_counts.loc[
            type_counts["Titles"].idxmax(), "Content Type"
        ]
        st.write(f"- Most represented content type: **{dominant_type}**.")

    if not top_genres.empty:
        st.write(
            f"- Most common genre in the filtered data: **{top_genres.index[0]}**."
        )

    if not top_countries.empty:
        st.write(
            f"- Country contributing the most titles: **{top_countries.index[0]}**."
        )
else:
    st.warning("No titles match the selected filters.")

st.caption("Data source: Provided Netflix dataset | Created for Data Science Internship")
