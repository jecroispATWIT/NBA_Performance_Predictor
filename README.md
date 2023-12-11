# NBA_Performance_Predictor
Description:
This repository hosts a comprehensive data science project focused on predicting the future performance of NBA players. Utilizing advanced statistical analysis and machine learning techniques, this project explores various factors that influence player performance. The repository contains datasets, code, and detailed documentation, providing insights into player performance trends and predictive modeling in basketball.

# Methodologies:
Use mean and standard deviation to understand the general trends and characteristics of the players.
Apply correlation techniques to explore the relationship between individual player stats.
Use regression models to analyze how players' performance metrics evolve across their career spans.
Implement predictive models, like logistic regression, to forecast players' performance in playoff games based on regular season data.
Employ methods like PCA to identify the most influential variables affecting player performance.


# Tools Used:
Python (NumPy, Pandas, Matplotlib, SciKit Learn)
Jupyter Notebooks
Data from Kaggle Dataset. [https://www.kaggle.com/datasets/justinas/nba-players-data]

# Objective:
To offer data-driven insights and predictive models that help understand and forecast NBA player performance, enhancing strategic decisions in team management and player assessment.

# Questions:
How do individual player statistics (such as points per game, assists, and rebounds) compare to other players?
What is the relationship between a player's experience (number of seasons played) and performance metrics over time?
Can machine learning models using player stats from the regular season accurately predict playoff performance and outcomes?

# Results: 
Question 1: How do individual player statistics (such as points per game, assists, and rebounds) compare to other players?
- I calculated the weighted player productivity score for each player based on a combination of key individual player statistics, and this score provides a comprehensive  measure of their overall impact on the game. Here's the evidence and analysis based on this data:
	
- Weighted Player Productivity Score: We assigned weights to various statistical categories, with points per game (pts_per_game) having the highest weight (0.4) and other categories receiving weights accordingly. This allowed us to calculate a single score that represents the overall productivity of each player.
		[Corrolation Matrix](Images/289400742-d765b848-e496-467e-8d74-b3195b8b4d2e.png)
	
- Comparison of Player Productivity: By comparing these weighted productivity scores across all players, we can objectively assess their relative impact on the game. Players with higher scores are deemed to have a more significant overall influence based on their performance in various statistical categories.

	 |   Rank   |     First      |         Last          | Weighted Productivity Score |
	|:--------:|:--------------:|:---------------------:|:---------------------------:|
	|   1      |      Shai      | Gilgeous-Alexander    |           251.350           |
	|   2      |    Stephen     |        Curry          |           248.051           |
	|   3      |     Kevin      |        Durant         |           246.512           |
	|   4      |     Larry      |         Bird          |           242.624           |
	|   5      |      Trae      |         Young         |           242.460           |
	|   6      |     Nikola     |         Jokic         |           242.380           |
	|   7      |      Dale      |         Ellis         |           242.220           |
	|   8      |     James      |        Harden         |           241.929           |
	|   9      | Karl-Anthony   |         Towns         |           241.647           |
	|   10     |      Kiki      |      Vandeweghe       |           239.880           |
- LeBron James: While LeBron James may not have the highest weighted productivity score in our analysis, it's important to consider additional factors. LeBron's versatility, leadership, longevity, and team success contribute to his status as an all-time great player. He consistently ranks among the top players in terms of productivity and has made a significant impact on his teams, as evidenced by numerous playoff appearances.
	|   First   |   Last   | Weighted Productivity Score | Team Points Per Game | Playoff Appearances | Seasons |
	|:---------:|:--------:|:---------------------------:|:--------------------:|:-------------------:|:-------:|
	|  LeBron   |  James   |           231.405           |         102.7        |         13          |    19   |



