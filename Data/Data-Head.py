import pandas as pd

 # Load the data from the CSV file
file_path = r"C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\final_data.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure and content
data.head()
