# probability for this question can be determined by the approach below
# as we have to won the game so number spoken by me should match the label for this we can use proability complement
# we can find the probability that I loose in this game
# probability of loosing can be determined easily using dearrangement
#  PROBABILITY : 1-D(n)/n! , where D(n) = n!(1-1!+ 1/2! - 1/3! ......((-1)^n*1/n!)
# Final Probability for winning is (1-1/2! + 1/3! - 1/4! ......)
#  By taylor's theorem we can guess the value this probabiity approaches to is 1/e
# The probability for winning will be maximum when no of cards is less that is 2
#  Now let's visualize it using graph
import numpy as np
import matplotlib.pyplot as plt
import math
def solve(n):
    val=0
    for i in range(1,n+1):
        val+=((-1)**(i+1))/math.factorial(i)
    return val
x=[i for i in range(2,21)]
# vect_fun=np.vectorize(solve)
y=[solve(j) for j in x]
plt.title("Probability vs N")
plt.xlabel("Values of n...............")
plt.ylabel("Values of probability................")
plt.xticks(range(1,21,1))
plt.plot(x,y)
plt.show()  
print("max proability of winning the game occurs when the no of cards is 3")

