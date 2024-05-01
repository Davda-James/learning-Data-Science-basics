import numpy as np 
import matplotlib.pyplot as plt 


# Q (3)(a)
def plot_me(y,samples):
    color=['orange','blue','green','red']
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs[0,0].set_title("parent distribution")
    axs[0,0].set_xlabel("x values")
    axs[0,0].set_ylabel("probability density values")
    axs[0,0].hist(y,bins=20,ec="black",color=color[0])
    for i in range(1,4):
        row = 0 if i < 2 else 1
        col = i % 2
        axs[row,col].hist(samples[i-1],bins=15, ec="black" ,label=f'Sample {i+1}',color=color[i-1])
        axs[row,col].set_title('Random Samples')    
        axs[row,col].set_xlabel("x values")
        axs[row,col].set_ylabel("probability density")
    plt.tight_layout()
    plt.show()
def conclusion(samples):
    means=np.zeros(len(samples))
    var=np.zeros(len(samples))
    for i in range(len(samples)):
        meanx=np.mean(samples[i])
        variance=np.var(samples[i])
        means[i]=meanx
        var[i]=variance
    return means,var
samples=[]
mu,sigma=map(float,input("enter mean and std deviation by space : ").split(" "))
n=50
yvalues=np.random.normal(mu,sigma,size=1000)

for i in range(5):
    random_sample=np.random.choice(yvalues,size=n,replace=True)
    samples.append(random_sample)

# plot of graphs 
plot_me(yvalues,samples)

#  Q(3)(b)

# conclusion of data and comparison
means,var=conclusion(samples)
for i in range(5):
    print(f"mean of sample{i} is : {means[i]}")
    print(f"variance of sample{i} is : {var[i]}")



# Q 3(c)
m=20
def plot_all(new_samples):
    color=['orange','blue','green','red']
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    for i in range(4):
        row = 0 if i < 2 else 1
        col = i % 2
        axs[row,col].hist((new_samples[i]), ec="black" ,label=f'Sample {i+1}',color=color[i-1])
        axs[row,col].set_title('Random Samples')    
        axs[row,col].set_xlabel("x values")
        axs[row,col].set_ylabel("probability density")
    plt.tight_layout()
    plt.show()

new_samples=[]
for i in range(4):
    data=np.random.choice(yvalues,m+10*i)
    new_samples.append(data)

plot_all(new_samples)

print("data for new samples with increasing size of sample : ")
new_means,new_var=conclusion(new_samples)
for i in range(len(new_samples)):
    print(f"mean of sample{i+1} is : {new_means[i]}")
    print(f"variance of sample{i+1} is : {new_var[i]}")