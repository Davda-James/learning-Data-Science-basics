# # here we have to find cdf and pdf of given data and random variable 
# # here random variable is the buzzing of lier machine and probability corresponding to it is no of students for which the buzzer
# # sirens for X times / total no of students that are examined
# # let make the X list for storing random variables and no of students
import matplotlib.pyplot as plt 
import numpy as np
import random
X=[i for i in range(6)]
# x=X+X
# # x.sort()
Y=[2,11,23,9,4,1]
n=50
# # for probability density function we will make list fx
fx=[Y[i]/n for i in range(len(Y))]
mean=[X[i]*fx[i] for i in range(6)]
# now find the cdf
F=np.cumsum(fx)
# plt.xtitle("X", fontsize=16)
# plt.ytitle("fX(x)",fontsize=16)
fig, axs = plt.subplots(1,2, figsize=(13,6), facecolor='dimgrey')
# First subplot
axs[0].set_title("X vs f(x)", color='white')
axs[0].scatter(X, fx,color='red')  
axs[0].bar(X,fx,color="darkblue",width=0.05)
axs[0].set_facecolor('darkgray')
axs[0].set_xlabel("X Values",color='black',fontsize=16)
axs[0].set_ylabel("PDF",color='black',fontsize=16)
axs[0].set_xticks(X)
axs[0].tick_params(axis='x', colors='white')
axs[0].set_yticks(np.arange(0,0.5,0.05))
axs[0].tick_params(axis='y', colors='white')
axs[0].grid(True, color='black')

# Second subplot
axs[1].set_title("X vs F(x)", color='white')
plt.plot(X, F, marker='o', color='darkblue', drawstyle='steps-post')
axs[1].set_facecolor('darkgray')
axs[1].set_xlabel("X Values",color='black',fontsize=16)
axs[1].set_ylabel("CDF",color='black',fontsize=16)
axs[1].set_xticks(X)
axs[1].tick_params(axis='x', colors='white')
axs[1].tick_params(axis='y', colors='white')
axs[1].grid(True, color='black')

# axs[2].set_title("Third Subplot", color='white')
# axs[2].plot(fx,F,color='darkblue')
# axs[2].set_facecolor('darkgray')
# axs[2].tick_params(axis='x', colors='white')
# axs[2].tick_params(axis='y', colors='white')
# axs[2].grid(True, color='black')
# Adjust layout
plt.tight_layout()
plt.show()


# b.
def calculatetheoretical(data,n):
    mean=sum(data)/n
    val=0
    for i in data:
        val+=abs(i-mean)**2
    val=val/n
    return mean,val
    
# Simulate the experiment for different values of n
for n in [50, 500, 5000]:
    exp_mean=[]
    exp_std=[]
    for i in range(1000):
        simulated_X = np.random.choice(X, size=n, p=fx)
        simulated_mean = np.mean(simulated_X)
        simulated_std_dev = np.std(simulated_X)
        exp_mean.append(simulated_mean)
        exp_std.append(simulated_std_dev)
    mean=format(sum(exp_mean)/1000,".4f")
    std=format(sum(exp_std)/1000,".4f")
    theoretical_mean,theoretical_std=calculatetheoretical(simulated_X,n)
    theoretical_mean=format(theoretical_mean,".4f")
    theoretical_std=format(theoretical_std,".4f")
    print(f"For n = {n} :")
    print(f"Theoretical mean is {theoretical_mean} , experimental mean is {mean}")
    print(f"Theretical std is {theoretical_std} , experiental mean is {std}")


# c.
selected_n=50
l=[]
for i in range(1000):
    data=np.random.choice(X,size=selected_n,p=fx)
    mean=np.mean(data)
    l.append(mean)
plt.title("Sample Means")
plt.xlabel("Means")
plt.ylabel("Occurences")
plt.hist(l,color='blue',bins=30,linewidth=0.2,alpha=0.5,ec='black',label="Sample Means Histogram")
plt.grid(True,color="lightgray")
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

print("Mean of sample means is ",format(np.mean(l),".4f"))
print("Standard Deviation of sample means is ",format(np.std(l),".4f"))


'''
    The graph appears like that of normal distribution graph somewhat bell shaped
    Yes the sample mean is a random variable with its own distriution whose graph is seen above.
'''