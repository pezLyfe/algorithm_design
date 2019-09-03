#python3
import sys

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

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_improved(a, b))