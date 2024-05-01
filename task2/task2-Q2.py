import math
import numpy as np
import matplotlib.pyplot as plt
def func(n):
    return  math.factorial(n)/(math.sqrt(2*math.pi*n)*pow(n/math.e,n))
vect_fun=np.vectorize(func)
x=[i for i in range(1,21)]
y=vect_fun(x)
plt.title("Ratio of factorial and Stirling formula")
plt.xlabel("Values of n")
plt.ylabel("Values of ratio")
plt.plot(x,y)
plt.show()