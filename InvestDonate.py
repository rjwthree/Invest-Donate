# The 'Asset' function computes the investment's size after the nth year's donation
# The 'Donation' function computes the size of of the nth year's donation
# The 'Sum' function computes the sum of all donations after the nth year's donation

# 'm' is the annualized growth multiplier (e.g., 1.1 indicates 10% growth per year)
# 'k' is the initial investment
# 'q' is the fraction donated after each cycle
# 'n' is the number of years
# 't' is the time spent on each cycle (e.g., 10 indicates a donation every 10 years)

def Asset(m, k, q, n, t = 1):
    if n % t != 0:
        return 'Whoa! The number of years \'n\' must be a multiple of cycle length \'t\'.'
    n /= t # adjust n from number of years to number of cycles
    m **= t # adjust m from growth per year to growth per cycle
    return round(k*(m*(1-q))**n, 2)

def Donation(m, k, q, n, t = 1):
    if n % t != 0:
        return 'Whoa! The number of years \'n\' must be a multiple of cycle length \'t\'.'
    n /= t # adjust n from number of years to number of cycles
    m **= t # adjust m from growth per year to growth per cycle
    return round(k*q*(m*(1-q))**n, 2)

def Sum(m, k, q, n, t = 1):
    if n % t != 0:
        return 'Whoa! The number of years \'n\' must be a multiple of cycle length \'t\'.'
    n /= t # adjust n from number of years to number of cycles
    m **= t # adjust m from growth per year to growth per cycle
    s = 0 # sum of donations starts at 0
    for i in range(1, int(n+1)): # from 1 to n
        s += k*q*(m*(1-q))**i # add each cycle's donation to the sum
    return round(s, 2)
    
    
# Example    
# After 23 years at 20% growth while donating 2% per year, the investment
# has grown from 1000 to about 41600, so the donation is about 830
# The sum of all donations is about 5430
m = 1.2
k = 1000
q = .02
n = 23
print('Asset = ' + str(Asset(m, k, q, n))) # 41626.36
print('Donation = ' + str(Donation(m, k, q, n))) # 832.53
print('Sum of Donations = ' + str(Sum(m, k, q, n))) # 5429.16




# The 'Time' function computes the number of years needed for cumulative
# donations to exceed the initial investment multiplied by a factor 'z'

def Time(m, z, q, t = 1):
    n = s = 0 # number of cycles (n) and sum of donations (s) start at 0
    m **= t # adjusts m from growth per year to growth per cycle
    while s < z: # while the sum of donations (s) is less than the desired amount (z)
        n += 1 # increment n to indicate a cycle
        s += q*(m*(1-q))**n # add the appropriate amount to sum of donations (s)
    return n*t # return the number of years (i.e, cycles multiplied by years per cycle)
    
    
# Example
# At 20% growth and donating 2% per year, it takes 23 years to donate more than 5 times the initial investment
Time(m = 1.2, z = 5, q = .02) # 23










