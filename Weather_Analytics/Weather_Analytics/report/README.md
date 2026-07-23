# Weather Analytics Toolkit

## Project Overview
This project is a Weather, Climate, and Flood Monitoring System that we developed in Python to analyze weather data from Assam. Assam gets a lot of rain and has floods every year, so we built this toolkit to help study these weather patterns. Our toolkit loads the weather data, cleans it, and performs various analyses like rainfall analysis, weather analysis, flood risk analysis, and statistical analysis. It also calculates derived quantities, shows flood warnings, predicts the next seven days of rainfall, and saves graphs in a figures folder.

## Project Objectives
The main purpose of this project is to analyze the climate and weather data of Assam to understand weather patterns better. We want to solve problems like finding which months are the hottest or coldest, which districts get the most rain, if river levels go up when it rains, and if we can predict flood risk and rainfall to warn people in advance.

## Features
- Load raw weather data from a CSV file and clean up any missing values.
- Calculate average monthly temperatures and identify hottest and coldest months.
- Calculate total rainfall, monthly average rainfall, and district-wise rainfall.
- Analyze river levels and classify the flood risk for each day.
- Run statistical calculations like mean, median, mode, variance, standard deviation, and correlation.
- Create and save 5 different charts to show trends visually.
- Calculate custom values like daily temperature difference and rainfall category.
- Predict rainfall for the next 7 days using simple moving averages.
- Provide an interactive command-line menu to run everything easily.

## Folder Structure
Here is the folder structure of our project:
```
Weather_Analytics/
│
├── data/
│   ├── assam_weather_data.csv
│   ├── cleaned_data.csv
│   └── monthly_summary.csv
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── weather_analysis.py
│   ├── rainfall_analysis.py
│   ├── flood_analysis.py
│   ├── statistics_module.py
│   ├── visualization.py
│   └── utilities.py
│
├── figures/
│   ├── rainfall_trend.png
│   ├── temperature_histogram.png
│   ├── rainfall_vs_river_level.png
│   ├── district_rainfall.png
│   └── flood_risk_distribution.png
│
├── report/
│   ├── README.md
│   └── presentation.pptx
│
└── requirements.txt
```

## Requirements
We used a few Python libraries for this project. You need to install:
- pandas
- matplotlib

You can install all of them at once by running this command in your terminal:
```bash
pip install -r requirements.txt
```

## How to Run the Project
1. Open your terminal or command prompt.
2. Go to the project directory and navigate to the `src` folder:
   ```bash
   cd Weather_Analytics/src
   ```
3. Run the main script using Python:
   ```bash
   python main.py
   ```
4. A menu will appear on your screen. Type a number from 1 to 11 to choose an option and press Enter.

## Menu Options
- **1. Load and Clean Dataset**: Reads the raw weather data file, removes any row that has missing data, and saves the clean data to a new file.
- **2. Weather Analysis**: Calculates average temperatures for each month, finds the hottest and coldest months, and saves the summary.
- **3. Rainfall Analysis**: Shows total rainfall statistics and displays average rainfall by month, district, and season.
- **4. Flood Analysis**: Displays river level averages, categorizes daily flood risk, and identifies flood-prone days.
- **5. Statistical Analysis**: Prints statistical values (like mean, mode, standard deviation) for temperature, rainfall, and humidity, and shows correlation between variables.
- **6. Derived Quantities**: Shows daily temperature differences, categorizes rainfall levels, and displays monthly averages.
- **7. Visualization**: Generates all 5 charts and saves them as PNG images in the `figures` folder.
- **8. Flood Warning System**: Runs the flood warning module to classify risk levels and saves records to a warning file.
- **9. Seven-Day Prediction**: Predicts rainfall for the next 7 days using moving averages and saves the prediction.
- **10. Run Complete Project**: Runs all the options one after another automatically.
- **11. Exit**: Closes the program.

## Modules Used
All our Python files are in the `src` folder:
- `main.py`: This is the main program file. It displays the menu, takes user input, and runs the other modules.
- `data_loader.py`: Handles loading the raw CSV data, checking for missing values, cleaning them, and saving the cleaned dataset.
- `weather_analysis.py`: Performs temperature calculations, analyzes seasonal averages, and saves monthly statistics.
- `rainfall_analysis.py`: Analyzes rainfall metrics across months, districts, and seasons.
- `flood_analysis.py`: Analyzes river levels, calculates flood risk metrics, and lists flood-prone days.
- `statistics_module.py`: Calculates mathematical values like mean, mode, median, standard deviation, and correlation coefficients.
- `visualization.py`: Creates charts (line graphs, bar charts, histograms, scatter plots, box plots) using matplotlib.
- `utilities.py`: Contains common functions used by other files, like loading cleaned data, print formats, and pausing execution.

## Output Files
The toolkit generates and updates these files inside the `data` folder:
- `cleaned_data.csv`: The clean weather dataset without any empty values.
- `monthly_summary.csv`: Contains the average maximum and minimum temperatures calculated for each month.
- `flood_warning.csv`: Contains the dataset with an added "Flood_Warning" risk level column.
- `seven_day_prediction.csv`: Contains the predicted rainfall values for the next seven days.

## Graphs
The following graphs are generated and saved in the `figures` folder:
- `rainfall_trend.png`: A line graph showing average monthly rainfall trend.
- `temperature_histogram.png`: A histogram displaying how maximum temperatures are distributed.
- `rainfall_vs_river_level.png`: A scatter plot that checks if river levels increase with rainfall.
- `district_rainfall.png`: A bar chart comparing average rainfall across different districts.
- `flood_risk_distribution.png`: A box plot showing the distribution and spread of rainfall.

## Project Requirements
This project fully satisfies the Project III requirements. We used modular programming with separate files, created more than 10 custom functions, used multiple loops, implemented error handling with `try-except` blocks, performed CSV read and write operations, did statistical calculations, mapped derived quantities, implemented a flood risk classification system, generated required charts, and added comments.

## Future Improvements
- Add a graphical user interface (GUI) using Tkinter to make it look nicer than the command-line menu.
- Improve the prediction feature by using advanced machine learning models instead of a simple moving average.
- Add live weather API integration to fetch real-time weather data for Assam districts.
- Send email or SMS alerts automatically when the flood risk becomes severe.
- Add a feature to support importing data from Excel files as well as CSV.

## Authors
- Rakesh Karan Sharma
- Adarsh Dihingia
- Ahia Alam Khan
- Ayush Miri
- Prem Pawe
- Nishita

## License
This project was developed only for educational purposes as part of Project III coursework.
