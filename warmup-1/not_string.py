"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

e.g:---->
not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(str):
  return str if str.startswith("not") else "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
print(not_string('good'))
print(not_string('not good'))