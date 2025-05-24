from typing import List


class Solution:

    @staticmethod
    def maximumHappinessSum(happiness: List[int], k: int) -> int:
        """

        @param happiness: List of happiness once we pick a happiness the unpicked happiness decrease by 1
        @param k: Maximum Selections we can make
        @return: Sum of maximum happiness
        """
        if not k:
            return 0

        n = len(happiness)

        happiness.sort(reverse=True)

        current = 0
        visited = 0

        # dp = [(x - i) for (x, i) in zip(happiness, range(n))]  # O(n)
        for i in range(k + 1):  # (n)
            happiness[i] = happiness[i] - i
            if happiness[i] <= 0:
                break

            current += happiness[i]

        return current


happiness = [1, 2, 2, 3]
k = 3
happiness1 = [0, 1, 2]
k1 = 2
obj = Solution()
print(obj.maximumHappinessSum(happiness, k))
print(obj.maximumHappinessSum(happiness1, k1))
happiness2 = [2, 3, 4, 5]
k2 = 1
print(obj.maximumHappinessSum(happiness2, k2))
print(Solution.maximumHappinessSum(happiness, k))
