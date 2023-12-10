import pandas as pd

# Load the data from the CSV file
file_path = 'C:/Users/jecroisp/OneDrive - Wentworth Institute of Technology/Documents/NBA_Performance_Predictor/all_seasons.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure and contents
data.head()
