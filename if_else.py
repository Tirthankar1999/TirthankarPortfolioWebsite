# a=int(input("enter the marks of physics: "))
# b=int(input("enter the marks of mathematics: "))
# if a > b:
#   print("a is greater than b")
# elif a == b:
#    print("a is equal to b")
# elif a < b:
#     print("a is less than b")
# else:
#     print("doesnt matter")              
# c=int(input("enter the marks of chemistry: "))
# d=int(input("Enter d "))
# if(a>b and b>a ):
#     print("a is greatest ")
# elif(b>a and b>c):
#     print("b is greatest ")
# elif(c>a and c>b):
#     print("c is greatest ")  
# elif(d>a and d>b):
#     print("d is greatest")    
# else:
#     print("every nos are equal")    
# if(a>33 and b>33 and c>33 and (a+b+c)/3>=40):
#     print("student is passed")
# elif((a+b+c)/3 > 40):
#      print("student is passed")
# else:
#     print("student is not passed")
#a =input("Enter the post ")
# if("make a lot of money" in a):
#     spam = True
# elif("buy now" in a):
#     spam = True    
# elif("subscribe this" in a):
#     spam = True
# elif("click this" in a):
#     spam = True
# else:
#     spam = False    
        
# if(spam):
#     print("Spam")
# else:
#     print("perfect!")
# if(len(a)<10):
#     print("Perfect")
# else:
#     print("Wrong")   
# b = input("Enter b ")
# c = input("Enter c ")
# d = input("Enter d ")
# list = [b,c,d]
# print(list)
# if(a in list):
#     print("You Got it!")
# else:
#     print("not")    
# if(a>=90 and a<=100):
#     Grade = 'Ex'
# elif(a>=80 and a<=90):
#     Grade = 'A'
# elif(a>=70 and a<=80):
#     Grade = 'B'
# elif(a>=60 and a<=70):
#     Grade = 'C'
# elif(a>=50 and a<=60):
#     Grade = 'D'
# elif(a<50):
#     Grade = 'F'      
# else:
#     print("out of Range")                  
# print(Grade)
# if("Harry" in a):
#     print("Ok")
# else:
#     print("Not Ok")    
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))
if a>b and a>c and a>d:
    print(f"{a} is greatest")
elif b>a and b>c and b>d:
    print(f"{b} is greatest")
elif c>a and c>b and c>d:
    print(f"{c} is greatest")        
elif d>a and d>b and d>a:
    print(f"{d} is greatest")
else:
    print("Every nos are equal")        