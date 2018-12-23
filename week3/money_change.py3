def money_change(m, ordered_coins):
    amount_coins = 0

    for i in range(len(ordered_coins)):
        amount_coins += m // ordered_coins[i]
        m = m % ordered_coins[i]

    return amount_coins


ordered_coins = [10, 5, 1]

m = int(input())

print(money_change(m, ordered_coins))
