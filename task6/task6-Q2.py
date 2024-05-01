import numpy as np
import math
import matplotlib.pyplot as plt 
import scipy.stats as scis

#  Q-8 (a)(i)
def generate_uniform():
    np.random.seed(2)
    return np.random.rand(1000)

def uniform_plot(xvalues):
    fig=plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    plt.title('histogram')
    plt.xlabel('samples')
    plt.hist(xvalues,bins=25,ec="black",hatch="*")
    plt.subplot(1,2,2)
    plt.title('pdf of uniform distribution')
    plt.xlabel('X')
    xlist=[i for i in range(20)]
    ylist=[1]*20
    plt.plot(xlist,ylist,color="orange")
    plt.show()

# Q (8)(ii)
def generate_normal(xvalues):
    normal_no=scis.norm.ppf(xvalues)
    return normal_no

def normal_plot(xvalues):
    normal_no=generate_normal(xvalues)
    fig=plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    plt.title('histogram')
    plt.xlabel('samples')
    plt.hist(normal_no,bins=25,ec="black",hatch="*")

    xlist=np.linspace(-3,3,1000)
    pdf_values=(1/np.sqrt(2*np.pi))*(np.exp(-0.5*(xlist**2)))
    plt.subplot(1,2,2)
    plt.title('pdf of normal distribution')
    plt.xlabel('X')
    plt.plot(xlist,pdf_values,color="orange")
    plt.show()


def trun_exp(b,param):
    xxvalues=np.random.uniform(0,1,1000)
    yvalues=-np.log(abs(1-xxvalues*(1-np.exp(-b*param))))/param
    return yvalues

def trun_exp_plot(b,param):
    yvalues=trun_exp(b,param)
    fig=plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    plt.title('histogram')
    plt.xlabel('samples')
    plt.hist(yvalues,bins=25,ec="black",hatch="*")
    xvalueslist=np.linspace(0,b,1000)
    yvalueslist=(param*np.exp(-param*xvalueslist))/(1-np.exp(-param*b))    
    plt.subplot(1,2,2)
    plt.title('pdf of truncated exponential plot')
    plt.xlabel('X')
    plt.plot(xvalueslist,yvalueslist,color="orange")
    plt.show()


xvalues=generate_uniform()

#  uncomment this three lines below to plot the three graphs of uniform plot , normal plot and trun_exp_plot 
uniform_plot(xvalues)
normal_plot(xvalues)
trun_exp_plot(5,1)

def given_f():
    xvalues=np.random.uniform(0,1,1000)
    yvalues=(np.sqrt(160*xvalues+9)-3)/2
    fig=plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    plt.title('histogram')
    plt.xlabel('samples')
    plt.hist(yvalues,bins=25,ec="black",hatch="*")
    xlist=np.linspace(0,5,1000)
    ylist=(2*xlist+3)/40
    plt.subplot(1,2,2)
    plt.title('')
    plt.xlabel('X')
    plt.plot(xlist,ylist,color="orange")
    plt.show()


# Q (8)(b)

# f =(1/40)*(2x + 3), 0 < x < 5 
 
given_f() 
