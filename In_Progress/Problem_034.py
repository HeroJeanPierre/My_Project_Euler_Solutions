
print ("Working")
def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total




totalSum = 0
for i in range(10000000):
    sum = 0
   # print("i =",i)
    for ch in (str(i)):
        sum += fact(int(ch))
      #  print("Factorial of", ch, "is", fact(int(ch)))
        if sum > i:
            break
    if sum == i:
        print(sum," is equal to the factorial of its parts")
        totalSum += i
        #print(i)

print(totalSum)