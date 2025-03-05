def staircase(n, p):
    if n <= 0 or n >= 0:
        return "\n".join([" " * (n - i) + f"{p}" * i for i in range(1, n + 1)])
