"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

e.g:---->
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

print(near_hundred(100))
print(near_hundred(201))
print(near_hundred(20))
print(near_hundred(101))
