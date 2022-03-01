''''
list is done with third bracket
it has the following features 
duplication AND Ordered is allowed
mutability is allowed(changeble once the value stored)
'''
#a=[1,2,3,3,3,3,4,4,5,5]
# a[1] = 7
# print(a)
'''''
APPEND-
append adds the uservalue in the last index
'''
# a = [1,2,3]
# a.append(4)
# print(a)
'''
insert inserts the user value in the user given index
'''
# a.insert(1,4)
# print(a)
#b= [1,2,3]
# b.insert(1,True)
# print(b)
'''
extend extends the list
'''
# b.extend([4,5,6])
# print(b)
'''
pop removes the value in the given index in bracket
'''
# b.pop(1)
# print(b)
'''
remove removes the value in the bracket
'''
# b.remove(2)
# print(b)
'''
reverse reverse the list
'''
# b.reverse()
# print(b)
'''
sorting the list
'''
#c = [3,2,1]
# c.sort()
# print(c)
'''
clearing the list
'''
# c.clear()
# print(c)
'''
index method gets the index of the no in the parenthesis
'''
#print(a.index(2))
#print(a.count(3))
"unpacking of variables"
# k = [15,26,78]
# x , y , z = k
# print(x)
"we can create a list of value of different types"
# a = ["tirtho", 1 , 9.6 , 7.8888888888]
# print(a)

# import math
# L = [3,1,2,4]
# T = ('A','b','c','d')
# L.sort()
# counter = 0
# for X in T:
#     L[counter]+=ord(X)
#     counter+=1
#     break
# print(math.ceil(max(L)/min(L)))#here index assignment happens like in L in place of 1 66 get stored
# list_1= list([1,2,3])
# print(type(list_1))
# list1 = [3,4,5,20,5]
# print(list1.index(5))#here index of 5 will be pirnted as 2 as first 5 index will be printed from the list
# def increment_items(L,increment):
#     i =0
#     while i < len(L):
#         L[i]+= increment
#         i += 1
# values = [1,2,3]        
# print(increment_items(values,2))        
# print(values)#here values will be modified by the function above as the function is already called in line 89
# list = []
# def example(L):
#     i = 0
#     result = []
#     while i< len(L):
#         result.append(L[i])
#         i = i+3
#     return result    
# print(example(list))    
# veggies = ['apple', 'mango', 'banana', 'papaya']
# veggies.insert(veggies.index('apple'), 'tomato')#hre insert function wont replace apple with tomato, it will just insert tomato at position 0 of list veggies
# print(veggies)
# x = [[0], [1]]
# print((''.join(list(map(str,x)))))
# my_string = 'my_string'
# k = [print(i) for i in my_string if i not in "aeiou"]
# print(k)
# print([[i+j for i in "abc"]for j in "def"])
# [print (1/x) for x in [1,2,3] ]
# k = list(map(lambda x : x** -1, [1,2,3]))
# print(k)
# [print(x**-1) for x in [1,2,3]]
# [print (j) for i in range(2,8) for j in range(i*2,50,i)]
# L = ["good", "oh!", "excellent!", "#450"]
# [print(n) for n in L if n.isalpha() or n.isdigit()]#hre isalpha() method chcks whether every chaarcter in the string is alphabet or not wheras isdigit checks whther every character in the string is digit or not
# list1 = list([1,2,3])
# print(list1.pop())
# print(list1)
# print(type(list1))
# a = ['red','blue','yellow','white','black']
# while a:
#     if len(a) < 3:
#         break
#     print(a.pop())
# print("Done")  
# list1 = ['Harry', 


'''
repeat the sentence until comes 0 in place of 99
'''
# lst = []
# s = '''99 bottles of bear on the wall, 99 bottles of bear.
#   take it down . pass it around . 98 bottles of bear on the wall
#         '''
# lst.append(s)        
# n = 99
# for i in range(98, 0, -1):
#     s = s.replace(str(n-1), str(i-1))
#     s = s.replace(str(n), str(i))
#     n = i
#     lst.append(s)
# print('\n'.join(lst))    
'''
reverse the list like [6,5,4,1,2,3]
'''
# lst2 = [1,2,3,4,5,6]
# n = len(lst2)//2
# lst2 = (lst2[-n:])[::-1] + lst2[:-n]
# print(lst2) 

'''
take a list and skip the nos before and after 2 and print the total of rest of the nos in the list
'''
# list = []
# number = int(input("Enter the no:"))
# n = int(input("Enter the elements"))
# sum = 0
# for i in range(0, n):
#     elements = int(input("Enter the elements: "))
#     list.append(elements)

# truth = [True]*(len(list))
# for i in range(0, len(list)):
#     if list[i] == number:
#         truth[i] = False
#         if i - 1 >= 0:
#             truth[i-1] = False
#         if i + 1 < len(list):
#             truth[i+1] = False
# sum = 0
# for i in range(0, len(list)):
#     if truth[i] == True:
#         sum = sum + list[i]
# print(sum)




# list1 = []
# list = []

# for i in range(4):
#     list1 = []
#     for j in range(3):
#         list1.append(str(i)+','+str(j))
#     list.append(list1)    
# print(list)
    



# list = []
# l = int(input("Enter the length: "))
# for i in range(0,l):
#     elements = int(input("Enter the elements: "))
#     list.append(elements)
# s = str(list)
# for i in list:

#     s = s.replace(str(i),str(2*(i-1)))
# print(s)    






# from tkinter.font import names


# names1 = ['Amir','Bear','Charlton','Daman']
# names2 = names1
# names3 = names1[:]
# print(names3)
# names2[0] = 'Alice'
# names3[1] = 'Bob'
# sum = 0
# for it in (names1, names2,names3):
#     if it[0] == 'Alice':
#         sum += 1
#     if it[1] == 'Bob':
#         sum += 10
# print(sum)        
# print(names3)
# print(names1)
# print(names2)
lst2 = [1,2,3,4,5,6]
n = len(lst2)//2
lst3 = lst2[n:]
print(lst3)