#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#create data frame from dictionary
df = pd.DataFrame({'Name': ['Olena', 'Maks', 'Slava'], 'Age': [22, 34, 45]})
df.describe()
#print df head
#print(df.head())
sns.barplot(data=df, x='Name', y='Age')
plt.show()
