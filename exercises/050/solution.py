a = 0
b = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        b = b + a 
    a = a + 1 
print(b)
