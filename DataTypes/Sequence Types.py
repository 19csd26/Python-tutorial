#2.Sequence Types:
#I.list: Ordered collection of items, mutable.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

#II.tuple: Ordered collection of items, immutable.
coordinates = (10, 20)
colors = ('red', 'green', 'blue')

#III.range: Represents a sequence of numbers, often used for looping.
# Create a range from 0 to 10 (exclusive) with step 1
my_range = range(0, 10)
print(list(my_range))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a range from 1 to 10 (exclusive) with step 2
my_range = range(1, 10, 2)
print(list(my_range))  # Output: [1, 3, 5, 7, 9]
