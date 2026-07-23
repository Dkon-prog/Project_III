import pandas as pd


def load_data():
    """
    Reads the Assam weather dataset.
    """

    try:
        df = pd.read_csv("data/assam_weather_data.csv")
        print("\nDataset Loaded Successfully.\n")
        return df
    except (FileNotFoundError, OSError):
        try:
            df = pd.read_csv("../data/assam_weather_data.csv")
            print("\nDataset Loaded Successfully.\n")
            return df
        except (FileNotFoundError, OSError):
            print("\nError: assam_weather_data.csv not found.")
            return None


def display_data(df):
    """
    Displays the first five rows of the dataset.
    """

    if df is None:
        print("Dataset not loaded.")
        return

    print("\n========== FIRST FIVE ROWS ==========\n")
    print(df.head())


def dataset_information(df):
    """
    Displays information about the dataset.
    """

    if df is None:
        print("Dataset not loaded.")
        return

    print("\n========== DATASET INFORMATION ==========\n")
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    lines = buffer.getvalue().split('\n')
    header_idx = -1
    for i, line in enumerate(lines):
        if ' #   Column' in line:
            header_idx = i
            break
    if header_idx != -1:
        dtype_start = lines[header_idx].find('Dtype')
        for i in range(header_idx, len(lines)):
            line = lines[i]
            if i == header_idx or i == header_idx + 1 or (line.strip() and line.startswith(' ')):
                lines[i] = line[:dtype_start].rstrip()
    print('\n'.join(lines))

    print("\n========== COLUMN NAMES ==========\n")
    print(df.columns)

    print("\n========== SHAPE OF DATASET ==========\n")
    print(df.shape)


def check_missing_values(df):
    """
    Displays missing values in each column.
    """

    if df is None:
        print("Dataset not loaded.")
        return

    print("\n========== MISSING VALUES ==========\n")
    print(df.isnull().sum())


def clean_data(df):
    """
    Removes rows containing missing values.
    """

    if df is None:
        print("Dataset not loaded.")
        return None

    rows_before = len(df)

    df = df.dropna()

    rows_after = len(df)

    print("\nMissing values removed successfully.")
    print("Rows Removed :", rows_before - rows_after)
    print("Shape After Cleaning :", df.shape)

    return df


def save_cleaned_data(df):
    """
    Saves the cleaned dataset.
    """

    if df is None:
        print("No cleaned dataset available.")
        return

    try:
        df.to_csv("data/cleaned_data.csv", index=False)
        print("\ncleaned_data.csv created successfully.")
    except (FileNotFoundError, OSError):
        try:
            df.to_csv("../data/cleaned_data.csv", index=False)
            print("\ncleaned_data.csv created successfully.")
        except (FileNotFoundError, OSError):
            print("\nError: Could not save cleaned_data.csv.")


def main():

    df = load_data()

    if df is not None:

        display_data(df)

        dataset_information(df)

        check_missing_values(df)

        df = clean_data(df)

        save_cleaned_data(df)

        print("\nData Loader Module Executed Successfully.")


if __name__ == "__main__":
    main()