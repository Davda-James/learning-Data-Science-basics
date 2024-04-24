import numpy as np
import matplotlib.pyplot as plt


# a
 
'''
# probability of incandescent bulb being defective is 0.1
# probability of LED bulbs being defective is 0.05
# Total incandescent bulbs = 2
# total LED bulbs =3
# let say we assign random variable X be total no of incadescence bulbs picked and Y be no of defective bulbs
#  Choices for X=0,1,2 and Y=0,1,2
# possibility is P(X=0,Y=0) = 0.27075 
#                P(X=0,Y=1) = 0.0285
#                P(X=0,Y=2) = 0.00075
#                P(X=1,Y=0) = 0.513
#                P(X=1,Y=1) = 0.084
#                P(X=1,Y=2) = 0.003
                 P(X=2,Y=0) = 0.081
                 P(X=2,Y=1) = 0.018
                 P(X=2,Y=2) = 0.001
'''

prob=[0.27075,0.0285,0.00075,0.513,0.084,0.003,0.081,0.018,0.001]
X=[0,0,0,1,1,1,2,2,2]
Y=[0,1,2,0,1,2,0,1,2]
ax=plt.axes(projection="3d")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Joint Probability")
ax.scatter(X,Y,prob,linewidth=0.1,label="Joint probability X,Y")
plt.show()

# print(0.27075+0.513+0.081)
# b
'''
# marginal probability of X
marginal probability of P(x)= 0.3      x=0 
                            = 0.6      x=1
                            = 0.1      x=2

# marginal probability of Y
marginal probbility of P(y)= 0.86475   y=0
                           = 0.1305    y=1
                           = 0.00475   y=2              
                               
'''

# c
xval=[0,1,2]
margx=[0.3,0.6,0.1]
plt.title("Marginal of X without replacement")
plt.xlabel("X")
plt.ylabel("Probability of X")
plt.scatter(xval,margx,color="red")
plt.bar(xval,margx,width=0.01,color="blue")
plt.show()



# d
'''
    P(Y=1 | first is incadescence) = P(Y=1 & first is incadescent)/P(first is incadescent)
                                    = 0.15
'''


# e
'''
    No X and Y are not independent as 
    P(X=0 & Y=0) = 0.27075 and P(X=0)=0.3 and P(Y=0)=0.86475
    and 0.27075 != 0.3*0.86475

'''

# f
'''
                 P(X=0,Y=0) = 0.324 
#                P(X=0,Y=1) = 0.0342
#                P(X=0,Y=2) = 0.0018
#                P(X=1,Y=0) = 0.4104
#                P(X=1,Y=1) = 0.0672
#                P(X=1,Y=2) = 0.0024
#                P(X=2,Y=0) = 0.1296
#                P(X=2,Y=1) = 0.0288
#                P(X=2,Y=2) = 0.0016
'''




# g
'''
    pmf of x   P(x) =   0.36     x=0
               P(x) =   0.48     x=1
               P(x) =   0.16     x=2
               
        with replacement
'''
newxval=[0,1,2]
newmargx=[0.36,0.48,0.16]
plt.title("Marginal of X with replacement")
plt.xlabel("X")
plt.ylabel("Probability of X")
plt.scatter(newxval,newmargx,color="red")
plt.bar(newxval,newmargx,width=0.01,color="blue")
plt.show()

