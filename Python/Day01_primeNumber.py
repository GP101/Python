def IsPrime( prime, a ):
    isPrime = True
    for i in prime:
        if( a % i == 0 ):
            isPrime = False
            break
    return isPrime

prime = [2,3,5,7]
i = 8
while i < 100:
    b = IsPrime( prime, i)
    if b == True :
        prime.append( i )
    i += 1

print prime
