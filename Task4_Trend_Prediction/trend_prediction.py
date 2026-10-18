import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "Task1_Data_Cleaning" / "netflix_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "Task4_Trend_Prediction"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

# Count titles released in each year
yearly_content = (
    df.groupby("release_year")
    .size()
    .reset_index(name="total_titles")
    .sort_values("release_year")
)

print("Historical Content by Release Year:")
print(yearly_content.tail(10))

# Prepare data for the model
X = yearly_content[["release_year"]]
y = yearly_content["total_titles"]

# Train a linear regression model on historical data
model = LinearRegression()
model.fit(X, y)

# Predict historical values to evaluate the model
historical_predictions = model.predict(X)

mae = mean_absolute_error(y, historical_predictions)
r2 = r2_score(y, historical_predictions)

print("\nModel Evaluation:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared Score: {r2:.3f}")

# Estimate content counts for the next five years
future_years = pd.DataFrame({
    "release_year": range(
        int(yearly_content["release_year"].max()) + 1,
        int(yearly_content["release_year"].max()) + 6
    )
})

future_years["predicted_titles"] = model.predict(
    future_years[["release_year"]]
).round(0).astype(int)

print("\nEstimated Content Counts for Future Years:")
print(future_years)

# Save historical data and future estimates
yearly_content.to_csv(
    OUTPUT_DIR / "historical_yearly_content.csv",
    index=False
)

future_years.to_csv(
    OUTPUT_DIR / "future_content_estimates.csv",
    index=False
)

# Plot historical trend and future estimates
plt.figure(figsize=(12, 6))

plt.plot(
    yearly_content["release_year"],
    yearly_content["total_titles"],
    label="Historical Data"
)

plt.plot(
    future_years["release_year"],
    future_years["predicted_titles"],
    marker="o",
    linestyle="--",
    label="Linear Regression Estimate"
)

plt.title("Netflix Content Release Trend and Future Estimates")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "trend_prediction.png")
plt.show()

print("\nTrend Prediction Analysis completed successfully!")
print("Files saved in:", OUTPUT_DIR)