import pandas as pd


pl_data = pd.read_csv("../E0.csv")

home_team_goals = pl_data.groupby('HomeTeam').agg(
    gole=('FTHG', 'sum')
).sort_values('gole', ascending=False)

pl_data['total_goals'] = pl_data['FTHG'] + pl_data['FTAG']

mean_goals = pl_data.groupby('HomeTeam').agg(
    srednia_goli=('total_goals', 'mean')
).sort_values('srednia_goli', ascending=False)

print(mean_goals)