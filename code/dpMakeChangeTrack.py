def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount :
                coinCount = minCoins[cents - j] + 1
                newCoin = j

        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change

    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]

    # coinsUsed is a list of the coins used to make change
    coinsUsed = [0] * (amnt + 1)

    # coinCount is the minimum number of coins used to make change for the
    # amount corresponding to the position in the list.
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requests")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()




