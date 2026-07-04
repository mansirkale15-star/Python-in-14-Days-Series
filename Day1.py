#Variables, here a, b and c are variables 
a = 5
b = 50
c = a+b
print(c)
print(a,b,c)

""" Datatypes, there are 5 main types of Datatypes in python they are numeric[int,float,complex], sequence[str,list,tuple], set[set,frozenset], mapping[dict], boolean[true,false]"""
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type(10,))
print("Hello" * 3)
print(type({1}))

#input/output 
#in input we can take text as well as no. input from the user 

#text input
a = input("Enter your name: ")
print(a)
#no. input
b = int(input("Enter your number: "))
print(b)

print("Hello",a,"Welcome to my world")
print("Okay! so your number is",b,"I'll call you soon")

#TypeCasting 
#Typecasting means changing the datatype
""" so there are 5 test case in type casting """
#str -> int
n = "20"
print(n)
print(type(n))
n1 = int(n)
print(type(n1))

#str -> float
print(type(n))
n2 = float(n)
print(type(n2))

#float -> int
m = 3.4
print(m)
print(type(m))
n3 = int(m)
print(n3)
print(type(n3))

#int -> str
print(n3)
print(type(n2))
n4 = str(n3)
print(n4)
print(type(n4))


#operators
"""There are 5 types of operators """
#Arithematic operator
a = 2
b = 4
c = a+b
d = a-b
e = a*b
f = a/b
g = a//b
h = a%b
i = a**b
print(a,b,c,d,e,f,g,h,i)

#<-----------------------------program 1----------------------------->
#Build a mini calcultor

#<----------------------------program 2------------------------------>
#temperature converter