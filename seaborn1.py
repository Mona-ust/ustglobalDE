#seaborn is powerfull python datavisualization library that is built on of matplotlib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.data import tips


'''
#print(sns.get_dataset_names())
tips = sns.load_dataset('tips')
print(tips.head())
iris = sns.load_dataset('iris')
print(iris.head())
gap=px.data.gapminder()
print(gap)

sns.relplot(data=tips,x="total_bill",y="tip",kind="scatter")
plt.title("Total bill vs Tip")
plt.show()

'''

gap=px.data.gapminder()
india=gap[(gap['country']== 'India')]
sns.relplot(data=gap,y="lifeExp",x="year",kind="line")
plt.title("YoY life  Expectancy of India")
#sns.displot(data=gap, x="tip",kind="hist")
#sns.histplot(data=gap,x="tip",hue="sex")
plt.show()