"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

e.g:---->
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""


def sleep_in(weekday, vacation):
    return not weekday or vacation


print(sleep_in(True, True))
print(sleep_in(True, False))
print(sleep_in(False, True))
print(sleep_in(False, False))