price = [7,1,5,3,6,4]
max_profit = 0

for i in range(0, len(price)):
    for j in range(i+1, len(price)):
        if price[j] > price[i]:
            profit = price[j] - price[i]
            max_profit = max(max_profit, profit)

print(max_profit) 
            
