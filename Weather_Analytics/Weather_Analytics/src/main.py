import pandas as pd
from utilities import load_cleaned_data, print_heading, print_subheading

from data_loader import main as load_dataset
from weather_analysis import main as weather_analysis
from rainfall_analysis import main as rainfall_analysis
from flood_analysis import main as flood_analysis
from statistics_module import statistics_module as statistics_analysis
from visualization import main as generate_graphs

# Calculate derived quantities
def derived_quantities():
    print("\nCleaned Dataset Loaded Successfully.")
    
    # Load cleaned data
    df = pd.read_csv("../data/cleaned_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month_name()
    
    print("\n================ DERIVED QUANTITIES ================\n")
    
    # Daily average temperature
    df["Average_Temperature"] = (
        df["Maximum_Temperature"] + df["Minimum_Temperature"]
    ) / 2
    
    print("Average Temperature (First 10 Records)\n")
    print(df[["Date", "District", "Average_Temperature"]].head(10))
    
    # Temperature difference
    df["Temperature_Range"] = (
        df["Maximum_Temperature"] - df["Minimum_Temperature"]
    )
    
    print("\nTemperature Range (First 10 Records)\n")
    print(df[["Date", "District", "Temperature_Range"]].head(10))
    
    # Rainfall category classification function
    def rainfall_category(rain):
        if rain < 5:
            return "Low"
        elif rain < 20:
            return "Moderate"
        elif rain < 50:
            return "Heavy"
        else:
            return "Very Heavy"
            
    df["Rainfall_Category"] = df["Rainfall"].apply(rainfall_category)
    
    print("\nRainfall Category Count\n")
    print(df["Rainfall_Category"].value_counts())
    
    # Average monthly temperature
    monthly_avg = df.groupby("Month")["Average_Temperature"].mean()
    print("\nAverage Monthly Temperature\n")
    print(monthly_avg.round(2))
    
    # Average monthly humidity
    monthly_humidity = df.groupby("Month")["Humidity"].mean()
    print("\nAverage Monthly Humidity\n")
    print(monthly_humidity.round(2))
    print("\nDerived Quantities Module Executed Successfully.")

# Classify flood risk based on rainfall, river level and humidity
def classify_risk(rainfall, river_level, humidity):
    if rainfall >= 120 or river_level >= 15:
        return "Severe Risk"
    elif rainfall >= 70 or river_level >= 10:
        return "High Risk"
    elif rainfall >= 30 or humidity >= 85:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Run flood warning analysis
def flood_warning():
    print_heading("Flood Warning System")
    
    # Load dataset
    df = pd.read_csv("../data/cleaned_data.csv")
    
    # Apply flood risk classification
    df["Flood_Warning"] = df.apply(
        lambda row: classify_risk(
            row["Rainfall"],
            row["River_Level"],
            row["Humidity"]
        ),
        axis=1
    )
    
    print_subheading("Flood Warning Summary")
    print(df["Flood_Warning"].value_counts())
    
    print_subheading("High And Severe Risk Records")
    warning = df[
        df["Flood_Warning"].isin(
            ["High Risk", "Severe Risk"]
        )
    ]
    
    if len(warning) == 0:
        print("No High or Severe Risk Days Found.")
    else:
        print(
            warning[
                [
                    "Date",
                    "District",
                    "Rainfall",
                    "River_Level",
                    "Humidity",
                    "Flood_Warning"
                ]
            ].head(20)
        )
        
    print_subheading("District Wise Flood Warning")
    district_summary = pd.crosstab(
        df["District"],
        df["Flood_Warning"]
    )
    print(district_summary)
    
    # Save the updated warning dataset
    df.to_csv("../data/flood_warning.csv", index=False)
    print("\nFlood warning report saved successfully.")
    print("\nFlood Warning Module Executed Successfully.")

# Prepare weekly/monthly averages and moving average predictions
def prepare_prediction(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Average_Temperature"] = (
        df["Maximum_Temperature"] +
        df["Minimum_Temperature"]
    ) / 2
    
    # Sort dataset by date
    df = df.sort_values("Date")
    last7 = df.tail(7).copy()
    
    # Extract previous week and month data
    previous7 = df.iloc[-14:-7]
    previous30 = df.iloc[-37:-7]
    
    week_avg = previous7["Rainfall"].mean()
    month_avg = previous30["Rainfall"].mean()
    
    # Calculate moving average
    moving_avg = (
        df["Rainfall"]
        .rolling(window=7)
        .mean()
        .iloc[-1]
    )
    
    # Create prediction DataFrame for next 7 days
    prediction_df = pd.DataFrame({
        "Day": [
            "Day 1",
            "Day 2",
            "Day 3",
            "Day 4",
            "Day 5",
            "Day 6",
            "Day 7"
        ],
        "Predicted Rainfall (mm)": [
            round(moving_avg, 2)
        ] * 7
    })
    
    return (
        df,
        last7,
        week_avg,
        month_avg,
        moving_avg,
        prediction_df
    )

# Run the prediction module
def prediction():
    print_heading("SEVEN-DAY PREDICTION")
    df = load_cleaned_data()
    
    (
        df,
        last7,
        week_avg,
        month_avg,
        moving_avg,
        prediction_df
    ) = prepare_prediction(df)
    
    print_subheading("Prediction Summary")
    print(f"Previous Week Average Rainfall : {week_avg:.2f} mm")
    print(f"Previous Month Average Rainfall: {month_avg:.2f} mm")
    print(f"Moving Average Prediction      : {moving_avg:.2f} mm")
    
    print_subheading("Actual Last 7 Days")
    print(
        last7[
            [
                "Date",
                "District",
                "Rainfall",
                "Average_Temperature",
                "Humidity",
                "River_Level"
            ]
        ]
    )
    
    print_subheading("Predicted Rainfall (Next 7 Days)")
    print(prediction_df)
    
    # Save predictions to CSV
    prediction_df.to_csv(
        "../data/seven_day_prediction.csv",
        index=False
    )
    print("\nPrediction report saved successfully.")
    print("\nSeven-Day Prediction Module Executed Successfully.")

# Display line
def line():
    print("=" * 70)

# Display heading
def heading():
    line()
    print("               WEATHER ANALYTICS TOOLKIT")
    print("                    Project III")
    line()

# Display menu choices
def menu():
    heading()
    print("1. Load and Clean Dataset")
    print("2. Weather Analysis")
    print("3. Rainfall Analysis")
    print("4. Flood Analysis")
    print("5. Statistical Analysis")
    print("6. Derived Quantities")
    print("7. Visualization")
    print("8. Flood Warning System")
    print("9. Seven-Day Prediction")
    print("10. Run Complete Project")
    print("11. Exit")
    line()

# Pause execution
def pause():
    input("\nPress Enter to Continue...")

# Run complete project step-by-step
def run_complete_project():
    print("\nRunning Complete Weather Analytics Project...\n")
    print("1. Loading Dataset...")
    load_dataset()
    print("\n2. Weather Analysis...")
    weather_analysis()
    print("\n3. Rainfall Analysis...")
    rainfall_analysis()
    print("\n4. Flood Analysis...")
    flood_analysis()
    print("\n5. Statistical Analysis...")
    statistics_analysis()
    print("\n6. Derived Quantities...")
    derived_quantities()
    print("\n7. Generating Graphs...")
    generate_graphs()
    print("\n8. Flood Warning System...")
    flood_warning()
    print("\n9. Seven-Day Prediction...")
    prediction()
    print("\n")
    line()
    print("PROJECT COMPLETED SUCCESSFULLY")
    line()

# Main function with loop control
def main():
    while True:
        menu()
        choice = input("Enter your choice (1-11): ")
        if choice == "1":
            print("\nLoading and Cleaning Dataset...\n")
            load_dataset()
            pause()
        elif choice == "2":
            print("\nWeather Analysis\n")
            weather_analysis()
            pause()
        elif choice == "3":
            print("\nRainfall Analysis\n")
            rainfall_analysis()
            pause()
        elif choice == "4":
            print("\nFlood Analysis\n")
            flood_analysis()
            pause()
        elif choice == "5":
            print("\nStatistical Analysis\n")
            statistics_analysis()
            pause()
        elif choice == "6":
            print("\nDerived Quantities\n")
            derived_quantities()
            pause()
        elif choice == "7":
            print("\nVisualization Module\n")
            generate_graphs()
            pause()
        elif choice == "8":
            print("\nFlood Warning System\n")
            flood_warning()
            pause()
        elif choice == "9":
            print("\nSeven-Day Weather Prediction\n")
            prediction()
            pause()
        elif choice == "10":
            run_complete_project()
            pause()
        elif choice == "11":
            print("Thank You for Using")
            print("Weather Analytics Toolkit")
            print("Project III")
            break
        else:
            print("\nInvalid Choice.")
            print("Please Enter a Number Between 1 and 11.")
            pause()

if __name__ == "__main__":
    main()