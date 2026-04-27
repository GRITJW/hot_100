def row(a, b):
    if b < 0:
        ans = 1 / a
        d  = 1 / a
        l = 1
        if l < :
            ans *= ans
            l *= 2
        else:
            ans *= d
    elif b > 0:
        ans = a
        for _ in range(b-1):
            ans *= a
    else:
        return 1
    return ans
a = 2
b = 3
print(row(2, -3))
