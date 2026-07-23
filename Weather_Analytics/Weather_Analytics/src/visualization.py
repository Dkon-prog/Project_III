import matplotlib.pyplot as plt
from utilities import load_cleaned_data, prepare_data
from flood_analysis import add_flood_risk

# Load dataset and prepare data for plotting
def load_dataset():
    df = load_cleaned_data()
    if df is not None:
        df = prepare_data(df)
        df = add_flood_risk(df)
    return df

df = load_dataset()

# Plot monthly average rainfall line graph
def plot_line_graph():
    month_order = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]
    rainfall = (
        df.groupby("Month")["Rainfall"]
        .mean()
        .reindex(month_order)
    )
    plt.figure(figsize=(10,5))
    plt.plot(
        rainfall.index,
        rainfall.values,
        marker="o",
        linewidth=2,
        label="Average Rainfall"
    )
    plt.title("Monthly Average Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../figures/rainfall_trend.png")
    plt.close()

# Plot temperature distribution histogram
def plot_histogram():
    plt.figure(figsize=(8,5))
    plt.hist(
        df["Maximum_Temperature"],
        bins=10,
        edgecolor="black"
    )
    plt.title("Maximum Temperature Distribution")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("../figures/temperature_histogram.png")
    plt.close()

# Plot rainfall vs river level scatter plot
def plot_scatter_plot():
    plt.figure(figsize=(8,5))
    plt.scatter(
        df["Rainfall"],
        df["River_Level"],
        alpha=0.7,
        marker="o",
        label="Weather Data"
    )
    plt.title("Rainfall vs River Level")
    plt.xlabel("Rainfall (mm)")
    plt.ylabel("River Level (m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../figures/rainfall_vs_river_level.png")
    plt.close()

# Plot district wise average rainfall bar chart
def plot_bar_chart():
    district_rainfall = (
        df.groupby("District")["Rainfall"]
        .mean()
        .sort_values(ascending=False)
    )
    plt.figure(figsize=(10,5))
    plt.bar(
        district_rainfall.index,
        district_rainfall.values,
        label="Average Rainfall"
    )
    plt.title("District Wise Average Rainfall")
    plt.xlabel("District")
    plt.ylabel("Average Rainfall (mm)")
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../figures/district_rainfall.png")
    plt.close()

# Plot rainfall box plot
def plot_box_plot():
    plt.figure(figsize=(8,5))
    plt.boxplot(
        df["Rainfall"],
        patch_artist=True,
        label=["Rainfall"]
    )
    plt.title("Rainfall Box Plot")
    plt.ylabel("Rainfall (mm)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../figures/flood_risk_distribution.png")
    plt.close()

# Main function to generate all graphs
def main():
    print("\n====================================")
    print("       VISUALIZATION MODULE")
    print("====================================")
    
    print("\nGenerating Line Graph...")
    plot_line_graph()
    
    print("Generating Histogram...")
    plot_histogram()
    
    print("Generating Scatter Plot...")
    plot_scatter_plot()
    
    print("Generating Bar Chart...")
    plot_bar_chart()
    
    print("Generating Flood Risk Distribution...")
    plot_box_plot()
    
    print("\n====================================")
    print("All graphs generated successfully.")
    print("Graphs are saved in the figures folder.")
    print("====================================")

if __name__ == "__main__":
    main()