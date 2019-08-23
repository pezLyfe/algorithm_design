#python3

def calc_fib_better(n):
    i = 0
    a = []
    while i <= n:
        if i == 0:
            a.append(int(0))
        elif i == 1:
            a.append(int(1))
        else:
            a.append(int(a[i-1] + a[i-2]))
        i += 1
    return a[i-1]

n = int(input())
print(calc_fib_better(n))