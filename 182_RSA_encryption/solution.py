p = 1009
q = 3643

φ = (p - 1) * (q - 1)


# Euclidean algorithm
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


# calculate possible values of e
values_of_e = set()
for e in range(2, φ):
    if gcd(e, φ) == 1:
        values_of_e.add(e)

# calculate number of unconcealed messages for each e
sum_e_for_uc = {}
for e in values_of_e:
    um = ((1 + gcd(e-1, p-1)) * (1 + gcd(e-1, q-1))) # found this formula and it just works...
    
    # add e to sum for corresponding count of unconsealed messages
    if um in sum_e_for_uc.keys():
        sum_e_for_uc[um] += e
    else:
        sum_e_for_uc[um] = e        

answer = sum_e_for_uc[min(sum_e_for_uc.keys())] # finds the smallest number of uncolseald messages which is the key to the sum of e's
print(answer) # sum of smallest unconsealed count
