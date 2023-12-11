import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
all_seasons_df = pd.read_csv(r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\all_seasons.csv')
team_totals_df = pd.read_csv(r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\Team Totals.csv')
team_stats_per_game_df = pd.read_csv(r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\Team Stats Per Game.csv')



relevant_columns = ['pts', 'ast', 'reb', 'pts_playoffs', 'ast_playoffs', 'reb_playoffs']


all_seasons_df['pts_playoffs'] = all_seasons_df['pts'].shift(-1)
all_seasons_df['ast_playoffs'] = all_seasons_df['ast'].shift(-1)
all_seasons_df['reb_playoffs'] = all_seasons_df['reb'].shift(-1)


correlation_matrix = all_seasons_df[relevant_columns].corr()

# Plotting the correlation heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation between Regular Season and Playoff Performance')
plt.show()
