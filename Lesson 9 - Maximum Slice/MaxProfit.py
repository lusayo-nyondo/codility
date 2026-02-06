# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) < 2:
        return 0

    max_profit = 0
    minimum_buy_price = A[0]

    for price in A:
        if price < minimum_buy_price:
            minimum_buy_price = price
        
        current_profit = price - minimum_buy_price

        if current_profit > max_profit:
            max_profit = current_profit
    
    return max_profit