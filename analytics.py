#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#create data frame from dictionary
df = pd.DataFrame({'Name': ['Olga', 'Maks', 'Slava'], 'Age': [22, 34, 45]})
#print df head
print(df.head())
sns.barplot(data=df, x='Name', y='Age')
plt.show()
