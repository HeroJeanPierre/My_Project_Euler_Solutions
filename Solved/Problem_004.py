def isPalindrome(num):
    numStr = str(num)
    # # This is an acceptable solution too, the bottom one is mine though
    # so I am keep that
    if numStr == numStr[::-1]:
        return True
    else:
        return False
    
    # for i in range(int(len(numStr)/2)):
    #     if (numStr[i] != numStr[-(i + 1)]):
    #         return False        
    # return True

current = 0
largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        current = i*j

        if(isPalindrome(current)):
            if(current > largest):
                largest = current

print('The largest palindrome that is a product of two 3-digit numbers is:', largest)

# Commented out solution: 0.46s user 0.00s system 99% cpu 0.459 total
# My solution:            0.81s user 0.00s system 99% cpu 0.819 total
