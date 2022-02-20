from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

unsold_cost = 0
df = pd.read_csv('/Users/sayanadhikary/IdeaProjects/big_data_projects/source_files/IPL_AUCTION_2013-2022.csv')
# display(df)
df['Indian_price'] = np.where(df['NATIONALITY'] == 'Indian', df['PRICE'], 0)
sum_total = df['PRICE'].sum()
sum_indian = df['Indian_price'].sum()
sum_overseas = sum_total - sum_indian
# display(df)
perc_indian = (1.0 * sum_indian / sum_total ) * 100
perc_overseas = (1.0 * sum_overseas / sum_total ) * 100
display(df)
print('{:.2f} percentage of the total funds is spent on Indian players. {:.2f} percentage of the funds is spent on Overseas players.'.format(perc_indian, perc_overseas))

x = [sum_indian, sum_overseas]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
labels = ['Indians', 'Overseas']
plt.legend(labels,loc=3)

plt.show()