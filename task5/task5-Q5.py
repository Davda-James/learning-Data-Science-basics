import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation 


def pie_estimation(trials):
    points=0
    for _ in range(trials):
        x=np.random.uniform(0,1)
        y=np.random.uniform(0,1)
        if x**2+y**2<=1:
            points+=1
    p=points/trials
    pi=4*p
    return pi

nooftrials=3000
xvalues=np.arange(1,3001,1)
# for i in xvalues:
#     print(i)
ans=[pie_estimation(i) for i in xvalues]

# plt.title("Estimate of pi with no of samples")
# plt.xlabel("no of samples")
# plt.ylabel("Value of pi")
# plt.plot(xvalues,ans,label="pi with no of samples")
# plt.legend(loc="upper right")
# plt.savefig("monte_carlo_simulation_pi.png")
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, nooftrials)
ax.set_ylim(2, 4)
ax.set_xlabel("Number of samples")
ax.set_ylabel("Value of π")
ax.set_title("Estimation of π with increasing number of samples")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(xvalues[:i], ans[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(xvalues), interval=10, blit=True)

plt.show()







