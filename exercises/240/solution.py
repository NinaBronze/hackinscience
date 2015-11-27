suite = [1, 2]
fin = 10
while len(suite) < fin:
    suite.append(suite[-1] + suite[-2])
for i in suite[0:9]:
    print(i, end=', ')
print(suite[-1], ".")
