from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Determines whether the input list contains duplicate integer values.

        Parameters
        ----------
        nums : List[int]
            List of integers to be analyzed for duplicates.

        Returns
        -------
        bool
            True if any value appears more than once, False otherwise.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)

        Notes
        -----
        """

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()

    print(sol.hasDuplicate([1, 2, 3, 4]))       # False
    print(sol.hasDuplicate([1, 2, 3, 1]))       # True
    print(sol.hasDuplicate([]))                 # False
    print(sol.hasDuplicate([5, 5, 5, 5]))       # True