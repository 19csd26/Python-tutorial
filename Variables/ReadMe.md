# Types of Variables in Python

In Python, variables can be categorized into different types based on their scope and lifetime. Understanding these types is essential for writing efficient and maintainable code.

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
