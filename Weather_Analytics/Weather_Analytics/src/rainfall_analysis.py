from utilities import load_cleaned_data, prepare_data

# Calculate basic rainfall statistics
def rainfall_statistics(df):
    print("\n========== RAINFALL STATISTICS ==========\n")
    total_rainfall = df["Rainfall"].sum()
    average_rainfall = df["Rainfall"].mean()
    maximum_rainfall = df["Rainfall"].max()
    minimum_rainfall = df["Rainfall"].min()
    
    print(f"Total Rainfall   : {total_rainfall:.2f} mm")
    print(f"Average Rainfall : {average_rainfall:.2f} mm")
    print(f"Maximum Rainfall : {maximum_rainfall:.2f} mm")
    print(f"Minimum Rainfall : {minimum_rainfall:.2f} mm")

# Calculate and display monthly average rainfall
def monthly_rainfall(df):
    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    monthly = df.groupby("Month")["Rainfall"].mean()
    monthly = monthly.reindex(month_order)
    monthly = monthly.round(2)
    print("\n========== MONTHLY AVERAGE RAINFALL ==========\n")
    print(monthly)
    
    highest = monthly.idxmax()
    rainfall = monthly.max()
    print("\nHighest Average Rainfall Month")
    print(f"{highest} ({rainfall:.2f} mm)")
    return monthly

# Calculate and display district-wise average rainfall
def district_rainfall(df):
    district = df.groupby("District")["Rainfall"].mean().round(2)
    print("\n========== DISTRICT WISE RAINFALL ==========\n")
    print(district)
    
    highest = district.idxmax()
    rainfall = district.max()
    print("\nDistrict with Highest Average Rainfall")
    print(f"{highest} ({rainfall:.2f} mm)")

# Calculate and display seasonal average rainfall
def seasonal_rainfall(df):
    season_order = [
        "Winter",
        "Summer",
        "Monsoon",
        "Post-Monsoon"
    ]
    season = df.groupby("Season")["Rainfall"].mean()
    season = season.reindex(season_order)
    season = season.round(2)
    print("\n========== SEASONAL RAINFALL ==========\n")
    print(season)

# Main function for rainfall analysis
def main():
    df = load_cleaned_data()
    if df is not None:
        df = prepare_data(df)
        rainfall_statistics(df)
        monthly_rainfall(df)
        district_rainfall(df)
        seasonal_rainfall(df)
        print("\nRainfall Analysis Module Executed Successfully.")

if __name__ == "__main__":
    main()