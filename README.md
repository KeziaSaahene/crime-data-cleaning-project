Crime Data Cleaning Project
This project involves cleaning and preprocessing a dataset of crime reports from a CSV file. The dataset contains details about various crime incidents, such as crime type, date and time of the event, neighborhood, and reporting area. The goal is to prepare the data for further analysis, such as exploratory data analysis (EDA) and visualization.

Dataset
The dataset is provided in the form of a CSV file named Crime_Reports_20240701.csv and includes the following columns:

Crime Date Time: The date and time the crime occurred.
Date of Report: The date and time when the crime report was filed.
Crime: The type of crime reported.
Reporting Area: The area where the crime was reported.
Neighborhood: The neighborhood where the crime occurred.
Location: A description of the location of the crime.
Steps Taken
1. Data Exploration
Displayed the first few rows of the data using head().
Generated basic descriptive statistics using describe().
2. Data Cleaning
Checked for missing values using isna().sum() and handled missing data in the following ways:
Dropped rows with missing Crime Date Time.
Filled missing Reporting Area with the median value.
Filled missing Neighborhood with "Unknown".
Filled missing Location with "Unknown Location".
3. Data Type Corrections
Converted the Crime Date Time column to a datetime format and extracted the start time.
Converted the Date of Report column to a datetime format.
Changed the Crime, Reporting Area, and Neighborhood columns to categorical data types for better efficiency and easier analysis.
4. Duplicate Rows
Checked for and removed any duplicate rows using duplicated().sum().
5. Exporting Cleaned Data
Saved the cleaned and processed data to a new CSV file: processed_crime_data.csv.
Tools & Libraries
Pandas: Used for data manipulation and cleaning.
Matplotlib & Seaborn: Potential libraries for data visualization (though not yet used in this script, they are often used for further analysis).
Python: Programming language used for the project.
How to Use
Clone or download this repository.
Place the dataset Crime_Reports_20240701.csv in the same directory as the script.
Run the Python script to clean the data.
The cleaned dataset will be saved as processed_crime_data.csv.
Future Work
Conduct further exploratory data analysis (EDA) on the cleaned dataset.
Visualize crime trends over time, by neighborhood, and by crime type.
Apply machine learning techniques to predict crime occurrences or identify patterns in crime data.
