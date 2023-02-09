import pandas as pd
def solution(n):
    k = {'1':'2'}
    pd.DataFrame([[1,2,3],[1,2,3]])
    dp = [0] * (n+1)
    dp[1] = 1
    if n>1:
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
    
    return dp[n] % 1234567