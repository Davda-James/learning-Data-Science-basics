import numpy as np
import random 
import pandas as pd
import math 
import matplotlib.pyplot as plt
list_choice=[0,0,1] 
n=int(input("enter the number of times you wanna play game: "))
switch_wins=0
stay_wins=0
random.seed(2)
for i in range(n):
	# here if user wanted to try then we can remove the comments and comment the portion thta generates random choice on its own
	random.shuffle(list_choice)
	# user_choice=int(input("Enter door number you want to choose: "))
	# while(user_choice>2 or user_choice<0):
	# 	user_choice=int(input("Enter the number between 0 to 2: "))	
	user_choice=random.choice([0,1,2])
	door_without_prize=[i for i in range(3) if  i!=user_choice and list_choice[i]==0]
	prized_door=list_choice.index(1)
	monty_choice=random.choice(door_without_prize)
	# here we are taking random input for switching or staying using random choice 
	final_dec=random.choice(['y','n'])
	# we can uncomment below final_dec when we are taking user input
	# final_dec=input("Do you wanna switch your door (0 or 1 or 2) ?(type y for yes and n for no): ")
	if(final_dec=='y'):
		# print("Wait for luck ,oops probability ................")
		if(user_choice!=prized_door):
			switch_wins+=1
			# this has been commented out but we can uncomment when we are taking user_input
			# print("YOU WON A CARRRRRRR..................")
		else:
			stay_wins+=1
			# print("SORRY YOU LOOSEEE....................")
	else:
		if(user_choice==prized_door):
			stay_wins+=1
			# print("YOU WON A CARRRRRRR.................")
		else:
			switch_wins+=1
			# print("SORRY YOU LOOSEEE...................")
data=pd.DataFrame({"Choice":["Switch","Stay"],"Wins":[switch_wins,stay_wins],"Probability of winning":[switch_wins/n,stay_wins/n]})
print(data)
plt.title("Probability Vs Contestant Choice")
plt.xlabel("contestant Choice")
plt.ylabel("Probability of winning")
xlist=['Switch',"Stay"]
ylist=[switch_wins/n,stay_wins/n]
plt.grid(True)
plt.bar(xlist,ylist,color=["green","orange"])
plt.show()
