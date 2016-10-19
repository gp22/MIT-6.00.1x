

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    low = 0
    high = num
    ans = (high + low)//2
    
    while (high - low) > 1:
        if abs(num - base**ans) > abs(num - base**low):
            high = ans
        else:
            low = ans
        ans = (high + low)//2
    return low
    
print(closest_power(4, 1))
    
#For example,
#
#    closest_power(3,12) returns 2
#    closest_power(4,12) returns 2
#    closest_power(4,1) returns 0

