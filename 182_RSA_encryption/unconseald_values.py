p = 71
q = 73

n = p * q
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

# Calculate smallest number of unconseald messages for e
um_min = 100000
for e in values_of_e:
    um = 0 # unconseald messages
    for m in range(0, n):
        if m**e % n == m: # if encypted message is same as message
            um += 1
        if um > um_min:
            break
    if um_min > um:
        um_min = um
        print(um_min)
