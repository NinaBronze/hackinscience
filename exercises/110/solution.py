import sys

operateur = '+-*/%^'
a = sys.argv[1]
op = sys.argv[2]
b = sys.argv[3]
    
if len(sys.argv) < 4:
    print("usage: solution.py a_number (an_operator +-*/%^) a_number")

elif operateur.find(op) != 0:
    print("usage: solution.py a_number (an_operator +-*/%^) a_number")
    

else:

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print('input error')
        sys.exit()

    if op == '+':
        print(a + b)

    if op == '-':
        print(a - b)

    if op == '*':
        print(a * b)

    if op == '/':
        if b == 0:
            print('input error')
            sys.exit()
        else:
            print(a / b)

    if op == '^':
        print(a ** b)

    if op == '%':
        print(a % b)
