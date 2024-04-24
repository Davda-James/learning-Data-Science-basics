import re 
import pandas as pd
import csv
import matplotlib.pyplot as plt 
import numpy as np
from collections import Counter
def clean_string(s):
    pattern = r'[^a-zA-Z\s]'
    cleaned_text = re.sub(pattern, '',s).lower()
    return cleaned_text

with open("fileA-TimeMachine.txt",'r',encoding='utf-8') as f:
    main_string=f.read()
    f.close()
string=clean_string(main_string)
string=string.replace("  ","")
string=string.replace("   ","")
string=string.replace("    ","")
string=string.replace("     ","")
string=string.replace("      ","")
string=string.replace("\n"," ")
string=string.replace("\n\n"," ")
string=string.replace("\n\n\n"," ")
string=string.replace("\n\n\n\n"," ")
string=string.rstrip()
with open("new_test.txt","w") as f:
    f.write(string)
    f.close()
data=string.split(" ")



# Q (1)(a)
# def calculate_freq():
#     dic={}
#     for word in data:
#         if(word!=''):
#             if(word not in dic.keys()):
#                 dic[word]=1
#             else:
#                 dic[word]+=1
#     return dic  
def plot_freq(zlist):
    plt.hist(zlist, bins=40, density=True)
    ticking=np.arange(1,50,1)
    plt.xlabel('Frequency')
    plt.ylabel('Probability')
    # plt.xticks(ticking)
    plt.title('Frequency Distribution')
    plt.show()

# dic=calculate_freq()
# with open("frequency_of_words.csv","w",newline='') as f:
#     writer=csv.writer(f)
#     writer.writerow(['words', 'frequency'])
#     for key, value in dic.items():
#             writer.writerow([key, value])
#     f.close()


# uncomment below directly to plot the graph of the frequency  

# df=pd.read_csv("frequency_of_words.csv")
# freqlist=list(df.loc[:,'frequency'])
# #  as in freqlist there are some outliers which kind of has frequency 0 as they are not appearing many times due to which for 
# # better view of the graph i have filtered those so that we could observe which values has higher frequency
# newlist=list(filter(lambda x:x<100,freqlist))
# plot_freq(newlist)





# Q (1)(b)

new_string=string.replace(" ","")

pairs = [new_string[i:i+2] for i in range(len(new_string)-1)]
pair_counts = Counter(pairs)
total_pairs=sum(pair_counts.values())
pair_probabilities = {pair: count / total_pairs for pair, count in pair_counts.items()}
sorted_pairs = sorted(pair_probabilities.items(), key=lambda x: x[1], reverse=True)
print("Top 10 ordered pairs and their probabilities:")
for pair, probability in sorted_pairs[:10]:
    print(f"{pair}: {probability:.6f}")




# Q (1)(c)
sec_string= re.sub(r'[^\w\s]', '', main_string)
pairs2 = [sec_string[i:i+2] for i in range(len(sec_string)-1)]
pair_counts2 = Counter(pairs2)
total_pairs2 = sum(pair_counts2.values())
pair_probabilities2 = {pair: count / total_pairs for pair, count in pair_counts2.items()}
sorted_pairs2 = sorted(pair_probabilities2.items(), key=lambda x: x[1], reverse=True)
print("Top 10 ordered pairs and their probabilities:")
for pair, probability in sorted_pairs2[:10]:
    print(f"{pair}: {probability:.6f}")



