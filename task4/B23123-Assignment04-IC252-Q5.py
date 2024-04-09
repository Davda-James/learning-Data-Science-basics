import numpy as np
import matplotlib.pyplot as plt

# a
def joint_pdf(x,y):
    if(0<=x<=1 and 1<=y<=2):
        return 1
    else:
        return 0
x_val=np.linspace(0,1.5,200)
y_val=np.linspace(0.5,2.5,200)
vectorpdf=np.vectorize(joint_pdf)(x_val,y_val)
ax=plt.axes(projection="3d")
ax.plot(x_val,y_val,vectorpdf)
plt.show()


# b
def check1(x):
    if(0<=x<1):
        return 1
    else:
        return 0
def check2(y):
    if(1<=y<=2):
        return 1
    else:
        return 0
ans=True
for i in range(len(vectorpdf)):
    if(vectorpdf[i]!=check1(x_val[i])*check2(y_val[i])):
        ans=False
        break
if(ans==False):
    print("Not Independent")
else:
    print("Independent")

# c
    # so P(X>0.5 | Y=1.5) = P(X>0.5 & Y=1.5)/P(Y=1.5)
    # P(X>0.5 | Y=1.5) = 1  

# d
ax2=plt.axes(projection="3d")
xvalues=np.linspace(0,1,20)
yvalues=[1.5 for i in range(20)]
ax2.set_title("Conditional Probability X>0.5 given Y=1.5")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.plot(xvalues,yvalues,1)
plt.show()

# e
'''
        Z= X +Y 
        so 1<=z<=3 and let's break this interval into two 
        one is 1<=z<=2 and other is from 2<z<=3
        for 1<=z<2:
        by transformation formula :
            f(z)= integral(0,z-1) of (fx(x) * fy(y)) =z-1
            and for interval 2<z<=3:
            f(z)= integral(z-2,1) of(fx(x)*fy(y)) = 3-w
            which means final pdf of Z is:

                fZ(z)=   z-1   1<=z<=2
                         3-z   2<z<=3 
                        0      else where
''' 
#  simulation of it 

# f
    
num_samples = 100000
X_samples = np.random.uniform(0, 1, num_samples)
Y_samples = np.random.uniform(1, 2, num_samples)
Z_samples = X_samples + Y_samples

# Compute empirical PDF
hist, bin_edges = np.histogram(Z_samples, bins=100, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

def theoretical_pdf(z):
    if(1<=z<=2):
        return z-1
    elif(2<=z<=3):
        return 3-z
    else:
        return 0

# Compare with theoretical PDF
theoretical_values = np.array([theoretical_pdf(z) for z in bin_centers])

# Plot empirical and theoretical PDF
plt.plot(bin_centers, hist, label='Empirical PDF')
plt.plot(bin_centers, theoretical_values, label='Theoretical PDF')
plt.xlabel('Z')
plt.ylabel('Density')
plt.legend()
plt.title('Comparison of Empirical and Theoretical PDFs')
plt.show()
