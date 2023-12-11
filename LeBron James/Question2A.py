import matplotlib.pyplot as plt
import pandas as pd

file_path = r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\all_seasons.csv'
player_performance = pd.read_csv(file_path)

weights = {
    'pts': 2,       # Higher weight for points per game
    'ast': 1,
    'reb': 1,
    'usg_pct': 1,    # Multiplied by 100 since it's a percentage
    'oreb_pct': 1,    # Multiplied by 100 since it's a percentage
    'ast_pct': 1    # Multiplied by 100 since it's a percentage
}

player_performance['performance_metric'] = (
    player_performance['pts'] * weights['pts'] +
    player_performance['ast'] * weights['ast'] +
    player_performance['reb'] * weights['reb'] +
    player_performance['usg_pct'] * 100 * weights['usg_pct'] +
    player_performance['oreb_pct'] * 100 * weights['oreb_pct'] +
    player_performance['ast_pct'] * 100 * weights['ast_pct']
)
selected_data = player_performance[['player_name', 'draft_year', 'season']].copy()

selected_data['draft_year'] = pd.to_numeric(selected_data['draft_year'], errors='coerce')


selected_data.dropna(subset=['draft_year'], inplace=True)


selected_data['draft_year'] = selected_data['draft_year'].astype(int)


selected_data['Start Year'] = selected_data['season'].str.extract(r'(\d{4})').astype(int)

def convert_year(two_digit_year):
    if two_digit_year >= 95:
        return 1900 + two_digit_year
    else:
        return 2000 + two_digit_year

# Ensure 'y' is a Series of integers representing the last two digits of the year
y = selected_data['season'].str.extract(r'-(\d{2})').astype(int).squeeze()

# Apply the 'convert_year' function to each element of 'y'
selected_data['End Year'] = y.apply(convert_year)

player_performance['End Year'] = y.apply(convert_year)

# After calculating 'End Year' and before the subtraction
player_performance['End Year'] = pd.to_numeric(player_performance['End Year'], errors='coerce')
player_performance['draft_year'] = pd.to_numeric(player_performance['draft_year'], errors='coerce')

# drop rows with NaN in either 'End Year' or 'draft_year'
player_performance.dropna(subset=['End Year', 'draft_year'], inplace=True)

# convert both columns to integers
player_performance['End Year'] = player_performance['End Year'].astype(int)
player_performance['draft_year'] = player_performance['draft_year'].astype(int)


player_performance['Seasons Played'] = player_performance['End Year'] - player_performance['draft_year']



player_name = 'LeBron James'
player_data = player_performance[player_performance['player_name'] == player_name].copy()
player_data['Seasons Played'] = player_data['End Year'] - player_data['draft_year']

# create the line chart using the 'player_data' DataFrame
plt.figure(figsize=(10, 6))
plt.plot(player_data['Seasons Played'], player_data['performance_metric'], marker='o', label=player_name)
plt.xlabel('Number of Seasons Played')
plt.ylabel('Performance Metric')
plt.title(f'{player_name}\'s Performance Over Seasons')
plt.legend()
plt.grid(True)
plt.show()