#Airthmetic operator
a = 5
b = 2
print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a power b 


# #relational operator
a = 20
b = 50
print(a == b)  
print(a != b)  
print(a > b)  
print(a < b)  
print(a >= b)  
print(a <= b)  




#Assinment operators
num = 10
num = num + 10 #same this one and 27 one
num += 10
print("num : " , num) 
num = 23
num -= 3
print("num : " , num)
num = 5
num *= 5
print("num : " , num)
num = 2
num /= 4
print("num : " , num)
num = 4
num %= 4
print("num : " , num)
num = 4
num **= 2
print("num : " , num)


#logical operators
print(not True)
print(not False)
a = 20
b = 10
print(not(a > b)) 
val1 = True
val2 = False
print("and operator : " , val1 and val2)
print("or operator : " , val1 or val2)
val1 = True
val2 = True
print("and operator : " , val1 and val2)
print("or operator : " , val1 or val2 )
print("or operator : ", (a == b) or (a > b))


#Type conversion
a = 2
b = 4.25
sum = a + b  # 2.0+4.25 there automatically type has changed fron int to float
print(sum)
# a = "2" 
# b = 4.25
# print(a + b) 
# #so here python did not change the string value so here we will use type casting
a = int("2") 
b = 4.25
print(a + b) 

a = 3.14
a = str(a) 
print(type(a)) 


#INPUT
name = input("enter your name: ") 
print("welcome" , name)  
#output of any input value will always be string but if we want other type here is it how
#like if we want our value in int
val = int(input("enter some value: ")) 
print(type(val), val) 
#float
name = float(input("enter price : ")) 
print(type(name), name)

name = input("enter your name : ")
age = int(input("enter your age : "))
marks = float(input("enter your marks : "))
print("welcome" , name)
print("age = " , age) 
print("marks = " , marks) 

# Question 1: write a program to input two numbers and print their sum
val1 = int(input("number 1 "))
val2 = int(input("number 2 ")) 
print("sum : " , val1 + val2) 

# Question 2: write a program to input side of square and print its area
side = int(input("enter square side : "))
area = side * side
print("area = " , area)
# Question 3: write a program to input 2 floating point numbers and print their average
num1 = float(input("value 1 : "))
num2 = float(input("value 2 : "))
average = (num1 + num2)/2
print("avg = " , average) 

# Question 4: 
a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
print("final answer : " , a >= b)




