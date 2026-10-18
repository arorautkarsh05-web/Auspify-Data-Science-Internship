import pandas as pd
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "Dataset.csv"
OUTPUT_DIR = BASE_DIR / "Task1_Data_Cleaning"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the dataset
df = pd.read_csv(INPUT_FILE)

print("Original Dataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())
print("Duplicate Show IDs:", df["show_id"].duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Clean text columns
text_columns = [
    "type", "title", "director", "country",
    "rating", "duration", "listed_in"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# Convert date column to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"], errors="coerce"
)

# Extract duration value and unit
df["duration_value"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

df["duration_unit"] = df["duration"].str.extract(
    r"(min|Season|Seasons)", expand=False
)

# Handle missing text values
for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# Save cleaned dataset
output_file = OUTPUT_DIR / "netflix_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nCleaned Dataset Shape:", df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nCleaned dataset saved successfully:")
print(output_file)