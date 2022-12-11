#files Testing...


import pickle
myList = list()
f = open("testing1.txt", 'r')
myList = f.readlines()
num = len(myList)
myDict = dict()
lstList = list()
print("---------------------------")

for elements in myList:
    #print(elements)
    print("---------------------------")
    lst = elements[4:].split()

    for i in range(len(lst)):
        try:
            lst[i] = float(lst[i])
        except Exception as e:
            pass

    
    print("---------------------------")
    #print(lstList)
    print("---------------------------")
    myDict[elements[:3]] = lst 
print("---------------------------")
print(myDict)
print("---------------------------")
print(lst)
#print(myList)
print("---------------------------")

'''
my_list = ["1", "2", "3.22", "char", "5"]

for i in range(len(my_list)):
    try:    
        my_list[i] = float(my_list[i])
    except Exception as e:
        pass

print(my_list) # prints [1, 2, 3, 4, 5]
'''
