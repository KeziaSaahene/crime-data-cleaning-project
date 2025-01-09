#importing python libraries; pandas, matplotlib and seaborn to begin
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Crime_Reports_20240701.csv')

# exploring the data
print(data.head())
print(data.describe())


#starting the data cleaning process
#checking for missing values in the dataset
print(data.isna().sum())

# some values were found to be missing 
# addressing missing values

# Drop rows with missing 'Crime Date Time' because missing values are few
data = data.dropna(subset=['Crime Date Time'])
print("After dropping rows with missing 'Crime Date Time':")

# filling missing 'Reporting Area' values with the median 
data['Reporting Area'] = data['Reporting Area'].fillna(data['Reporting Area'].median())
print("After filling missing 'Reporting Area':")

# filling missing 'Neighborhood' with "Unknown"
data['Neighborhood'] = data['Neighborhood'].fillna('Unknown')
print("After filling missing 'Neighborhood':")

# filling missing 'Location' with "Unknown Location"
data['Location'] = data['Location'].fillna('Unknown Location')
print("After filling missing 'Location':")

print(data.isna().sum())

#standardizing; ensuring the data types are correct
print(data.dtypes)
 
# converting Crime Date Time to datetime data type
# Extract start times
data['Start Time'] = data['Crime Date Time'].str.extract(r'(.+?) -')[0]

# Convert to datetime
data['Start Time'] = pd.to_datetime(data['Start Time'], format="%m/%d/%Y %H:%M", errors='coerce')


# addressing Date of Report column
# Cconvertimg Date of Report to datetime data type
data['Date of Report'] = pd.to_datetime(data['Date of Report'],  format="%m/%d/%Y %I:%M:%S %p",  # Format for "02/25/2009 07:16:00 AM"errors='coerce'
)

# addressing crime column
#  converting crime to 'category' data type
data['Crime'] = data['Crime'].astype('category')  
print(data['Reporting Area'].head(199))

# addressing Reporting Area column
# Converting 'Reporting Area' to category data type
data['Reporting Area'] = data['Reporting Area'].astype('category')
print(data['Reporting Area'].unique())

# addressing Neighborhood column
# convert Neighborhood to category data type
data['Neighborhood'] = data['Neighborhood'].astype('category')
print(data.dtypes)


# Checking for duplicates
print(f"Duplicate rows: {data.duplicated().sum()}")


# Saving the cleaned and processed data to a new CSV file for further processing 
data.to_csv('processed_crime_data.csv', index=False)
print("Processed data has been saved to 'processed_crime_data.csv'.")
