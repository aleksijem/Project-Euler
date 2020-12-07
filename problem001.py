NUM = 999


def sum(n: int):
    return n * (n + 1) // 2


def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a: int, b: int):
    return a * b // gcd(a, b)


sum3 = 3 * sum(NUM // 3)
sum5 = 5 * sum(NUM // 5)
sum15 = lcm(3, 5) * sum(NUM // lcm(3, 5))

print(sum3 + sum5 - sum15)
