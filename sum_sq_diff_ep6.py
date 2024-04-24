# The sum of the squares of the first ten natural numbers is,
#  1sq + 2sq .... 10sq = 385

# The square of the sum of the first ten natural numbers is,
# (1+2...10)sq = 55sq = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# square each natural number up to, and including, 100, sum that
num = 1
num_sum = 0

while num <= 100:
    num_sum+= num * num
    num +=1

# add natural nums, sq
nat_num = 1
nat_num_sum = 0

while nat_num <= 100:
    nat_num_sum+=nat_num
    nat_num+=1

sq_nat_num_sum = nat_num_sum * nat_num_sum

# subtract
answer = sq_nat_num_sum - num_sum

print(answer)