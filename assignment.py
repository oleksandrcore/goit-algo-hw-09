import timeit


COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    coins = {}
    
    for coin in COINS:
        if (amount // coin) != 0:
            coins[coin] = amount // coin
            amount %= coin
    
    return coins


def find_min_coins(amount):
    coin_counts = {}
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
    
    remaining_amount = amount
    for coin in COINS:
        coin_count = remaining_amount // coin
        if coin_count > 0:
            coin_counts[coin] = coin_count
            remaining_amount -= coin * coin_count
    
    return coin_counts

time1 = timeit.timeit(lambda: find_coins_greedy(113), number=1000)
time2 = timeit.timeit(lambda: find_min_coins(133), number=1000)

print("Час виконання find_coins_greedy(113):", time1)
print("Час виконання find_min_coins(113):", time2)

time1 = timeit.timeit(lambda: find_coins_greedy(56435), number=100)
time2 = timeit.timeit(lambda: find_min_coins(56435), number=100)

print("Час виконання find_coins_greedy(56435):", time1)
print("Час виконання find_min_coins(56435):", time2)
