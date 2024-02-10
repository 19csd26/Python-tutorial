# Python Data Types

This README file provides an overview of the different data types available in Python along with code examples.

## 1.Numeric Types

### int
Integer numbers, e.g., 5, -3, 0.

```python
x = 5
y = -3
z = 0
```
### float
Floating-point numbers, e.g., 3.14, -0.001, 2.0.

```python
pi = 3.14
temperature = -0.001
height = 2.0
```
## 2.Sequence Types

### list
Ordered collection of items, mutable.

```python
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
```
### tuple
Ordered collection of items, immutable.

```python
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
```
### range
Represents a sequence of numbers, often used for looping.

```python
# Create a range from 0 to 10 (exclusive) with step 1
my_range = range(0, 10)
print(list(my_range))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a range from 1 to 10 (exclusive) with step 2
my_range = range(1, 10, 2)
print(list(my_range))  # Output: [1, 3, 5, 7, 9]
```
## 3.Text Sequence Type

### str
Represents a string of characters.

```python
name = "Alice"
message = 'Hello, World!'
```
## 4.Mapping Type

### dict
Collection of key-value pairs.

```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
## 5.Set Type

### set
Unordered collection of unique items, mutable.

```python
unique_numbers = {1, 2, 3, 4, 5}
```
### frozenset
Unordered collection of unique items, immutable.

```python
immutable_set = frozenset({1, 2, 3})
```
## 6.Boolean Type

### bool
Represents Boolean values, either True or False

```python
is_raining = True
is_sunny = False
```
## 7.Binary Types

### bytes
Represents a sequence of bytes, immutable.

```python
binary_data = b'hello'
```
### bytearray
Mutable version of bytes.

```python
mutable_binary_data = bytearray(b'hello')
```
### memoryview
Provides a memory view of a sequence of bytes.

```python
mv = memoryview(b'hello')
```
## 8.None Type:

### None
Represents the absence of a value or a null value.

```python
no_value = None
```
