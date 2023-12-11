# Calculating a 'productivity score' for each player
# Here, we can define productivity as a combination of points, assists, and rebounds per game
# A simple approach could be to take the sum of these three statistics for each player

import pandas as pd

file_path = r"C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\final_data.csv"
data = pd.read_csv(file_path)

data['productivity_score'] = data['pts'] + data['ast'] + data['reb']

# Grouping by player and averaging their productivity score across years
# This gives a more balanced view over their entire career
player_productivity = data.groupby(['first', 'last'])['productivity_score'].mean().reset_index()

#player_productivity = data.groupby(['player_name'])['productivity_score'].mean().reset_index()
# Sorting to find the top 10 and bottom 10 players in terms of productivity
top_10_productive_players = player_productivity.sort_values(by='productivity_score', ascending=False).head(10)
bottom_10_productive_players = player_productivity.sort_values(by='productivity_score').head(10)


# Calculating the weighted productivity score
weights = {
    'pts': 2,       # Higher weight for points per game
    'stl': 1,
    'blk': 1,
    'ast': 1,
    'reb': 1,
    'fg_pct': 1,    # Multiplied by 100 since it's a percentage
    'ft_pct': 1,    # Multiplied by 100 since it's a percentage
    'fg3_pct': 1    # Multiplied by 100 since it's a percentage
}


data['weighted_productivity_score'] = (
    data['pts'] * weights['pts'] +
    data['stl'] * weights['stl'] +
    data['blk'] * weights['blk'] +
    data['ast'] * weights['ast'] +
    data['reb'] * weights['reb'] +
    data['fg_pct'] * 100 * weights['fg_pct'] +
    data['ft_pct'] * 100 * weights['ft_pct'] +
    data['fg3_pct'] * 100 * weights['fg3_pct']
)

# Correlating Team Performance with Player Productivity
# For this analysis, we need to combine the player productivity data with the team stats data.
# We will use the team abbreviation from the player data and match it with the team stats data.
team_stats_data = pd.read_csv(r"C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\Team Stats Per Game.csv")

# First, let's prepare the player productivity data by averaging it across each season for each team.
player_productivity_avg = data.groupby(['team', 'year'])['weighted_productivity_score'].mean().reset_index()

# Renaming columns for clarity
player_productivity_avg.rename(columns={'year': 'season', 'team': 'abbreviation'}, inplace=True)

# Now, let's merge this with the team stats data.
merged_data = pd.merge(team_stats_data, player_productivity_avg, on=['abbreviation', 'season'], how='inner')

# To analyze the correlation, we'll focus on team performance metrics like points per game and playoff appearances.
# Since 'playoffs' is a boolean, we can convert it to numeric for correlation analysis.
merged_data['playoffs_numeric'] = merged_data['playoffs'].astype(int)

# Calculating correlation
correlation_matrix = merged_data[['weighted_productivity_score', 'pts_per_game', 'playoffs_numeric']].corr()



# Grouping by player and averaging their weighted productivity score across years
weighted_player_productivity = data.groupby(['first', 'last'])['weighted_productivity_score'].mean().reset_index()

# Sorting to find the top 10 and bottom 10 players in terms of the weighted productivity score
top_10_weighted_productive_players = weighted_player_productivity.sort_values(by='weighted_productivity_score', ascending=False).head(10)
bottom_10_weighted_productive_players = weighted_player_productivity.sort_values(by='weighted_productivity_score').head(10)

top_10_weighted_productive_players, bottom_10_weighted_productive_players
#correlation_matrix