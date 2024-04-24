import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm
from scipy.integrate import quad
import math

# time to repair an AM radio has µAM = 1 and standard deviation of σAM = 0.5
# time to repair an FM radio has µAM = 1.5 and standard deviation of σAM = 0.75

#  simulation of problem of radio 
mu_am=1
std_am=0.5
mu_fm=1.5
std_fm=0.75
#  defining a normal distribution so that no need to rewrite the formula again and again
def pdfnormal(x,mu,std):
    return 1/(math.sqrt(2*math.pi)*std) * math.exp(-0.5*((x - mu)/std)**2)

# def jointpdf(x,y,mu_am,mu_fm,std_am,std_fm):
#     return 1/(2*math.pi*std_am*std_fm) * math.exp(-0.5*(((x-mu_am)/std_am)**2 + ((y-mu_fm)/std_fm)**2))

# plotting the graph
xA=np.linspace(mu_am-std_am*2,mu_am+std_am*2,100)
xB=np.linspace(mu_fm-std_fm*2,mu_fm+std_fm*2,100)
# y=1/(2*np.pi*std_am*std_fm) * np.exp(-0.5*(((xA - mu_am)/std_am)**2 + ((xB - mu_fm)/std_fm)**2))
X, Y = np.meshgrid(xA, xB)
y=norm.pdf(X,mu_am,std_am)*norm.pdf(Y,mu_fm,std_fm)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y,y, cmap='viridis')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Probability Density')

plt.show()

# ax=plt.axes(projection="3d")
# ax.plot(xA,xB,y)
# plt.show()


# b 
# P(fm<1 | am=2) = P(fm <1 & am=2)/ P(am=2)
def normalfm(x):
    return norm.pdf(x,mu_fm,std_fm)
integral1,error1=quad(normalfm,0,1)

p1=float(format(pdfnormal(2,mu_am,std_am),".4f")) 
'''
as repairing time of fm and am are independent hence 
    P(fm<1 & am=2)  = P(fm<1)* P(am=2)
                    = integral1 * 1/(math.sqrt(2*math.pi)*std_am)) * math.exp(-0.5*((2 - mu_am)/std_am)**2
                    = integral1 * p1
'''
ans=format(integral1*p1,".4f")
print(ans)



# c
np.random.seed(2)
simulated_am=np.random.normal(mu_am,std_am,100)
simulated_fm=np.random.normal(mu_fm,std_fm,100)
total_repair_time=simulated_fm+simulated_am
# print(total_repair_time)



# d
plt.xlabel("Time")
plt.ylabel("Probability")
plt.title("Probability Distribution of Total Repair Time")
plt.hist(total_repair_time,bins=25,ec="black",hatch="//",color="orange",label="Total Repair Time")
plt.grid(True)
plt.legend(loc="upper right")
plt.show()

#  finding mean and std of total repair time we got using simulation
mean_total=np.mean(total_repair_time)
std_total=np.std(total_repair_time)
print(f"mean of total repair time is {format(mean_total,".4f")}")
print(f"std of total repair time is {format(std_total,".4f")}")



# e
''' 
let say Xam as the random variable representing the repair time for an AM radio.
        Xfm as the random variable representing the repair time for an FM radio.
        Tam as the total repair time for AM radio repair (including the ongoing repair).
        Tfm as the total repair time for FM radio repair (including the ongoing repair).
        
        So  Tam=Xam+Yam
            Tfm=Xfm+Yfm
        Now Yam=Tam - Xam
            hence using change of variable formula i.e  fyam(y)=fxam(g(y)) * |g'(y)|
            so here g(y)=Tam-y
            |g'(y)|=1
            hence     
                        fyam(y)=fxam(Tam-y)

            Similarly for fyfm(y)=fxfm(Tfm-y)
'''