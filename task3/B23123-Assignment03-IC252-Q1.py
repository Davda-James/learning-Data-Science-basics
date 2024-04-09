
# average cases 1373 cases per day , 57 cases per hour

#  here we can use poisson distribution 
# So CDF is (lambda**k)*e**(-lambda)/k!
# here lambda is equal to 57
import random 
import math
import matplotlib.pyplot as plt
import numpy as np
# a.

# Rate parameter (lambda) for the exponential distribution (average number of cases per hour)
lambda_ = 57  # Converting average cases per hour to rate parameter

samples = np.random.exponential(scale=lambda_, size=1000)

# plotting graph
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, color='blue', edgecolor='black', alpha=0.7, label='Histogram: Exponential Distribution')
plt.title('Probability Density Function of Wait Time for Next Covid-19 Confirmed Case')
plt.xlabel('Wait Time (hours)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()

# from scipy.stats import expon

# Parameters
# mu = 1/57  # Average wait time between confirmed cases in hours
# # Generate x values for plotting
# x = np.linspace(0, 10, 1000)

# # Calculate PDF using exponential distribution function
# pdf = expon.pdf(x, scale=mu)

# # Plot PDF
# plt.plot(x, pdf, label='PDF of Wait Time')
# plt.xlabel('Wait Time (hours)')
# plt.ylabel('Probability Density')
# plt.title('Probability Density Function of Wait Time for Next Covid-19 Confirmed Case')
# plt.legend()
# plt.show()

def calculate(val):
    return math.exp(-val)

# b.    
# convert the rate into minutes i.e 57/60 now convert this into parameter that is 60/57
# waiting time less than equal to 1 includes time from 0 to 1 so  
            # probability for it is :     1-e**(-lambda)
prob=1-calculate(57/60)
print(f"probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute is ",format(prob,".4f"))



# c.

# probability for waiting time between 1 to 2 minutes is CDF(2)-CDF(1) and cdf for this exponential distribution is 
    #             1-e**(-lambda*x)
# that is equal to e**(-2*lambda)-e**(-1*lambda)
prob=calculate(57/60)-calculate(2*57/60)
print(f"probability that waiitng time is in between 1 to 2 minutes is ",format(prob,".4f"))


# d.
# probability that waiting time is more than 2 min is same as 1-P(x<2) or 1- CDF(x<2) =1-e**(-2*lambda)
# hence  probability P(x<2)=e**(-2*60/57)
print(f"probability of waiting time more than 2 min is ",format(calculate(2*57/60),".4f"))


# e. 
# if cases per hour is doubled then lambda changes hence probability will become e**(-lambda)-e**(-2*lambda)
'''as cases per hour is doubled hence new case rate is 114 cases per hour now cconvert into min so
    so 114/60 cases per min and hence new mu=60/114
    so new probability will be equal to 
'''
print("average number of cases per hour doubled, then probability of wait time for the next Covid-19 confirmed case to be between 1 min and 2 min is ",format(calculate(114/60)-calculate(2*114/60),".4f"))