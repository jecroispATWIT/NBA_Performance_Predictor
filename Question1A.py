# We will use the merged dataset 'merged_data' which contains both individual player productivity scores
# and team performance metrics.
# Ensure you have already loaded the player productivity data and the team performance data.
import pandas as pd

team_stats_data = pd.read_csv(r"C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\Team Stats Per Game.csv")
file_path = r"C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\final_data.csv"
data = pd.read_csv(file_path)


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

# Calculating the weighted productivity score
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

# First, ensure player names are included in the player productivity data.
player_productivity_with_names = data.groupby(['team', 'year', 'first', 'last'])['weighted_productivity_score'].mean().reset_index()

# Prepare the team performance data to include season and team abbreviation.
team_performance_data = team_stats_data[['season', 'abbreviation', 'playoffs', 'pts_per_game']]

# Merge player productivity with team performance data.
# Make sure to merge on both 'team'/'abbreviation' and 'year'/'season' columns.
merged_data= pd.merge(
    player_productivity_with_names, 
    team_performance_data, 
    left_on=['team', 'year'], 
    right_on=['abbreviation', 'season'], 
    how='inner'
)

# The 'merged_data_with_names' DataFrame now contains both individual player productivity scores
# and team performance metrics, with player names included.

# First, let's filter for the players on teams that made it to the playoffs as a proxy for team success.
players_on_playoff_teams = merged_data[merged_data['playoffs'] == True]

# Now, let's find the top players based on their weighted productivity score who were on playoff teams.
top_players_on_playoff_teams = players_on_playoff_teams.sort_values(
    by='weighted_productivity_score', 
    ascending=False
).head(10)[['season', 'abbreviation', 'team', 'first', 'last', 'weighted_productivity_score', 'pts_per_game']]

top_players_on_playoff_teams




# To make a case for LeBron James using the available data, we need to find his entries in the dataset
# and evaluate his performance metrics. Let's extract the data pertaining to LeBron James.

lebron_stats = merged_data[
    (merged_data['first'] == 'LeBron') & 
    (merged_data['last'] == 'James')
].sort_values(by='season', ascending=False)

# Now let's compile the relevant statistics for LeBron James over the seasons.
lebron_career_stats = lebron_stats.groupby(['first', 'last']).agg({
    'weighted_productivity_score': 'mean',  # Average productivity score
    'pts_per_game': 'mean',                 # Average team points per game
    'playoffs': 'sum',                      # Total playoff appearances
    'season': 'count'                       # Number of seasons
}).reset_index()

# Calculating his rank in terms of productivity score among all players.
lebron_rank = player_productivity_with_names.rank(method='max', ascending=False)
lebron_rank = lebron_rank[lebron_rank['first'] == 'LeBron'][lebron_rank['last'] == 'James']

lebron_career_stats, lebron_rank

