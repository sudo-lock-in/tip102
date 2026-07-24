def energy_on_nth_day(n):
    # similar to fibonacci
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

