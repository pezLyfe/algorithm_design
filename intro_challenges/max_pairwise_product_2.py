# Uses python3
'''
The starter file provided by the course used nested for loops to calculate the solution
as a result, the submission failed due to an excessive runtime. The list.sort() method in python works really fast, so use that to order the list and then multiply the largest entry in the list by the second largest entry in the list
'''

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

a.sort()

x = len(a)

result = a[x-1] * a[x-2]

'''for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]
'''

print(result)