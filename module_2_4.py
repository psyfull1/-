numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i > 1:
        for a in range(2, i):
            if i % a == 0:
                is_prime = False
                break
    if i == 1:
        is_prime = False

    if is_prime:
        primes.append(i)
    elif i != 1:
        not_primes.append(i)

print("Primes:", primes)
print("Not Primes:", not_primes)
