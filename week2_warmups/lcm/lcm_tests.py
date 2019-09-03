import random
import time

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_improved(a, b):
    if b == 0:
        return a

    else:
        a_prime = a % b
        return gcd_improved(b, a_prime)

def lcm_improved(a, b):
    '''
    Use the previous exericse to find the greatest comming divisor
    Then multipy a and b and divide by the greatest common divisor to find the least common multiple
    '''
    n = gcd_improved(a, b)
    y = (a * b) // n
    return y

def lcm_test(limit):
    i = 0
    random.seed(a = 0)

    while (i < limit):
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        naive_start = time.time()
        x = lcm_naive(a,b)
        naive_time = time.time() - naive_start

        improved_start = time.time()
        y = lcm_improved(a,b)
        improved_time = time.time() - improved_start

        improvement = naive_time / (improved_time + 0.0000000001)

        if x == y:
            print('test {} passed, inputs are {} , {}'.format(i,a,b))
            print('Improvement of {} x faster '.format(improvement))
            i += 1
        
        else:
            print('test {} failed, inputs are {}, {}'.format(i, a, b))
            print('Naive {}, improved {}'.format(x, y))
            break

lcm_test(20)