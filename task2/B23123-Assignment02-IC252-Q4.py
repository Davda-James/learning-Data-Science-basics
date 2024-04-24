import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random 
l=[1,2,3,4,5,6]
data={'Sum' : [i for i in range(2,13)], 'Frequency':[0 for i in range(11)]}
res=pd.DataFrame(data)
for i in range(10000):
    ans1=random.choice(l)
    ans2=random.choice(l)
    val=ans1+ans2
    res.loc[res['Sum'] ==val , 'Frequency']+=1
print("the result of only sum and frequency is : \n",res)
res['Probability']=res['Frequency']/10000
print("the result of only sum,frequency and probability is : \n",res)

# plotting the graph of probability vs sum 
plt.title("Probability vs Sum")
plt.xlabel("Sum")
plt.ylabel("Probability in 10,000 trials")
plt.bar(res['Sum'],res['Probability'], edgecolor='black' ,hatch='.')
plt.show()