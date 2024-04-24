import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D
import math
# Q (7)(a) 
# #  entropy of fair coin will be summation of(p(x)*log(1/p(x)))
# # probability of head=1/2 and tail is 1/2
# # entropy=0.5*log(2)+0.5(log(2))
# entropy_fair=math.log2(2)
# print(f"Entropy of fair coin is {entropy_fair}")

# #  calculating the entropy of biased coin 
xvalues=np.linspace(0.00000001,0.99999999,1000)
yvalues=-(xvalues*np.log2(xvalues)+(1-xvalues)*np.log2(1-xvalues))
fig=plt.figure(figsize=(10,6))
plt.title("Entropy Vs probability of head")
plt.xlabel("probability of head")
plt.ylabel("Entropy")
plt.plot(xvalues,yvalues,label="Entropy vs head probability")
plt.legend()
plt.show()

# Q (7)(b)
#  gaussian distribution
def gauss_distribution(x,mu1,sigma1):
    return (1/(sigma1*np.sqrt(2*np.pi)))*np.exp(-0.5*(((x-mu1)/sigma1)**2))

def kl_divergence(p,q):
    return np.sum(p*np.log2(p/q))

def cross_entropy(p,q):
    return -1*np.sum(p*np.log2(q))

def plot_gauss(mu1,sigma1,mu2,sigma2):
    xvalues=np.linspace(min(mu1-3*sigma1,mu2-3*sigma2),max(mu1+3*sigma1,mu2+3*sigma2),3000)
    yvalues1=gauss_distribution(xvalues,mu1,sigma1)
    yvalues2=gauss_distribution(xvalues,mu2,sigma2)
    kl12=kl_divergence(yvalues1,yvalues2)
    kl21=kl_divergence(yvalues2,yvalues1)
    cross1=cross_entropy(yvalues1,yvalues2)
    cross2=cross_entropy(yvalues2,yvalues1)
    print(f"KL divergenve D(g1||g2) = {kl12}")
    print(f"KL divergenve D(g2||g1) = {kl21}")
    print(f"Cross Entropy CE(g1,g2) = {cross1}")
    print(f"Cross Entropy CE(g2,g1) = {cross2}")
    fig=plt.figure(figsize=(10,6))
    plt.title("Gaussian Distribution")
    plt.xlabel("X")
    plt.ylabel("Probability Density")
    plt.plot(xvalues,yvalues1)
    plt.plot(xvalues,yvalues2)
    plt.show()

plot_gauss(1,0.6,1.4,0.6)


# Q (7)(b)(i)
# overlap each other
print("\n Values when distribution overlaps \n")
plot_gauss(1,1,1,1)
print("\n Values when distribution partially overlap \n")
plot_gauss(1,0.5,3,0.9)
print("\n Values when distribution do not overlap \n")
plot_gauss(1,0.2,6,0.5)