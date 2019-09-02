# Uses python3
import sys
import random
import time

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_improved(a, b):
    if b == 0:
        return a

    else:
        a_prime = a % b
        return gcd_improved(b, a_prime)

def gcd_test(limit):
    i = 0
    random.seed(a = 0)

    while (i < limit):
        a = random.randint(0, 1000000)
        b = random.randint(0, 1000000)

        naive_start = time.time()
        x = gcd_naive(a,b)
        naive_time = time.time() - naive_start

        improved_start = time.time()
        y = gcd_improved(a,b)
        improved_time = time.time() - improved_start

        improvement = naive_time / improved_time

        if x == y:
            print('test {} passed, inputs are {} , {}'.format(i,a,b))
            print('Improvement of {} x faster '.format(improvement))
            i += 1
        
        else:
            print('test {} failed, inputs are {}, {}'.format(i, a, b))
            break

gcd_test(20)