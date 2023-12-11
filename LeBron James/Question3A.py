import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
all_seasons_df = pd.read_csv(r'C:\Users\jecroisp\Documents\NBA_Performance_Predictor\Data\all_seasons.csv')

# Filtering the dataset for LeBron James
lebron_data = all_seasons_df[all_seasons_df['player_name'] == 'LeBron James']

# Sorting the data based on the 'season' to maintain chronological order
lebron_data = lebron_data.sort_values('season')

# Plotting LeBron's regular season performance over time
plt.figure(figsize=(14, 7))
plt.plot(lebron_data['season'], lebron_data['pts'], marker='o', label='Points Per Game')
plt.plot(lebron_data['season'], lebron_data['ast'], marker='s', label='Assists Per Game')
plt.plot(lebron_data['season'], lebron_data['reb'], marker='^', label='Rebounds Per Game')

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.xlabel('Season')
plt.ylabel('Performance Metrics')
plt.title('LeBron James\'s Regular Season Performance Over Seasons')
plt.legend()
plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping of xlabel
plt.show()
