import sys
import time

t = time.time()
numS = list()
denS = list()
frac = list()

newFrac = ""
swithchable = False;


def check_vals(first, second, num, den):
    oldFrac = "".join(num) + "/" + "".join(den)
    newFra = "".join(num[first]) + "/" + "".join(den[second])

    # sys.stdout.write(newFra + " ")

    try:
        if (eval(oldFrac) == eval(newFra)):
            print("(", oldFrac, " -> ", newFra, ") Works!")
            # input()
    except:
        pass


for denominator in range(10, 100):
    for numerator in range(10, denominator):
        if numerator % 10 == 0 or denominator % 10 == 0:
            continue

        denS = list(str(denominator))
        numS = list(str(numerator))
        frac = "".join(numS) + "/" + "".join(denS)
        # sys.stdout.write(frac + " -> ")

        if numS[0] == denS[0]:
            check_vals(1, 1, numS, denS)
        if numS[1] == denS[0]:
            check_vals(0, 1, numS, denS)
        if numS[0] == denS[1]:
            check_vals(1, 0, numS, denS)
        if numS[1] == denS[1]:
            check_vals(0, 0, numS, denS)
            # print()

print(time.time() - t)

# import time
# t=time.time()
#
# for y in range(1,10):
#     for z in range(y,10):
#         x=float(9)*y*z/(10*y-z)
#         if int(x) == x and y/z < 1 and x<10:
#             print (x, y, z, str(10*y+x)+'/'+str(z+10*x), str(y)+'/'+str(z))
# print (time.time()-t)