"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

e.g:---->
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""

def diff21(n):
    return abs(n - 21) * (2 if n > 21 else 1)

print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(23))
print(diff21(29))