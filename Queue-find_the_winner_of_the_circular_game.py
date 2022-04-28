from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for i in range(n):
            q.append(i + 1)
        count = 0
        while len(q) > 1:
            elem = q.popleft()
            count += 1
            if count % k != 0:
                q.append(elem)
        return q.popleft()