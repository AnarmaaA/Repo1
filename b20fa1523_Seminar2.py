#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Өгөгдсөн утга нь палиндром эсэхийг шалгах функц бич.
def checkPal(x):
    rev_x = x[::-1]
    if x == rev_x:
        return('It is a palindrome word')
    else:
        return('It is not a palindrome word!!!!!!')
print(checkPal('hgoghd'))


# In[13]:


#2. Өгөгдсөн жагсаалтаас том болон жижиг үсгүүдийг тоолох функц бич. 
def countCapitals(x):
    c_s = 0
    c_l = 0
    for i in x:
        if(i.islower()):
            c_s = c_s + 1
        if(i.isupper()):
            c_l = c_l + 1
    print('Upper:',c_l)
    print('Lower:',c_s)
a = ['D','g','f','A']
countCapitals(a)


# In[49]:


#3. Жагсаалтын утгуудын үржвэрийг олох функц бич. 
def multList(x):
    multi = 1
    for i in x:
        multi = multi * i
    return multi

a = [1,2,3,4,5,6,7,8,9,10]
print(multList(a))
    


# In[50]:


#4. Өгөгдсөн тооны бактерал олох функц бич.
def bak(x):
    bak_num = 1
    for i in range(x):
        bak_num = bak_num * (i+1)
    return bak_num
print(bak(5))


# In[5]:


#5. Өгөгдсөн жагсаалтыг урвуу болгох функц бич
def reverseList(x):
    rev_x = x[::-1]
    return rev_x

a = [1,2,3,4,5,6,7,8,9,10]
print(reverseList(a))
        


# In[60]:


#6. Жагсаалтын утгуудын нийлбэрийг олох функц бич. 
def sumList(x):
    sum_num = 0
    for i in x:
        sum_num = sum_num + i
    return sum_num
a = [1,2,3,4,5,6,7,8,9,10]
print(sumList(a))
    


# In[15]:


#7. Жагсаалтын давхардсан утгуудыг арилгах функц бич. !!!
def dupDelete(x):
    dup_ = []
    for i in x:
        if i not in dup_:
            dup_.append(i)
    return dup_
a = [1,2,33,44,33,44]
print('x:',dupDelete(a))


# In[44]:


#8. 3 тооны хамгийн ихийг олдог функц бич
def maxOfThree(a,b,c):
    max_ = 0
    if (a >= b) and (a >= c):
        max_ = a
    elif (b >= a) and (b >= c):
        max_ = b
    else:
        max_ = c
    return max_
print(maxOfThree(5,6,7))   


# In[ ]:





# In[ ]:




