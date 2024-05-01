# here we can use complement of probability that we have to find 
# It is given that we have to find the probability such that at least one pair among all has same birthday 
# The above probability will be same as 1-probability such that no one has same birthday
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def find_prob(k):
    val=1
    for i in range(1,k+1):
        val*=(366-k)/(365)
    return 1-val
k=int(input("enter no of people :"))
ans=find_prob(k)
ans=format(ans,".4f")
print(f"proability that at least one pair has same birthday is {ans}")
vect_fun=np.vectorize(find_prob)
x=[i for i in range(2,101)]
y=vect_fun(x)
plt.xlabel("Values of x .......")
plt.ylabel("Values of y .......")
plt.title("Plot of probability vs No of people")
plt.grid(True)
plt.plot(x,y)
plt.show()
