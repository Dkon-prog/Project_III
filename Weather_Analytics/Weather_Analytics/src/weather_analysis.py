import pandas as pd
from utilities import load_cleaned_data, prepare_data

# Calculate monthly average temperatures
def calculate_monthly_average(df):
    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    monthly_summary = df.groupby("Month")[[
        "Maximum_Temperature",
        "Minimum_Temperature"
    ]].mean()
    monthly_summary = monthly_summary.reindex(month_order)
    monthly_summary = monthly_summary.round(2)
    print("\n========== MONTHLY AVERAGE TEMPERATURE ==========\n")
    print(monthly_summary)
    return monthly_summary

# Find the hottest month
def hottest_month(monthly_summary):
    hottest = monthly_summary["Maximum_Temperature"].idxmax()
    temperature = monthly_summary["Maximum_Temperature"].max()
    print("\n========== HOTTEST MONTH ==========\n")
    print(f"{hottest} ({temperature:.2f} °C)")

# Find the coldest month
def coldest_month(monthly_summary):
    coldest = monthly_summary["Minimum_Temperature"].idxmin()
    temperature = monthly_summary["Minimum_Temperature"].min()
    print("\n========== COLDEST MONTH ==========\n")
    print(f"{coldest} ({temperature:.2f} °C)")

# Find extreme maximum and minimum temperatures
def extreme_temperatures(df):
    highest = df["Maximum_Temperature"].max()
    lowest = df["Minimum_Temperature"].min()
    print("\n========== EXTREME TEMPERATURES ==========\n")
    print(f"Highest Temperature : {highest:.2f} °C")
    print(f"Lowest Temperature  : {lowest:.2f} °C")

# Perform seasonal temperature analysis
def seasonal_analysis(df):
    season_order = [
        "Winter",
        "Summer",
        "Monsoon",
        "Post-Monsoon"
    ]
    season_summary = df.groupby("Season")[[
        "Maximum_Temperature",
        "Minimum_Temperature"
    ]].mean()
    season_summary = season_summary.reindex(season_order)
    season_summary = season_summary.round(2)
    print("\n========== SEASONAL TEMPERATURE ANALYSIS ==========\n")
    print(season_summary)

# Save monthly summary to CSV
def save_monthly_summary(monthly_summary):
    monthly_summary.to_csv("../data/monthly_summary.csv")
    print("\nmonthly_summary.csv created successfully.")

# Main function for weather analysis
def main():
    df = load_cleaned_data()
    if df is not None:
        df = prepare_data(df)
        monthly_summary = calculate_monthly_average(df)
        hottest_month(monthly_summary)
        coldest_month(monthly_summary)
        extreme_temperatures(df)
        seasonal_analysis(df)
        save_monthly_summary(monthly_summary)
        print("\nWeather Analysis Module Executed Successfully.")

if __name__ == "__main__":
    main()