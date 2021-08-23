def isHappy1(n: int) -> bool:
    def progress(n):
        s = 0
        divisor = 10
        while n != 0:
            m = n % divisor
            s += m**2
            n //= divisor
            if n == 0:
                yield s
                if s != 1:
                    s, n, divisor = 0, s, 10
                else:
                    break

    def progress2(n):
        i = 1
        for s in progress(n):
            if i % 2 == 0:
                yield s
            i += 1

    for s1, s2 in zip(progress(n), progress2(n)):
        if s1 and s2 and s1 == s2:
            return False
    return True

def isHappy2(n: int) -> bool:
    s = 0
    divisor = 10
    while n != 0:
        m = n % divisor
        s += m**2
        n //= divisor
        if n == 0:
            if s > 10:
                s, n, divisor = 0, s, 10
            else:
                return s in [1, 7, 10]