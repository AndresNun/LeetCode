from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two elements whose sum equals the target.

        Parameters
        ----------
        nums : List[int]
            List of integers.
        target : int
            Desired sum of two numbers from nums.

        Returns
        -------
        List[int]
            List containing the indices of the two numbers that add up to target.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)
        """

        prevHash = {}  # Stores {value: index}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash[n] = i
        return []  # Empty list if no solution found


# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([2, 7, 11, 15], 9))     # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))          # [1, 2]
    print(sol.twoSum([3, 3], 6))             # [0, 1]
    print(sol.twoSum([1, 5, 3, 7], 10))      # [2, 3]
    print(sol.twoSum([1, 2, 3], 7))          # []
