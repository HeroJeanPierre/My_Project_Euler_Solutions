import sys

total = 0
for i in range(1, 354294):
    fifthSum = 0
    # sys.stdout.write(str(c) + '\n')
    for j in str(i):
        fifthSum += int(j) ** 5
    if fifthSum == i:
        total += fifthSum

print(total)
input()