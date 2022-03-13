#!/usr/bin/env python
# coding: utf-8

# In[6]:


#--1
import numpy as np
arr = np.array([])
for i in range(50,101):
    arr = np.append(arr,i)
print(arr)
    


# In[7]:


#--2
arr = np.array([])
for i in range (1,11):
    arr = np.append(arr,1)
for i in range (1,11):
    arr = np.append(arr,0)
for i in range (1,11):
    arr = np.append(arr,6)
print(arr)


# In[8]:


#--4
arr = np.zeros((3,3), int)
np.fill_diagonal(arr,1)
print(arr)


# In[9]:


#--3
arr = np.arange(20,32)
a = np.reshape(arr,(3,4))
print(a)


# In[10]:


#--5
arr = np.zeros((5,5),int)
np.fill_diagonal(arr,[1,2,3,4,5])
print(arr)


# In[11]:


#--6
arr1 = np.arange(20,32)
a1 = np.reshape(arr1,(3,4))
arr2 = np.arange(30,42)
a2 = np.reshape(arr2,(3,4))
sum_arr = a1+a2
column_sums = sum_arr.sum(axis=0)
row_sums = sum_arr.sum(axis=1)
print(sum_arr)
print('Moriin niilber:' ,row_sums)
print('Baganiin niilber:',column_sums )


# In[ ]:





# In[42]:


#Salaries
KobeBryant_Salary = [27849149,30453805,23500000, 250000000,0,0,0,0,0,0]
JoeJohnson_Salary = [19752645,21466718,23180790, 22309344,11000000,10254904,0,0,0,0]
LeBronJames_Salary = [17545000,19067500,20644400, 22970500,30963450,33285709,35654150,37436858,39219566,0]
CarmeloAnthony_Salary = [19450000,22407474,22458000, 22875000,24559380,26243760,2393887,2159029,2564753,0]
DwightHoward_Salary = [19536360,20513178,21436271,22359364,23180275, 23500000, 24256725, 5443553, 2564753, 2641691]
ChrisBosh_Salary = [17545000,19067500,20644400,22192730, 23741060, 25289390, 26837720, 0,0,0]
ChrisPaul_Salary = [17779458,18668431,20068563,21468695, 22868827,24268959, 35654150, 38506482, 41358814, 30800000]
KevinDurant_Salary = [16669630,17832627,18995624,20158622, 26540100, 25000000, 30000000, 38199000, 38771513, 42018900]
DerrickRose_Salary = [16402500,17632688,18862875, 20093064, 21323252, 2525077, 2393887, 6859756, 7682927, 13445120]
DwayneWade_Salary = [17182000,18673000,15000000, 20000000, 23200000, 17878652, 2393887, 0,0,0]
#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

#Games 
KobeBryant = [78,6,35, 66,0,0,0,0,0,0]
JoeJohnson = [72,79,80, 81,57,24,78,55,0,0]
LeBronJames =[76,77,69, 76,74,82,55,67,45,48]
CarmeloAnthony = [67,77,40, 72,74,78,2,58,3,3]
DwightHoward = [76,71,41, 71,74,81,9,69,69,47]
ChrisBosh = [74,79,44, 53,0,0,0,0,0,0]
ChrisPaul = [70,62,82, 74,61,58,58,70,70,58]
KevinDurant = [81,81,27, 72,62,68,78,0,32,0]
DerrickRose = [0,10,51, 66,64,25,51,50,50,26]
DwayneWade = [69,54,62, 74,60,67,72,0,0,0]
#Matrix
Games = np.array([KobeBryant, JoeJohnson, LeBronJames, CarmeloAnthony, DwightHoward, ChrisBosh, ChrisPaul, KevinDurant, DerrickRose, DwayneWade])
#Field Goals
KobeBryant_FG = [738,31,266, 398, 0,0,0,0]
JoeJohnson_FG = [445,462,446, 377, 273, 146, 0,0]
LeBronJames_FG = [765,767,624, 737, 736, 857, 558, 643 ]
CarmeloAnthony_FG = [669,743,358,567, 602,472, 49, 336 ]
DwightHoward_FG = [470,473,251, 372,388,506,43,202]
ChrisBosh_FG = [485,492,343,358,0,0,0,0]
ChrisPaul_FG = [412,406,568,515, 374, 367, 302, 434]
KevinDurant_FG = [731,849,238,698, 551, 630, 721,0]
DerrickRose_FG = [0,58,338,447, 460, 162, 363, 369]
DwayneWade_FG = [569,415,509, 540, 414, 508, 416,0]
#Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])
print("Toglogchidiin tus buriin niit tsalin:")
print(np.sum(Salary, axis = 0))
print("Toglolchid buriin jiliin tsalinguud :")
print(np.sum(Salary, axis = 1))

print("Toglogchidiin tus bur niit toglolt:")
print(np.sum(Games, axis = 0))
print("On tus buriin toglogchdiin niit toglolt:")
print(np.sum(Games, axis = 1))
print("Toglogchidiin tus bur niit field goal:")
print(np.sum(FieldGoals, axis = 0))
print("On tus buriin toglogchdiin niit field goal:")
print(np.sum(FieldGoals, axis = 1))


# In[ ]:





# In[ ]:





# In[ ]:




