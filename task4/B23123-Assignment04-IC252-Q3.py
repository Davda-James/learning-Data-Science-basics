import math
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
from scipy.stats import norm 
from scipy.integrate import quad 
#  let use short alias for normal distribution pdf with mean u and standard deviation std for random variable y as normal(x,u,std)
# ((1/(sigma*root(2*pi)))*e**(-0.5*((x-U)/sigma)**2))
#  professor A has mean of 78 and a standard deviation (σ) of 5 
#  professor B has mean of 85 and a standard deviation (σ) of 3 


# a

#  probability P(X,Y="Easy") =0.3 * 0.5 * (normal(x,78,5) + normal(x,85,3))        |    
#  probability P(X,Y="Medium")=0.5 * 0.5 * (normal(x,78,5) + normal(x,85,3))       |  for  -infinite < x < infinite
#  probability P(X,Y="Hard") =0.2 * 0.5 * (normal(x,78,5) + normal(x,85,3))        |   


# b 
# marginal probability

#  if we find the marignal of Y
'''
# (Y="Easy") = 0.3*(0.5*integral of pdf1 + 0.5*pdf2 from -infinite to infinite which is 1 ) 
            = 0.3
# (Y="Medium") = 0.5*(0.5* integral of pdf1 + 0.5*pdf2 from -infinite to infinite which is 1 ) 
                = 0.5
# (Y="Hard") = 0.2*(0.5*integral of pdf1 + 0.5*pdf2 from -infinite to infinite which is 1 ) 
            = 0.2
'''
# if we find the marginal of X

'''
# marginal of x = P(X,Y="Easy) + P(X,Y="Hard") + P(X,Y="Medium")
                = (pdf1+pdf2) * (0.15 + 0.25 + 0.1)
                = (pdf1+pdf2) *(0.5)           
'''


# c 
#  conditional probability P(X>80 |Y="Easy") = P(X>80 intersection Y="Easy")/Proability(Y="Easy")
# which is equal to 1-0.5*(P(z1<0.4) + P(z2< -5/3))
def normal_pdf1(x):
    return norm.pdf(x,78,5)
def normal_pdf2(x):
    return norm.pdf(x,85,3)
integral1,error1=quad(normal_pdf1,80,np.inf)
integral2,error2=quad(normal_pdf2,80,np.inf)
integral1=float(format(integral1,".4f"))
integral2=float(format(integral2,".4f"))
print(f"probability of X>80 given Y=easy is :{float(format(0.5*(integral1+integral2),".4f")   )}") 

# d 
mu_A=78
std_A=5
mu_B=85
std_B=3
xA=np.linspace(mu_A-std_A*3,mu_A+std_A*3,1000)
yA=(1/(np.sqrt(2*np.pi)*std_A)) * np.exp(-0.5*((xA - mu_A)/std_A)**2)
xB=np.linspace(mu_B-std_B*3,mu_B+std_B*3,1000)
yB=(1/(np.sqrt(2*np.pi)*std_B)) * np.exp(-0.5*((xB - mu_B)/std_B)**2)
plt.title("Probability Density function")
plt.xlabel("X values")
plt.ylabel("Probability")
plt.plot(xA,yA,label="Professor A",color="blue")
plt.plot(xB,yB,label="Professor B",color="red")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()


# e
'''
In this scenario, the probability of a specific difficulty level Y would depend on the expected score X (i.e., which professor the student chooses). For example, if a student chooses Professor A (with a lower mean score), 
 they might be more likely to receive a harder exam compared to if they choose Professor B (with a higher mean score).
'''
