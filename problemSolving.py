from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        answer = 0

        for i in range(n):
            if colors[i] != colors[-1]:
                answer = max(answer, n - 1 - i)
            if colors[i] != colors[0]:
                answer = max(answer, i)

        return answer

if __name__ == "__main__":
    colors = [1, 1, 1, 6, 1, 1, 1]
    print(Solution().maxDistance(colors))
