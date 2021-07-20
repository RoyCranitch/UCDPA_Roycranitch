import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
nba = pd.read_csv('nba_extra.csv')
#print(nba.head(15))

#print(nba.columns)

#print(nba.values)

#print(nba.sort_values(['Player', 'PTS']))

top_scorers = nba[nba['PTS'] > 1800]
print(top_scorers)

sns.set_theme(style='whitegrid')
ax = sns.barplot(x='Player', y='PTS', data=top_scorers, alpha=.6)
ax.set_ylabel('Total Points Scored')
ax.set_title("Season Top Scorers")
plt.xticks(rotation=45)
ax.despine(left=True)
plt.show()



#print(nba[nba['PTS'] > 1500])


# Average Points per Game = total points divided by total games played.

#print(nba['Player'] + nba['PTS'] > 1500)