prev = 1
curr = 1
next = 2
sum = 0

while(True):
    if next > 4000000:
        break
    elif(next % 2 == 0):
        sum += next

    print(curr)
    
    prev = curr
    curr = next
    next = prev + curr

print('\nThe sum of the even numbered Fib numbers below 4,000,000 is:', sum)
