class Solution:
    def fib(self, n: int) -> int:
        buff = dict()
        buff[0], buff[1] = 0, 1
        i = 2
        while i <= n:
            buff[i] = buff[i-1] + buff[i-2]
            i += 1
        return buff[n]