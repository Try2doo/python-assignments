"""
Perform the addition operations between the following data types and check whether the code runs successfully or not:
int and int (Example: 5 + 5)
int and float (Example: 5 + 5.5)
float and float (Example: 5.5 + 5.5)
str and str (Example: 'hello' + 'world')
int and str (Example: 5 + 'hello')
"""

a = 5
b = 5
c = 5.5
d = 'hello'
e = 'world'
print(a + b)  # 10, int and int  
print(a + c)  #10.5,int and float
print(c + c)  #11.0,  float and float
print(d + e)  #helloworld,  str and str
print(a + d)  # int and str  error, int and str  error int and str  error)
#print(5 + 'hello')  #unsupported operand type(s) for +: 'int' and 'str'


