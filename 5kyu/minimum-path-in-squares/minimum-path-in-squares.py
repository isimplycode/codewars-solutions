def min_path(grid, x, y):
    dp=[[float('inf')]*len(grid[0]) for i in range(len(grid))]
    dp[0][0]=grid[0][0]
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if (i): dp[i][j]=dp[i-1][j]
            if (j): dp[i][j]=min(dp[i][j],dp[i][j-1])
            dp[i][j]+=grid[i][j]
            if (j==x and i==y):
                return dp[i][j]-grid[0][0]
    return -1
