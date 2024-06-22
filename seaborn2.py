import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

d =sns.load_dataset("diamonds")
sns.distplot(d['price'],bins =10,color='purple')
plt.grid()
plt.show()

sns.jointplot(x='clarity',y = 'depth',data =d,color ="olive")
plt.plot()
plt.show()


