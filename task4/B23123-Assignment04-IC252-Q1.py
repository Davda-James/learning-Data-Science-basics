import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# a.

print("theoretical value table :")

df=pd.DataFrame([[1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]],index=['T-shirt','sweater','jacket'],columns=["sunny","rainy","cloudy"])
print(df)
print("\n")

#  simulation of above problem a
# here n is no of simulation
n=10000
weatherlist=["sunny","rainy","cloudy"]
outfitlist=["T-shirt","sweater","jacket"]
ans=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(10000):
    weatherchoice=np.random.choice(weatherlist)
    outfitchoice=np.random.choice(outfitlist)
    ans[outfitlist.index(outfitchoice)][weatherlist.index(weatherchoice)]+=1
finaldf=pd.DataFrame(ans,index=outfitlist,columns=weatherlist)
finaldf["sunny"]=finaldf['sunny']/n
finaldf["rainy"]=finaldf["rainy"]/n
finaldf["cloudy"]=finaldf["cloudy"]/n
finaldf["sunny"]=finaldf['sunny'].apply(lambda x: format(x,".4f")).astype(float)
finaldf["rainy"]=finaldf['rainy'].apply(lambda x: format(x,".4f")).astype(float)
finaldf["cloudy"]=finaldf['cloudy'].apply(lambda x: format(x,".4f")).astype(float)
print(finaldf)

# print(df["rainy"].sum())
# adding marginal probability in data frame
add=[finaldf["sunny"].sum(),finaldf["rainy"].sum(),finaldf["cloudy"].sum()]
finaldf.loc["marginal weather"]=add

# adding marginal of outfit to dataframe
other=[]
other.append(finaldf.loc["T-shirt",["sunny","rainy","cloudy"]].sum())
other.append(finaldf.loc["sweater",["sunny","rainy","cloudy"]].sum())
other.append(finaldf.loc["jacket",["sunny","rainy","cloudy"]].sum())
other.append("")
finaldf["marginal outfit"]=other
print(finaldf)


# b

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].set_xlabel("Random Variable X (representing outfits)")
axs[0].set_ylabel("Marginal Probabilities")
axs[0].set_title("Marginal Probability Plot for outfit")
x=[0,1,2]
axs[0].set_xticks(x)
axs[0].bar(x,add, color="blue",width=0.01)
axs[0].scatter(x,add, color="red")
axs[0].plot()

axs[1].set_xlabel("Random Variable Y (representing weather)")
axs[1].set_ylabel("Marginal Probabilities")
axs[1].set_title("Marginal Probability Plot for weather")
axs[1].set_xticks(x)
y=finaldf["marginal outfit"].to_list()
y.remove("")
axs[1].bar(x,y, color="blue",width=0.01)
axs[1].scatter(x,y, color="red")
axs[1].plot()
plt.show()


# c

anslist=[]
anslist.append(finaldf.loc["T-shirt","sunny"]/finaldf.loc["marginal weather","sunny"])
anslist.append(finaldf.loc["T-shirt","rainy"]/finaldf.loc["marginal weather","rainy"])
anslist.append(finaldf.loc["T-shirt","cloudy"]/finaldf.loc["marginal weather","cloudy"])
anslist=list(map(lambda x:float(format(x,".4f")),anslist))
print(anslist)
