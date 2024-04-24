# By listing the first six prime numbers: 
# 2,3,5,7,11 and 13
# we can see that the 
# 6th prime is 13

# What is the 10001st prime number?

# find prime numbers
def is_prime(factor):
    # prime numbers can only be divided by themselves and one evenly
    # no evens
    # no previous prime numbers
    
    j = 3

    while j < factor:
        if factor % j == 0: 
            # factor is not prime
            # print ("not a prime" + str(factor))
            return False
        else:
            j+=2
    
    # print ("factor" + str(factor))
    return True
    

# appending to a list could get memory intensive?
# we could iterate a counter and when it gets to 10001 we just return the prime number it found

prime_test = 5
prime_counter = 3

while prime_counter <= 10001:
    if is_prime(prime_test):
        print(str(prime_test) + " is the" + str(prime_counter) + " prime number")
        if prime_counter < 10001:
            prime_counter+=1
            prime_test+=2
        else:
            prime_counter+=1
    else:
        prime_test+=2

print("final result")
print(prime_test)

# 104743