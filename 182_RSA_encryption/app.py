from math import gcd

p = 1009
q = 3643

φ = (p - 1) * (q - 1)

# Calculate possible values of e
possible_values_e = set()
for e in range(2, φ):
    if gcd(e, φ) == 1:
        possible_values_e.add(e)


# Calculate number of unconcealed messages for each e
sum_e_for_uc = {}
for e in possible_values_e:
    um = ((1 + gcd(e-1, p-1)) * (1 + gcd(e-1, q-1)))
    
    # Add e to sum for corresponding count of unconsealed messages
    if um in sum_e_for_uc .keys():
        sum_e_for_uc[um] += e
    else:
        sum_e_for_uc[um] = e

# sum for smallest unconsealed count
print(sum_e_for_uc[min(sum_e_for_uc .keys())])
