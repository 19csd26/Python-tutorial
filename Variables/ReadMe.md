# Types of Variables in Python

In Python, variables can be categorized into different types based on their scope and lifetime. Understanding these types is essential for writing efficient and maintainable code.

# Note: These are the main types of variables in Python, each with its own scope and usage. Understanding them is crucial for writing clear and effective Python code.

## 1. Local Variables

Local variables are defined within a function and have local scope, meaning they can only be accessed within that function.

Example:
```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
```
## 2. Global Variables

Global variables are defined outside of any function or class and have global scope, meaning they can be accessed from anywhere in the code.

Example:
```python
x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10

```
## 3. Nonlocal Variables

Nonlocal variables are used in nested functions and are declared in the enclosing function's scope. They are neither local nor global and can be modified within nested functions.

Example:
```python
def outer_function():
    x = 10  # Local variable of outer_function

    def inner_function():
        nonlocal x  # Using nonlocal to access the variable from the outer function
        x = 20  # Modifying the value of x from outer_function within inner_function
        print("Inner:", x)

    inner_function()
    print("Outer:", x)

outer_function()
```
## 4. Instance Variables

Instance variables are bound to an instance of a class and are defined within the constructor method (__init__) of the class. They are prefixed with self.

Example:
```python
class MyClass:
    def __init__(self, x):
        self.x = x  # Instance variable

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1.x)  # Output: 5
print(obj2.x)  # Output: 10
```
## 5. Class Variables

Class variables are shared among all instances of a class. They are defined within the class but outside of any method and are prefixed with the class name.

Example:
```python
class MyClass:
    class_var = 10  # Class variable

    def __init__(self, x):
        self.x = x  # Instance variable

print(MyClass.class_var)  # Output: 10

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1.class_var)  # Output: 10
print(obj2.class_var)  # Output: 10

```

