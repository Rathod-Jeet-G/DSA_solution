def maximumProfit(prices):
    n = len(prices)
    mini_profit = float('inf')
    max_profit = 0
    for i in range(n):
        if prices[i] < mini_profit:
            mini_profit = prices[i]
        else:
            max_profit = max(max_profit,prices[i] - mini_profit)
    return max_profit

prices = [7,1,5,3,6,4]
print(maximumProfit(prices))

# ans=0
# i = 0
# j = 1
# while(j<len(prices)):
#     if(prices[i]<prices[j]):
#         ans = max(ans,prices[j]-prices[i])
#         j+=1
#     else:
#         i=j
#         j=i+1
# print(ans)


