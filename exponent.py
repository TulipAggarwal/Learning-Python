#Learning exponent function in python

from unittest import result
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result
print("The answer is: " +str(raise_to_power(3,2)))