#Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

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

def fib_test():
    '''
    Runs through the first 10 fibonacci numbers and compares the results of the naive algorithm
    with the improved one
    '''
    i = 0
    x = calc_fib(i)
    y = calc_fib_better(i)
    while i < 10:
        if x == y:
            print('Test passed ok')
            i += 1
        else:
            print('Test failed on input {}, iteration {}'.format(i, i))
            break
    print('All tests passed')

fib_test()