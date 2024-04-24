import numpy as np
# a.
n=100
x=np.random.normal(150,10,n)
# integer_values = np.round(x).astype(int)
m=list(filter(lambda x:x<140,x))
print("probability that the widget weighs less than 140 is : ",len(m)/n)
# b.
otherlist=list(filter(lambda x: x>150,x))
otherlist.sort()
otherlist=otherlist[::-1]
top5=int(0.05*len(otherlist))
sorted_top5=otherlist[:top5]
print("minimum weight of product that willqualify as premium product is : ",format(min(sorted_top5),'.2f'))

# c.
seclist=list(filter(lambda x:x<150,x))
seclist.sort()
least10=int(0.10*len(x))
print("minimum weight allowed for a widget to be considered within the acceptable range",format(seclist[10],'.2f'))

# d.
prob=(n-(top5+least10))/n
print("proability that product is neither premium nor defective is : ",prob)