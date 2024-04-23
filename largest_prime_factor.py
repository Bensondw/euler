# the prime factors of 13195 are 5,7,13 and 29

# What is the largest prime factor of 600851475143?

# find the factors
i=3
product = 600851475143
# product = 100
factors = []

def is_prime(factor):
    # prime numbers can only be divided by themselves and one evenly
    # no evens
    # no previous prime numbers
    
    j = 3

    while j < factor:
        if factor % j == 0: 
            # factor is not prime
            print ("not a prime" + str(factor))
            return False
        else:
            j+=2
    
    print ("factor" + str(factor))
    return True
      
testmax = product/2

while i < (testmax):
    if product % i == 0:
        if is_prime(i):
            factors.append(i)
            print(str(i) + "is a prime factor")
        if is_prime(product/i):
            factors.append(product/i)
    i+=2
    testmax = product/i
    print(testmax)

largest_prime = max(factors)

print(largest_prime)

        
    
   
