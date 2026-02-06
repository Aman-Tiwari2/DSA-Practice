# buy or sell the stocks

price = [7,1,5,3,6,4]
max_profit = 0

for i in range(0, len(price)):
    for j in range(i+1, len(price)):
        if price[j] > price[i]:
            profit = price[j] - price[i]
            max_profit = max(max_profit, profit)

print(max_profit) 


prices = [7,1,5,3,6,4]

mini_price = float('inf')
max_profit = 0

for price in prices:
    mini_price = min(mini_price, price)
    max_profit = max(max_profit, price - mini_price)

print(max_profit)
            
