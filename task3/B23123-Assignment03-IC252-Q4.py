# In poker full house condition arises when we have 3 card among the five cards of same rank and other 2 cards of different rank
import math
import random

# a.
'''
    So first we can choose any among 13 cards to decide for rank we are free to do that and no. of ways for it is 13C2.
    Now we have to select among two ranks which rank should be thrice or twice and hence for it chances are 2C1.
    Now as we have selected rank of cards, so we have to choose two cards of same rank and for it no of ways is 4C2    Now we have to make choice for other two cards among the 48 cards: so among 48 we will choose 1 with 48C1 ways and now 
    we have to choose remaining 3 cards among other 4 cards and no of ways for it is 4c3.
'''
finalprob=(13*6*2*6*4)/(math.comb(52,5))
print(f"probability of full house in poker is {format(finalprob,".5f")}")

# b.
# d for diamond, c for club, h for hearts , and s for spade
# inserting diamond card in list
listofcard=[]   
for i in range(1,11):
    listofcard.append(f"{i}d")
listofcard=listofcard+["Jd","Qd","Kd","Ad"]

# inserting club card in list

for i in range(1,11):
    listofcard.append(f"{i}c")
listofcard=listofcard+["Jc","Qc","Kc","Ac"]

# inserting hearts card in list

for i in range(1,11):
    listofcard.append(f"{i}h")
listofcard=listofcard+["Jh","Qh","Kh","Ah"]

# inserting spade card in list

for i in range(1,11):
    listofcard.append(f"{i}s")
listofcard=listofcard+["Js","Qs","Ks","As"]

# validating for full house

def check_fullhouse(cards):
    # Counting occurrences of each rank
    card_count = {}
    for card in cards:
        rnk = card[:-1]  
        if rnk in card_count:
            card_count[rnk] += 1
        else:
            card_count[rnk] = 1
    
    # Checking for full house condition
    three_same = False
    two_same = False
    for count in card_count.values():
        if count == 3:
            three_same = True
        elif count == 2:
            two_same = True
    
    return three_same and two_same

# for i in range(1,11):
#     listofcard.append(f"{i}s")
# listofcard=listofcard+["Js","Qs","Ks","As"]
fullhouse=0
n=10000
for i in range(n):  
    randomly_generated_fivecards=random.sample(listofcard,5)
    ans=check_fullhouse(randomly_generated_fivecards)
    if ans==True:
        fullhouse+=1
print(f"experimental probability after doing experiment for {n} times is ",fullhouse/n)





# c. 
'''
    probability that in 1000 trials one will get at least 2 full houses is equal to 1 - probability of getting no full houses 
    or getting only one in 1000 trials  
    probability of getting no full house in 1000 trial =(1 - finalprob)**1000  
    probability of getting at least one full house in 1000 trials is = 1000C1 * finalprob * (1-finalprob)**999  
'''
print("probability of getting at least two full houses in 1000 trials is : ",format((1-(((1-finalprob)**1000) + 1000* finalprob * (1-finalprob)**999)),".4f"))
print("mean of getting at least two full houses in 1000 trials is :",format(1000*finalprob,".4f"))
print("variance of getting at least two full houses in 1000 trials is :",format(1000*finalprob*(1-finalprob),".4f"))

# simulation of above 
random.seed(10)
cnt=0
for i in range(100):
    # for j in range(1000):
    fullhouse1trial=0
    for i in range(1000):
        cardlist=random.sample(listofcard,5)
        if(check_fullhouse(cardlist)):      
            fullhouse1trial+=1
    if(fullhouse1trial>=2):
        cnt+=1
print("probability of getting at least two full houses in 1000 trials is ",format(cnt/100,".4f"))