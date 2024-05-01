import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
# f(x)=  integral of sin^4(x) from 0 to pi
# let here g(x)=sin^4(x)
# so max value of g(x) in 0 to pi is 1 and minimum value is 0
def integral_estimation(n):
    xlist = np.random.uniform(0, math.pi, n)
    avg_val = np.mean(np.sin(3 * xlist) ** 4)
    integral_estimate = avg_val * math.pi
    return integral_estimate

totaltrials=2000
xvalues=np.arange(1,totaltrials+1,1)
ans=[integral_estimation(i) for i in xvalues]

# # value of f(x) is theoretically caluclated = 3*pi/8 = 1.178
exact_value=1.178

# plt.title("Value of f(x) with no of samples")
# plt.xlabel("no of samples")
# plt.ylabel("Value of estimated integral")
# plt.plot(xvalues,ans,label=f"Estimated integral value= {ans[1999]}")
# plt.legend()
# plt.savefig("monte_carlo_integral.png")

#  animation of simulation
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.axhline(y=exact_value, color='r', linestyle='--', label=f'Exact Value {exact_value}\nAverage Value {sum(ans)/totaltrials}')  # Plot exact value as a reference
ax.set_xlim(0, totaltrials)
ax.set_ylim(0, 2.8)
ax.set_xlabel("Number of samples")
ax.set_ylabel("Estimate of integral")
ax.set_title("Monte Carlo Estimation of Integral with Increasing Number of Samples")
ax.legend()

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(xvalues[:i], ans[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=totaltrials, interval=10, blit=True)

plt.show()