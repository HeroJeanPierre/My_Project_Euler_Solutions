def fact(n):
    for i in range(1, n):
        n *= i
    return n

def s(n):
    m = 1
    while fact(m) % n != 0:
       m += 1
    return m


sum = 0
for i in range(2, 500):
        print(str(s(i)))

print ("The sum is:", sum)

