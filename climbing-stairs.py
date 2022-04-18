def climbStairs(n: int) -> int:
    # Store number of ways indexed at number of stairs
    ways = []
    ways.append(0)
    ways.append(1)
    ways.append(2)

    if n > 2:
        for i in range(3, n+1):
            ways_i = ways[i-1] + ways[i-2]
            ways.append(ways_i)
    return(ways[n])
