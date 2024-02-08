# Class Variable

class MyClass:
    class_var = 10  # Class variable

    def __init__(self, x):
        self.x = x  # Instance variable

print(MyClass.class_var)  # Output: 10

obj1 = MyClass(5)
obj2 = MyClass(20)

print(obj1.class_var)  # Output: 10
print(obj2.x)  # Output: 20
