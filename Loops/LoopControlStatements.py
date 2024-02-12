# Using break
for i in range(10):
    if i == 5:
        break
    print(i)  # Will print 0 to 4

# Using continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Will print odd numbers from 1 to 9

# Using pass
for i in range(5):
    pass  # Do nothing, just pass
