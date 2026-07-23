import pandas as pd

# Load the cleaned dataset
def load_cleaned_data():
    try:
        df = pd.read_csv("../data/cleaned_data.csv")
        print("\nCleaned Dataset Loaded Successfully.")
        return df
    except FileNotFoundError:
        print("\nError: cleaned_data.csv not found.")
        return None

# Prepare date, month and season columns
def prepare_data(df):
    if df is None:
        return None
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month_name()
    
    # Season dictionary to map month numbers
    season = {
        12: "Winter",
        1: "Winter",
        2: "Winter",
        3: "Summer",
        4: "Summer",
        5: "Summer",
        6: "Monsoon",
        7: "Monsoon",
        8: "Monsoon",
        9: "Monsoon",
        10: "Post-Monsoon",
        11: "Post-Monsoon"
    }
    df["Season"] = df["Date"].dt.month.map(season)
    return df

# Print main heading
def print_heading(title):
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)

# Print sub heading
def print_subheading(title):
    print("\n" + "-" * 40)
    print(title)
    print("-" * 40)

# Format number to two decimal places
def format_number(value):
    try:
        return round(float(value), 2)
    except:
        return value

# Pause execution
def pause():
    input("\nPress Enter to Continue...")

# Main function for testing
def main():
    print_heading("Utilities Module")
    df = load_cleaned_data()
    if df is not None:
        df = prepare_data(df)
        print("\nDataset Shape :", df.shape)
        print("\nColumns Available:")
        print(df.columns)
        print("\nUtilities Module Executed Successfully.")

if __name__ == "__main__":
    main()