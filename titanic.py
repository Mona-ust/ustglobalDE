import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#df=pd.read_csv("titanic - titanic.csv")
#print(df.columns)
#titanic = sns.load_dataset('titanic')
#print(titanic)
''' Seaborn to create a visualization of the Titanic dataset.
The visualization should show the relationship between the passenger 's age and survival.
(Scatterplot)
'''
#sns.scatterplot(data=titanic, x='age', y='survived', hue='survived', palette={0: 'red', 1: 'green'})
#plt.title('Relationship between Age and Survival on the Titanic')
#plt.xlabel('Age')
#plt.ylabel('Survived')
#plt.legend(title='Survived')
#plt.grid(False)
#plt.show()

'''
Try using a different type of plot, such as a line plot or a bar chart.
'''


titanic = sns.load_dataset('titanic')

titanic = titanic.dropna(subset=['age'])

range = [0, 10, 20, 30, 40, 50, 60, 70, 80]
titanic['age_range'] = pd.cut(titanic['age'], range)
age_survival = titanic.groupby('age_range')['survived'].mean().reset_index()

# Ploting the data
plt.figure(figsize=(12, 6))
sns.barplot(data=age_survival, x='age_range', y='survived')

# Customize the plot
plt.title('Survival Rate by Age Group on the Titanic')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)
plt.xticks(rotation=45)
#plt.grid(axis='y')
plt.show()



'''
# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Drop rows with missing age values
titanic = titanic.dropna(subset=['age'])

# Create age bins
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
titanic['age_bin'] = pd.cut(titanic['age'], bins)

# Calculate survival rates for each bin
age_survival = titanic.groupby('age_bin')['survived'].mean().reset_index()

# Convert 'age_bin' to string to make plotting easier
age_survival['age_bin'] = age_survival['age_bin'].astype(str)

# Create a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=age_survival, x='age_bin', y='survived', marker='o', color='b')

# Customize the plot
plt.title('Survival Rate by Age Group on the Titanic')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)
plt.grid(True)
plt.show()
'''

'''
Try adding additional variables to the plot, such as the passenger's class or gender.
'''






'''
Try using
different
colors or shapes
to
represent
the
different
values
of
the
variables.
'''

'''·
Try
adding
a
legend
to
the
plot.
'''


'''Try
saving
the
plot
to
a
file.
'''