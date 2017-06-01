# dist = set() # sets will only contain unique numbers
#
# for a in range(2, 101):
#     for b in range(2, 101):
#         dist.add(a ** b)
#
# print("Length of set is:", len(dist))
#
# print("Max =", max(dist))

print(len(set(a ** b for a in range(2, 101) for b in range(2, 101))))