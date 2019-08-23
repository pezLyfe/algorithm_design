# Uses python3
import sys

def get_fibonacci_last_digit(n):
    '''
    The last digit pattern repeats every 60 numbers, so modulo the input with 60 and input the result to the naive algorithm
    '''
    if n <= 60:
        x = n

    else:
        x = (n % 60)

    if x <= 1:
        return x
    
    previous = 0
    current = 1

    for _ in range(x - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
