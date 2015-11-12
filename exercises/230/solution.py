import itertools
import sys
from is_prime import is_prime

for i in itertools.count(100000000):
    if is_prime(i):
        print(i)
        sys.exit()
