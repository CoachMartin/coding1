def isprime(a):

    i = 2
    while i < a:
        if a%i == 0:
            return False
        i = i + 1
    
    return True


print(isprime(7))
print(isprime(4))
print(isprime(30))
print(isprime(20))
print(isprime(19))
print(isprime(13))