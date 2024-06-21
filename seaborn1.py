import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# ne1 =sns.load_dataset('titanic')
# print(ne1)

# x = sns.load_dataset('tips')
# print(x)

# y =sns.load_dataset("taxis")
# print(y)

ne =sns.load_dataset('flights')
print(ne)
sns.lineplot(x='year',y = "passengers",data =ne,hue ="month")
plt.show()

plt.figure(figsize=(20,10))
sns.set(style='dark')
sns.barplot(x='month',y='passengers',data = ne)
plt.show()