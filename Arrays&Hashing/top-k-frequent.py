from typing import List
from collections import defaultdict

class Solution:
    def topK(self, nums: List[int], k: int) -> List[int]:
        """
        Return list of top k frequent elements.

        Parameters
        ----------
        nums : List[int]
            List of integers.

        Returns
        -------
        List[int]
            List top K frequent elements.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)
        """

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# --- Time execution ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.topK([1,1,1,2,2,3], 2))  # Output: [1,2]