#python3

import random
import time

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fib_digit_better(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1

    if n <= 60:
        x = n

    else:
        x = (n % 60)

    for _ in range(x - 1):
        previous, current = current, previous + current

    return current % 10

def show_all_fib_digits(n):
    i = 0

    while i < n:
        print('Input {}, output {}'.format(i, get_fibonacci_last_digit_naive(i)))
        i += 1

def fib_digit_test(limit):
    
    i = 0
    random.seed(a=0)

    while i < limit:
        n = random.randint(0,300)
        start_naive = time.time()
        x = get_fibonacci_last_digit_naive(n)
        naive_time = time.time() - start_naive

        start_improved = time.time()
        y = get_fib_digit_better(n)
        better_time = time.time() - start_improved

        if x == y:
            print('Test {} passed ok! Input {}'.format(i, n))
            print('Naive time {}, improved time {}'.format(naive_time, better_time))
        else:
            print('Test failed, naive = {}, better = {}, input {}'.format(x, y, n))
            raise('Test failed, exiting')
        
        i+= 1

fib_digit_test(60)