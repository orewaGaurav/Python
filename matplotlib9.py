import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data ={"Party":["BJP",'INC','SP','AITC','DMK','DMK','TDP','JD','SHSUBT','NCPSP'],
       "Won":[240,99,37,29,22,16,12,9,8,7],
       'Leading':[0,0,0,0,0,0,0,0,0,0],
       "Total":[240,99,37,29,22,16,12,9,8,7]}
x =pd.DataFrame(data)
print(x)
ex =[0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
plt.pie(data["Won"],labels=data["Party"],autopct="%1.1f%%",explode =ex)
plt.title("ELECTION RESULT")
plt.legend()
plt.savefig("Election.png",dpi =300)
plt.show()


