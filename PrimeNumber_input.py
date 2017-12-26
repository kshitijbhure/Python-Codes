
def isPrime(n):
    if n==1:
        print ('1 is a special number')
        return False
    for x in range (2,n):
        if n%x==0:
            print ('{} is not a prime number since {} = {} * {}' .format(n,n,x,int(n/x)))
            return False
    else:
        print('{} is a prime number'.format(n))
        return True


print('Enter a Number : ')
n=input()
isPrime(int(n))

