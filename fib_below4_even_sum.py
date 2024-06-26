
# # Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1
#  and 2 , the first 10 terms will be:
#  1,2,3,5,8,13,21,34,55,89...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

# determine if fibonnaci below 4mil
fib = [1,2]
evens = [2]
i=0

while i < 4000000:
    next = fib[-1] + fib[-2]
    fib.append(next)
    
    if next % 2 == 0:
        evens.append(next)
    i = next
    

# sum it up
sum = 0
for i in evens:
    sum += i


print(sum)