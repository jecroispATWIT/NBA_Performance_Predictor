import pandas as pd

# Load the dataset
file_path = r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\all_seasons.csv'
player_performance = pd.read_csv(file_path)


player_performance['season'] = player_performance['season'].astype(str)


# Convert 'pts', 'ast', 'reb' to numeric, coercing errors and filling NaNs with zeros
player_performance['pts'] = pd.to_numeric(player_performance['pts'], errors='coerce').fillna(0)
player_performance['ast'] = pd.to_numeric(player_performance['ast'], errors='coerce').fillna(0)
player_performance['reb'] = pd.to_numeric(player_performance['reb'], errors='coerce').fillna(0)



# Calculate the performance metric for each season for each player
player_performance['performance_metric'] = (
    player_performance['pts'] +
    player_performance['ast'] +
    player_performance['reb']
)

# Get the first and last season for each player based on the 'season' column
player_performance['season'] = player_performance['season'].str[-2:].astype(int)
first_season = player_performance.groupby('player_name')['season'].min().reset_index()
last_season = player_performance.groupby('player_name')['season'].max().reset_index()

# Merge the first and last season with the player_performance dataframe to get their respective metrics
first_season = first_season.merge(player_performance, on=['player_name', 'season'], how='left')
last_season = last_season.merge(player_performance, on=['player_name', 'season'], how='left')

# Calculate the difference in performance metric to determine improvement
first_season.rename(columns={'performance_metric': 'first_season_metric'}, inplace=True)
last_season.rename(columns={'performance_metric': 'last_season_metric'}, inplace=True)
improvement = last_season[['player_name', 'last_season_metric']].set_index('player_name') - first_season[['player_name', 'first_season_metric']].set_index('player_name')
improvement = improvement.reset_index()
improvement['improvement'] = improvement['last_season_metric'] - improvement['first_season_metric']

# Sort the players based on improvement
improvement = improvement.sort_values(by='improvement', ascending=False)

# Display the top 5 players who have improved the most
improvement.head(5)

#The above code prevents NAN players from interfering with the rersults 

# filter out players who only have one season of data, as we cannot calculate improvement for them
player_season_counts = player_performance['player_name'].value_counts()
multi_season_players = player_season_counts[player_season_counts > 1].index

# Filter the main dataframe to include only these players
player_performance_multi_season = player_performance[player_performance['player_name'].isin(multi_season_players)]

#first and last season's performance metrics for these players
first_season = player_performance_multi_season.groupby('player_name').nth(0).reset_index()  # First season stats
last_season = player_performance_multi_season.groupby('player_name').nth(-1).reset_index()  # Last season stats

# Calculate the improvement for each player
first_season.set_index('player_name', inplace=True)
last_season.set_index('player_name', inplace=True)

# subtract the first season's performance metric from the last season's to find the improvement
improvement = (last_season['performance_metric'] - first_season['performance_metric']).reset_index()
improvement.columns = ['player_name', 'improvement']

#drop any NaN values that may result from the subtraction
improvement.dropna(inplace=True)

# sort by improvement to find the players who improved the most
improvement.sort_values(by='improvement', ascending=False, inplace=True)

#let's take a look at the top 5 most improved players
improvement.head(5)

