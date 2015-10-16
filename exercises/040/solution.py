a = 0
b = 0
for i in range(101):
        if i % 2 == 0:
            b = a + b
            a = a + 1
print(b)
