def exp_by_squaring(a, b, mod):
    """
    Example:
    a = 7, b = 10 = (1010)_2
    a^b = 1 * a^(10)_2 * a^(1000)_2
    """
    res = 1
    while b:
        if b & 1:  # if the last bit of b is 1
            res = (res * a) % mod
        a = (a * a) % mod  # e.g. a^(1)_2 ---> a^(10)_2
        b >>= 1    # b // 2
    return res % mod

print(exp_by_squaring(2,10, 10**7 + 1))   # 1024
