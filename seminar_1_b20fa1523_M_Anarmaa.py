# ---- 1 
mylist = ['python','php','java']
for i in mylist:
    print(i)
    
# ---- 2
numlist = [1,2,3,4,5,6,7,8,9,10]
sumList = 0
for i in numlist:
    sumList = sumList + i
print(sumList)
    
# ---- 3
def multiList(x):
    multi = 1
    for i in x:
        multi = multi * i
    return multi

numlist5 = [13,5,6,7,4]
print(multiList(numlist5))

# ---- 4
def multiByIndex(x):
    m = x[2] * x[-1]
    return m
    
print(multiByIndex(numlist5))

# ---- 5
def maxAndMin(x):
    maxNum = x[0]
    minNum = x[0]
    for i in x:
        if(minNum > i):
            minNum = i
    for j in x:
        if(maxNum < i):
            maxNum = i
    maxAndMin = [maxNum,minNum]
    return maxAndMin
print('Maximum :',maxAndMin(numlist5)[0],'Minumum:',maxAndMin(numlist5)[1])
        
# ---- 6
def countDoubles(x):
    count = 0
    for i in x :
        if len(i) > 2:
            if i[0] == i[-1]:
                count = count + 1   
    return count
inp = ['abdba','abcd','121']
print(countDoubles(inp))
            
# ---- 7 
inp2 = ['abdba','abcd','121','121','abcd']
inp2 = list(dict.fromkeys(inp2))
print(inp2)
    
# ---- 8
def checkEmpty(x):
    if len(x) == 0:
        return 'List is empty'
    else:
        return 'List is not empty'
checkList = []
print(checkEmpty(checkList))

# ---- 9
list_10 = [22,32,54,45,23,23,45,67,89,60]
list_delete = [list_10[3],list_10[5],list_10[7]]
for i in list_delete:
    list_10.remove(i)
    
for i in list_10:
    print(i)
   
# ---- 10
num_tuple = (12,23,45,32,35)
# ---- 11
tuple_1 = ('Sara','Nara','Bold')
new_element = ('Ganaa',)
tuple_1 = tuple_1 + new_element
print(tuple_1)
# ---- 12
print(num_tuple[1],num_tuple[-1])
# ---- 13
def searchInput(x,y):
    ch = 0
    for i in x:
        if i == y:
            ch = ch + 1
    if ch != 0:
        return 'Input is in the tuple'
    else:
        return 'Input is not in the tuple'
print(searchInput(num_tuple,int(input())))
# ---- 14
for i in num_tuple:
    print(i)
# ---- 15
students1 = {'Jack','Sarah','John','Hanna'}
students2 = {'Bayar','Zaya','Sanchir','Hanna','John'}
union = set.union(students1,students2)
for i in union:
    print(i)

# ---- 16
def findDupl(x,y):
    dupl = {''}
    for i in x:
        for j in y:
            if j == i:
                dupl.add(i)
    return dupl
print(findDupl(students1,students2))
# ---- 17
def lenList(x):
    c = 0
    for i in x:
        c = c + 1
    return c
print(lenList(students2))
# ---- 18
element = str(input())
students1.remove(element)
print('Removed',element,'from list.')
# ---- 19
students1.clear()
# ---- 20
del(students1)
# ---- 21
numDict = {
    '1':89,
    '2':45,
    '7':56,
    '3':75,
    '4':55,
    '34':67}

#Sort ascending.
print('Sorting values by ascend:\n')
for i in sorted (numDict.values()) :
     print(i, end = " ")
     
#Sorting descenting
print('\n\nSorting values by descend:\n')
des = sorted(numDict, key=numDict.get, reverse=True)
for i in des:
     print(numDict[i], end = " ")
     
# ---- 22
searchInDict = int(input())
values = numDict.values()
flag = False
for i in values:
    if searchInDict == i:
        flag = True
if flag:
    print(searchInDict,'is in the dictionary.')
else:
    print(searchInDict,'is not in the dictionary.')
    
# ---- 23
keys = numDict.keys()
flag = False
for i in keys:
    if str(searchInDict) == i:
        flag = True
if flag:
    print(searchInDict,'is in the dictionary.')
else:
    print(searchInDict,'is not in the dictionary.')

# ---- 24
for x,y in numDict.items():
    print(x, y)
    
# ---- 25
strDict = {
    'Name':'Sarah',
    'Age':30,
    'Sex':'Female',
    'Major':'Broker'}
def mergeTwoDict(x,y):
    z = x.copy()
    z.update(y)
    return z
print(mergeTwoDict(numDict,strDict))

# ---- 26
dict_sum = 0
for i in numDict.values():
    dict_sum = dict_sum + i
print('Sum of dictionary : ',dict_sum)


