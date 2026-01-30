prices = [7,1,5,3,6,4]


max_profit = 0
min_price = float("inf")



# using brute force approch

for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
        if prices[j] > prices[i]:
            p = prices[j] - prices[i]
            max_profit = max(max_profit, p)
print(max_profit)


#using optimal approch 

for i in range(0, len(prices)):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit,prices[i] - min_price)

print(max_profit)
    
            