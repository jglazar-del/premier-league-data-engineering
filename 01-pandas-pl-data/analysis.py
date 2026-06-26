import pandas as pd


pl_data = pd.read_csv("../E0.csv")

home_team_goals = pl_data.groupby('HomeTeam').agg(
    home_goals_total=('FTHG', 'sum')
).sort_values('home_goals_total', ascending=False).reset_index()

pl_data['total_goals'] = pl_data['FTHG'] + pl_data['FTAG']

mean_goals = pl_data.groupby('HomeTeam').agg(
    home_goals_mean=('total_goals', 'mean')
).sort_values('home_goals_mean', ascending=False).reset_index()

podsumowanie = home_team_goals.merge(mean_goals, on='HomeTeam')

pl_data_total = pl_data.merge(podsumowanie, on='HomeTeam')

print(pl_data_total)