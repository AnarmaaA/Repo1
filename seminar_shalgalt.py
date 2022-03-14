#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг мөр бүрд хэвлэх функц бич.
n = int(input())
for i in range(1,n+1):
    print('*'*i)


# In[6]:


# Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг жагсаалтын мөр бүрд хэвлэх функц бич.
n = int(input())
for i in range(1,n+1):
    l = ['*'*i]
    for j in l:
        print(j)


# In[12]:


# Дараах жагсаалтаас хамгийн их, хамгийн бага key-г авах функц бич.
students = {
'Bat': 18, 
'Oyun': 22,
'Dulam': 21,
'Suren': 20
}

def max_dict(x):
    max_min = [max(x, key=x.get ),min(x, key=x.get)]
    return max_min

res = max_dict(students)
for i in res:
    print(i)
    


# In[14]:


#  np.arange(1-1000) массив үүсгэ. Тухайн массиваас 3 эсвэл 7 –д хуваагдах тоонуудыннийлбэрийг ол.
import numpy as np
arr = np.arange(1,1000)
sum = 0
for i in arr:
    if ((i % 3) == 0 or (i % 7) == 0):
        sum = sum + i
print(sum)


# In[ ]:




