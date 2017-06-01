xx = open('try.txt', 'r')
text = xx.read().split("\n")

dic = set()
print(text)
for i in text:
    dic.add(eval(str(i.split("==")[0])))
    #input()

print(sum(dic))









# string = ""
#
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "==", "*"]
# sum = 0
# dic = set()
#
# debug = False
#
#
# def fact(n):
#     for i in range(1, n):
#         n *= i
#     return n
#
#
# def swap(i, j):
#     tmp = a[i]
#     a[i] = a[j]
#     a[j] = tmp
#
#     # a[i] = a[i] + a[j]
#     # a[j] = a[i] - a[j]
#     # a[i]= a[i] - a[j]
#
#
# def check_val():
#     string = ""
#     for i in a:
#         string += values[i]
#     # print(string)
#     try:
#         if (eval(string)):
#             print(string)
#             dic.add(eval(string.split("==")[1]))
#
#     except:
#         pass
#
# x = fact(len(a))
# for k in range(x):
#
#     if k % 100000 == 0: print("-----------", a,"----", 100*k/x,"% Finsihed")
#     maxIndex = 0
#     leastIndex = len(a) - 1;
#     for i in range(len(a) - 1):
#         if a[i] < a[i + 1] and i < len(a) - 1:
#             maxIndex = i
#         if (debug): print("Max i = \t", maxIndex)
#
#     for i in range(maxIndex, len(a)):
#         if a[i] > a[maxIndex] and a[i] <= max(a):
#             leastIndex = i
#         if (debug): print("Least i = \t", leastIndex)
#
#     swap(leastIndex, maxIndex);
#     if (debug): print()
#     if (debug): print(a)
#     if (debug): print("Sorting...")
#     for i in range(0, len(a) - maxIndex):
#         for j in range(maxIndex + 1, (len(a) - 1) - i):
#             if a[j] > a[j + 1]:
#                 swap(j, j + 1)
#
#     if (debug): input()
#     check_val()
#
# print(sum(dic))
