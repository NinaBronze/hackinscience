suite = [1, 2]
if len(suite) < 9:
    suite.append(suite[-2] + suite[-1])
    print(suite, end=', ')
elif len(suite) == 10:
    print(suite)
