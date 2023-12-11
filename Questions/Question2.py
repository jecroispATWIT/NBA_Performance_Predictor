import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\all_seasons.csv'
player_performance = pd.read_csv(file_path)

# Calculate the performance metric
weights = {
    'pts': 2, 'ast': 1, 'reb': 1,
    'usg_pct': 1, 'oreb_pct': 1, 'ast_pct': 1
}

player_performance['performance_metric'] = (
    player_performance['pts'] * weights['pts'] +
    player_performance['ast'] * weights['ast'] +
    player_performance['reb'] * weights['reb'] +
    player_performance['usg_pct'] * weights['usg_pct'] * 100 +
    player_performance['oreb_pct'] * weights['oreb_pct'] * 100 +
    player_performance['ast_pct'] * weights['ast_pct'] * 100
)

# Preprocess the 'draft_year' and 'season' columns
player_performance['draft_year'] = pd.to_numeric(player_performance['draft_year'], errors='coerce')
player_performance.dropna(subset=['draft_year'], inplace=True)
player_performance['draft_year'] = player_performance['draft_year'].astype(int)

# Function to convert two-digit year to four-digit year
def convert_year(two_digit_year):
    return 1900 + two_digit_year if two_digit_year >= 95 else 2000 + two_digit_year

# Extract the last two digits of the season year and convert to 'End Year'
y = player_performance['season'].str.extract(r'-(\d{2})').astype(int).squeeze()
player_performance['End Year'] = y.apply(convert_year)

# Calculate 'Seasons Played'
player_performance['Seasons Played'] = player_performance['End Year'] - player_performance['draft_year']

# Group by 'Seasons Played' and calculate the average 'performance_metric'
grouped_data = player_performance.groupby('Seasons Played')['performance_metric'].mean().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(grouped_data['Seasons Played'], grouped_data['performance_metric'])
plt.xlabel('Number of Seasons Played')
plt.ylabel('Average Performance Metric')
plt.title('Average Performance Metric Over Number of Seasons Played')
plt.grid(True)
plt.show()
