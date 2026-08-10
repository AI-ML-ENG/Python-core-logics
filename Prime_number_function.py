def prime_num(n):
    m="not_prime"
    l="is_prime"
    if n==1:
        return m
    elif n == 2:
        return l
    elif n%2==0:
        return m
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return m
    return l




