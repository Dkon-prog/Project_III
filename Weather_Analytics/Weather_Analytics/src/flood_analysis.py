from utilities import load_cleaned_data, prepare_data, print_heading

# Classify flood risk using Rainfall, Humidity and River Level
def classify_flood_risk(row):
    rainfall = row["Rainfall"]
    humidity = row["Humidity"]
    river = row["River_Level"]
    
    if rainfall >= 120 and river >= 8.0 and humidity >= 90:
        return "Severe Risk"
    elif rainfall >= 80 and river >= 7.0 and humidity >= 85:
        return "High Risk"
    elif rainfall >= 40 and river >= 5.5 and humidity >= 75:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Add Flood_Risk column to DataFrame
def add_flood_risk(df):
    df["Flood_Risk"] = df.apply(classify_flood_risk, axis=1)
    return df

# Display river level statistics
def river_level_statistics(df):
    print_heading("River Level Statistics")
    print(f"\nHighest River Level : {df['River_Level'].max():.2f} m")
    print(f"Lowest River Level  : {df['River_Level'].min():.2f} m")
    print(f"Average River Level : {df['River_Level'].mean():.2f} m")

# Display summary of flood risk categories
def flood_risk_summary(df):
    print_heading("Flood Warning Summary")
    summary = df["Flood_Risk"].value_counts()
    print(summary)

# Display high or severe flood risk records
def high_risk_records(df):
    print_heading("High Flood Risk Records")
    high = df[
        (df["Flood_Risk"] == "High Risk") |
        (df["Flood_Risk"] == "Severe Risk")
    ]
    if high.empty:
        print("\nNo High Flood Risk Records Found.")
    else:
        print(f"\nTotal High Risk Records : {len(high)}\n")
        print(
            high[
                [
                    "Date",
                    "District",
                    "Rainfall",
                    "Humidity",
                    "River_Level",
                    "Flood_Risk"
                ]
            ].head(20)
        )

# Display district-wise average river levels
def district_flood_risk(df):
    print_heading("District Wise Average River Level")
    district = (
        df.groupby("District")["River_Level"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )
    print(district)

# Display possible flood-prone dates
def flood_prone_periods(df):
    print_heading("Possible Flood-Prone Periods")
    flood_days = df[df["Flood_Risk"] != "Low Risk"]
    if flood_days.empty:
        print("\nNo Flood-Prone Periods Found.")
    else:
        print(
            flood_days[
                [
                    "Date",
                    "District",
                    "Flood_Risk"
                ]
            ].head(20)
        )

# Main function for flood analysis
def main():
    df = load_cleaned_data()
    if df is not None:
        df = prepare_data(df)
        df = add_flood_risk(df)
        river_level_statistics(df)
        flood_risk_summary(df)
        high_risk_records(df)
        district_flood_risk(df)
        flood_prone_periods(df)
        print("\nFlood Analysis Module Executed Successfully.")

if __name__ == "__main__":
    main()