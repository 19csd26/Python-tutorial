"""

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

e.g:---->
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""

def missing_char(str, n):
  return str[:n] + str[n+1:]


print(missing_char('kitten', 1))
print(missing_char('kitten', 3))
print(missing_char('kitten', 5))
print(missing_char('kitten', 7))
