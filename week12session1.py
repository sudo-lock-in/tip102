def energy_on_nth_day(n):
    # similar to fibonacci
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1 
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] 
    return dp[n]

# Example Usage:

# print(energy_on_nth_day(1))
# print(energy_on_nth_day(2))
# print(energy_on_nth_day(5))
# print(energy_on_nth_day(7))

def toph_training(cost):
    n = len(cost)
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return min(dp[n - 1], dp[n - 2])
    

# Example Usage:

# print(toph_training([10, 15, 20]))
# print(toph_training([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

def aang_wins(n):
    pass

