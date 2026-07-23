import pandas as pd
from utilities import load_cleaned_data

# Print statistics for a specific column
def display_statistics(name, data, unit=""):
    print("\n" + "=" * 60)
    print(name.upper())
    print("=" * 60)
    
    print(f"Mean               : {data.mean():.2f} {unit}")
    print(f"Median             : {data.median():.2f} {unit}")
    print(f"Mode               : {data.mode()[0]:.2f} {unit}")
    print(f"Maximum            : {data.max():.2f} {unit}")
    print(f"Minimum            : {data.min():.2f} {unit}")
    print(f"Standard Deviation : {data.std():.2f}")
    print(f"Variance           : {data.var():.2f}")

# Calculate and display statistics for weather columns
def statistics_module():
    df = load_cleaned_data()
    display_statistics(
        "Temperature Statistics",
        df["Maximum_Temperature"],
        "°C"
    )
    display_statistics(
        "Rainfall Statistics",
        df["Rainfall"],
        "mm"
    )
    display_statistics(
        "Humidity Statistics",
        df["Humidity"],
        "%"
    )
    
    print("\n" + "=" * 60)
    print("CORRELATION ANALYSIS")
    print("=" * 60)
    
    rainfall_river = df["Rainfall"].corr(df["River_Level"])
    humidity_rainfall = df["Humidity"].corr(df["Rainfall"])
    temperature_humidity = df["Maximum_Temperature"].corr(df["Humidity"])
    
    print(f"Rainfall vs River Level : {rainfall_river:.3f}")
    print(f"Humidity vs Rainfall    : {humidity_rainfall:.3f}")
    print(f"Temperature vs Humidity : {temperature_humidity:.3f}")
    
    print("\n" + "=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)
    print(df.describe())
    print("\nStatistics Module Executed Successfully.")

if __name__ == "__main__":
    statistics_module()