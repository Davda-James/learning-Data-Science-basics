import numpy as np
import matplotlib.pyplot as plt

# Q (3)(a)

def perform_drunkardwalk(totalsteps,p):
    if(p==0.5):
        choice_list=[-1,1]
    elif (p==0.6):
        choice_list=[-1,-1,-1,-1,1,1,1,1,1,1]
    final_pos=np.zeros(10000,dtype=int)
    choices=np.random.choice(choice_list,size=(10000,totalsteps))
    for i in range(10000):
        curr_pos=0
        for choice in choices[i]:
            curr_pos+=choice
        final_pos[i]=curr_pos
    return final_pos
def plot_distribution(prob_list,steps):
    plt.hist(prob_list, bins=30, density=True, alpha=0.75,ec="black",hatch=".")
    plt.xlabel('Final Location')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Final Locations')
    plt.savefig(f"{steps}_biased.png")
    plt.clf()
steps_list=[100,1000,10000]
for i in steps_list:
    prob_list=perform_drunkardwalk(i,0.6)
    plot_distribution(prob_list,i)


