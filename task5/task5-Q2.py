import math
import pandas as pd 
import numpy as np
import csv
import matplotlib.pyplot as plt
import math
from scipy.stats import entropy
# Q (2)(1)

def expect_mobility_mumbai(mumbai_data):
    mobility=(1/6)*(mumbai_data['retail_and_recreation_percent_change_from_baseline']+ mumbai_data['grocery_and_pharmacy_percent_change_from_baseline'] +mumbai_data['parks_percent_change_from_baseline']+mumbai_data['transit_stations_percent_change_from_baseline']+mumbai_data['workplaces_percent_change_from_baseline']+mumbai_data['residential_percent_change_from_baseline'])
    newdata= pd.DataFrame({'date': mumbai_data['date'],'retail_recreation':mumbai_data['retail_and_recreation_percent_change_from_baseline'],'grocery_pharmacy':mumbai_data['grocery_and_pharmacy_percent_change_from_baseline'],'parks':mumbai_data['parks_percent_change_from_baseline'],'station':mumbai_data['transit_stations_percent_change_from_baseline'],'workplaces':mumbai_data['workplaces_percent_change_from_baseline'],'residential':mumbai_data['residential_percent_change_from_baseline'],'expected_mobility': mobility})
    newdata.to_csv('expected_mobility_mumbai.csv', index=False)
    return newdata

df=pd.read_csv("2021_IN_Region_Mobility_Report.csv")
# retail_and_recreation_percent_change_from_baseline
# grocery_and_pharmacy_percent_change_from_baseline                            
# parks_percent_change_from_baseline                                           
# transit_stations_percent_change_from_baseline                               
# workplaces_percent_change_from_baseline                                
# residential_percent_change_from_baseline
mumbai_data = df[df['sub_region_2'] == 'Mumbai']
mumbai_data=mumbai_data[['date','retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']]

# call this for ques 1
newdata=expect_mobility_mumbai(mumbai_data)


# Q (2)(2)



#  Uncomment this to run q-2
# lockdown_start_date='2021-04-01'
# lockdown_end_date='2021-05-20'
# lockdown_data = mumbai_data[(mumbai_data['date'] >= lockdown_start_date) & (mumbai_data['date'] <= lockdown_end_date)]
# retail_recreation=lockdown_data['retail_and_recreation_percent_change_from_baseline']
# grocery_pharmacy=lockdown_data['grocery_and_pharmacy_percent_change_from_baseline']
# parks=lockdown_data['parks_percent_change_from_baseline']
# transit_station=lockdown_data['transit_stations_percent_change_from_baseline']
# workplaces=lockdown_data['workplaces_percent_change_from_baseline']
# residential=lockdown_data['residential_percent_change_from_baseline']
# new_expect=0.2*lockdown_data['grocery_and_pharmacy_percent_change_from_baseline']+0.2*lockdown_data['retail_and_recreation_percent_change_from_baseline']+0.05*lockdown_data['transit_stations_percent_change_from_baseline']+0.02*lockdown_data['parks_percent_change_from_baseline']+0.5*lockdown_data['residential_percent_change_from_baseline']+0.03*lockdown_data['workplaces_percent_change_from_baseline']
# dates=lockdown_data['date']
# fig=plt.figure(figsize=(10,7))
# plt.title("Expected mobilities and mobilities")
# plt.xlabel("Date")
# plt.ylabel("values")
# plt.xticks(rotation=45)
# plt.plot(dates,new_expect,color="blue",label="expectation mobility")
# plt.plot(dates,retail_recreation,color="orange",label="reatil_recreation")
# plt.plot(dates,grocery_pharmacy,color="green",label="grocery_pharmacy")
# plt.plot(dates,parks,color="yellow",label="parks")
# plt.plot(dates,transit_station,color="red",label="transit_station")
# plt.plot(dates,workplaces,color="violet",label="workplaces")
# plt.plot(dates,residential,color="black",label="residential")
# plt.legend(loc="upper right")
# plt.show()



# Q (2)(i)
def mean_abs_error(): 
    indiv_expect=(abs(newdata['retail_recreation']-newdata['expected_mobility'])+abs(newdata['grocery_pharmacy']-newdata['expected_mobility'])+abs(newdata['parks']-newdata['expected_mobility'])+abs(newdata['station']-newdata['expected_mobility'])+abs(newdata['workplaces']-newdata['expected_mobility'])+abs(newdata['residential']-newdata['expected_mobility']))/6
    sec_final_mean=indiv_expect.mean()
    final_list=list(map(lambda x:abs(x-sec_final_mean),indiv_expect))
    final_mean=sum(final_list)/len(final_list)
    return final_mean
def root_mean_squared_error():
    indiv_expect=(((newdata['retail_recreation']-newdata['expected_mobility'])**2+(newdata['grocery_pharmacy']-newdata['expected_mobility'])**2+(newdata['parks']-newdata['expected_mobility'])**2+(newdata['station']-newdata['expected_mobility'])**2+(newdata['workplaces']-newdata['expected_mobility'])**2+(newdata['residential']-newdata['expected_mobility'])**2)/6)**0.5
    meanx=indiv_expect.mean()
    last_list=list(map(lambda x:(x-meanx)**2,indiv_expect))
    final_mean=(sum(last_list)/len(last_list))**0.5
    return final_mean
# print(root_mean_squared_error());
def kldivergence():
    norm_retail=np.array(abs(newdata['retail_recreation']/sum(newdata['retail_recreation'])))
    norm_grocery=np.array(abs(newdata['grocery_pharmacy']/sum(newdata['grocery_pharmacy'])))
    norm_parks=np.array(abs(newdata['parks']/sum(newdata['parks'])))
    norm_station=np.array(abs(newdata['station']/sum(newdata['station'])))
    norm_work=np.array(abs(newdata['workplaces']/sum(newdata['workplaces'])))
    norm_resident=np.array(abs(newdata['residential']/sum(newdata['residential'])))
    norm_expect=np.array(abs(newdata['expected_mobility']/sum(newdata['expected_mobility'])))
    # norm_retail=np.array(list(map(lambda x:handle_zero(x),norm_retail)))
    # norm_grocery=np.array(list(map(lambda x:handle_zero(x),norm_grocery)))
    # norm_parks=np.array(list(map(lambda x:handle_zero(x),norm_parks)))
    # norm_station=np.array(list(map(lambda x:handle_zero(x),norm_station)))
    # norm_work=np.array(list(map(lambda x:handle_zero(x),norm_work)))
    # norm_resident=np.array(list(map(lambda x:handle_zero(x),norm_resident)))
    retail_kl=sum(np.where(norm_retail==0, 0,norm_retail*np.log2(norm_retail/norm_expect)))
    grocery_kl=sum(np.where(norm_grocery==0,0,norm_grocery*np.log2(norm_grocery/norm_expect)))
    parks_kl=sum(np.where(norm_parks==0,0,norm_parks*np.log2(norm_parks/norm_expect)))
    station_kl=sum(np.where(norm_station==0,0,norm_station*np.log2(norm_station/norm_expect)))
    work_kl=sum(np.where(norm_work==0,0,norm_work*np.log2(norm_work/norm_expect)))
    resident_kl=sum(norm_resident*np.log2(norm_resident/norm_expect))
    return (retail_kl+grocery_kl+parks_kl+station_kl+work_kl+resident_kl)/6
# print(mean_abs_error())
# print(root_mean_squared_error())
# print(kldivergence())

