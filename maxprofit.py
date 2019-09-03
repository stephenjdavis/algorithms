def get_max_profit(A):
    data = []
    max_profit = 0
    n = len(A)
    # The day's price (will end up being our day to buy)
    i = 0
    # The day's prices we might compare info with... (will end up being our day to sell)
    j = 0
    for i in range(n):
        for j in range(n):
            #... but only if they come after each day we're comparing.
            if (j > i): 
                # ... we set our max profit and update it when the difference between 
                # sell and buy is the greatest
                if ((A[j] - A[i] > max_profit)):
                    max_profit = A[j] - A[i]
                    buy_date = i + 1
                    sell_date = j + 1
    data.append(max_profit)
    data.append(buy_date)
    data.append(sell_date)
    return data

max_profit = str(get_max_profit([4,777,456,7,346,345])[0])
buy_date = str(get_max_profit([4,777,456,7,346,345])[1])
sell_date = str(get_max_profit([4,777,456,7,346,345])[2])
print ('Max profit is ' + max_profit + ', bought on day ' + buy_date + ' and sold on day ' + sell_date)
