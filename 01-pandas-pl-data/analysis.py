import pandas as pd


pl_data = pd.read_csv("../E0.csv")

ht_goals = pl_data.groupby('HomeTeam').agg(
    gole=('FTHG', 'sum')
).sort_values('gole', ascending=False)

print(ht_goals)