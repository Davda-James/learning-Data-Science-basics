import numpy as np
import matplotlib.pyplot as plt 
#  mean=65 and std=15
def plot_me(y,samples):
    color=['orange','blue','green','red']
    fig, axs = plt.subplots(2, 3, figsize=(10, 6))
    axs[0,0].set_title("parent distribution")
    axs[0,0].set_xlabel("x values")
    axs[0,0].set_ylabel("probability density values")
    axs[0,0].hist(y,bins=20,ec="black",color=color[0])
    for i in range(1,6):
        row = 0 if i < 3 else 1
        col = i % 3
        axs[row,col].hist(samples[i-1],bins=15, ec="black" ,label=f'Sample {i+1}',color=color[i%4])
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
        variance=np.std(samples[i])
        means[i]=meanx
        var[i]=variance
    return means,var

mu=65  
sigma=15
n=50
yvalues=np.random.normal(mu,sigma,1000)
samples=[]

# Q (3)(a)
for i in range(5):
    random_sample=np.random.choice(yvalues,size=n,replace=True)
    samples.append(random_sample)
# plot the graph 
plot_me(yvalues,samples)

means,std=conclusion(samples)
for i in range(5):
    print(f"mean of sample{i+1} is : {means[i]}")
    print(f"std of sample{i+1} is : {std[i]}")

def plot_all(y,new_samples):
    color=['orange','blue','green','red']
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs[0,0].set_title("parent distribution")
    axs[0,0].set_xlabel("x values")
    axs[0,0].set_ylabel("probability density values")
    axs[0,0].hist(y,bins=20,ec="black",color=color[0])
    for i in range(1,4):
        row = 0 if i < 2 else 1
        col = i % 2
        axs[row,col].hist((new_samples[i-1]),bins=15,ec="black" ,label=f'Sample {i+1}',color=color[i])
        axs[row,col].set_title('Random Samples')    
        axs[row,col].set_xlabel("x values")
        axs[row,col].set_ylabel("probability density")
    plt.tight_layout()
    plt.show()


#  Q(3)(b)
sizes=[100,150,250]
new_samples=[]
for i in range(3):
    ran_samp=np.random.choice(yvalues,sizes[i])
    new_samples.append(ran_samp)

# plot for the samples size 100,150,250 
plot_all(yvalues,new_samples)
print("sample size of 100,150,250")
new_mean,new_std=conclusion(new_samples)
for i in range(len(new_samples)):
    print(f"mean of sample{i+1} is : {means[i]}")
    print(f"std of sample{i+1} is : {new_std[i]}")


# Q (3)(c)

# Systematic sampling 
def systematic_sampling(population, k, sample_size):
    indices = np.arange(0, len(population), k)
    selected_indices = np.random.choice(indices, size=sample_size, replace=False)
    return population[selected_indices]

population = np.random.normal(loc=65, scale=15, size=10000)
k=20
sample_size=[100,150,200,250]
list_samples = [systematic_sampling(population, k, size) for size in sample_size]

def plot_last(new_samp):
    color=['orange','blue','green','red']
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    for i in range(4):
        row = 0 if i < 2 else 1
        col = i % 2
        axs[row,col].hist((new_samp[i]),bins=15,ec="black" ,label=f'Sample {i+1}',color=color[i])
        axs[row,col].set_title('Random Samples')    
        axs[row,col].set_xlabel("x values")
        axs[row,col].set_ylabel("probability density")
    plt.tight_layout()
    plt.show()

plot_last(list_samples)

#  Q (3)(d)
last_mean,last_std=conclusion(list_samples)
print()
print("stats of systematic sampling")
for i in range(len(list_samples)):
    print(f"mean of sample{i+1} is : {last_mean[i]}")
    print(f"std of sample{i+1} is : {last_std[i]}")

# yes there is difference between the mean and variance as comapred to the earlier in part 2
# but they are kinf of close to the real values only 
