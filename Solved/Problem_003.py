i = 2
n = 600851475143
number = n
while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1

print('Largest prime below {} is: {}'.format(number, n))
