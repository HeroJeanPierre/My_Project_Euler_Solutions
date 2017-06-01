pence = [1, 2, 5, 10, 20, 50, 100, 200]


def how_many_ways(x):
    sum = 0
    numberOfWays = 0

    for first in range(int(x / pence[0]) + 1):
        for second in range(int(x / pence[1]) + 1):
            if (first * pence[0] + second * pence[1]) == x:
                print(first, second)
                numberOfWays += 1
                break
            elif (first * pence[0] + second * pence[1]) > x:
                sum = 0
                break
            for third in range(int(x / pence[2]) + 1):
                if (first * pence[0] + second * pence[1] + third * pence[2]) == x:
                    print(first, second, third)
                    numberOfWays += 1
                    break
                elif (first * pence[0] + second * pence[1] + third * pence[2]) > x:
                    sum = 0
                    break
                for fourth in range(int(x / pence[3]) + 1):
                    if (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3]) == x:
                        print(first, second, third, fourth)
                        numberOfWays += 1
                        break
                    elif (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3]) > x:
                        sum = 0
                        break
                    for fifth in range(int(x / pence[4]) + 1):
                        if (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4]) == x:
                            print(first, second, third, fourth, fifth)
                            numberOfWays += 1
                            break
                        elif (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4]) > x:
                            sum = 0
                            break
                        for sixth in range(int(x / pence[5]) + 1):
                            if (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4] + sixth * pence[5]) == x:
                                print(first, second, third, fourth, fifth, sixth)
                                numberOfWays += 1
                                break
                            elif (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4] + sixth * pence[5]) > x:
                                sum = 0
                                break
                            for seventh in range(int(x / pence[6]) + 1):
                                if (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4] + sixth * pence[5] + seventh * pence[6]) == x:
                                    print(first, second, third, fourth, fifth, sixth, seventh)
                                    numberOfWays += 1
                                    break
                                elif (first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4] + sixth * pence[5] + seventh * pence[6]) > x:
                                    sum = 0
                                    break
                                for eighth in range(int(x / pence[7]) + 1):

                                    if ( first * pence[0] + second * pence[1] + third * pence[2] + fourth * pence[3] + fifth * pence[4] + sixth * pence[5] + seventh * pence[6] + eighth * pence[7]) == x:
                                        print(first, second, third, fourth, fifth, sixth, seventh, eighth)
                                        numberOfWays += 1
                                        break
    print(numberOfWays)


how_many_ways(50)


def nway(total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0
    if total % c == 0: count += 1
    for amount in range(0, total, c):
        count += nway(total - amount, coins)
    return count

## print(nway( 200, (1,2,5,10,20,50,100,200)))