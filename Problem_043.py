from itertools import permutations

l = list(permutations(range(10)))

print('Finished making loop')
sum = 0


def find_pent(perm):
    div = [1, 2, 3, 5, 7, 11, 13, 17]

    # print('Perm =', int(''.join(map(str, perm))))
    iteration = 0
    for i in range(1, 8):
        # print(int(''.join(map(str, perm[i:i + 3]))), 'div = ' + str(div[i]))
        if int(''.join(map(str, perm[i:i + 3]))) % div[i] == 0:
            iteration += 1

            if iteration == 7:
                global sum
                sum += int(''.join(map(str, perm)))  # int(''.join(map(str, perm)))
                print('Perm =', int(''.join(map(str, perm))))

                print("Sum =", (sum))

for i in range(len(l)):
    find_pent(l[i])

print("Sum =", sum)
