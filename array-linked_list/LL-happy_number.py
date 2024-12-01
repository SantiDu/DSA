# leetcode, rt 95%, mu 92%

class Solution:
    def isHappy(self, n: int) -> bool:
        # if n in [1, 7]:
        #     return True
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