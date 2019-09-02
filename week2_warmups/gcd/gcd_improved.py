# Uses python3
import sys

def gcd_improved(a, b):
    if b == 0:
        return a

    else:
        a_prime = a % b
        return gcd_improved(b, a_prime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_improved(a, b))