#  2520 is the smallest number that can be divided by each of the numbers from 
#  1 to 10
#  without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 
# 1 to 20
# ?

# a loop where we divide the number by each number 1 - 20, return false if it is not evenly divisible by one
# return true if it is and print the number

# function to test is_divisible that takes an int

def is_divisible(test_num):
    # start at 2, go to 20
    i = 2
    while i <= 20:
        if test_num % i != 0:
            return False
        else:
            i+=1
            if i > 17:
                print("i is " + str(i-1))
    return True
    
# script to call function and find the right number

test = False
num = 2520

while test == False:
    if is_divisible(num):
        test = True
        print(num)
    else:
        num +=2
        # print("num is " + str(num))

        