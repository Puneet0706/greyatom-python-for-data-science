# --------------
# Importing header files
import numpy as np
import warnings
import statistics 
  
warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print(type(new_record))
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print(type(data))
#Code starts here
census=np.concatenate((data,new_record),axis=0)
print(data.shape,census.shape)
print("=================")
print(census,"\n","================")
age=census[ :,0]
print(age)
max_age=round(max(age),0)
min_age=round(min(age),0)
age_mean=round(statistics.mean (age),2)
age_std=round(np.std(age),2)
print("=============","\n",max_age,"\n",min_age,"\n",age_mean,"\n",age_std)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


print("=================")
len_0= len(race_0)
len_1= len(race_1)
len_2= len(race_2)
len_3= len(race_3)
len_4= len(race_4)
print(len_0,len_1,len_2,len_3,len_4)

minimum=min(len_0,len_1,len_2,len_3,len_4)
minority_race=3
print(minority_race)

senior_citizens=census[census[:,0]>60]

working_hours_sum=round(senior_citizens.sum(axis=0)[6],2)
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=round(np.mean(high[:,7]),2)
avg_pay_low=round(np.mean(low[:,7]),2)
print("=======","\n",high,"\n",low,"\n",avg_pay_high,"\n",avg_pay_low)







