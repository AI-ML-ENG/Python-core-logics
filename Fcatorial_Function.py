
def factorial1(n):
    for i in range(1,n):
        n*= i
    return n

print(factorial1(5))