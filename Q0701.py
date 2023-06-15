"""
Create a python class with following properties:
1. private class attribute
2. public class attribute
3. instance attribute
4. initializer method
5. string representation method [__str__()]
"""

class MyClass:
    __private_attr = "Private attribute"

    public_attr = "Public attribute"
    def __init__(self, instance_attr):
        
        self.instance_attr = instance_attr
    def __str__(self): 
        return f"MyClass instance with instance_attr={self.instance_attr}"


obj = MyClass("Instance value")
print(obj.public_attr) 
print(obj.instance_attr) 
print(obj)  

