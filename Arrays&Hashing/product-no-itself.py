from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Return encoded string.

        Parameters
        ----------
        nums : List[str]
            List of Integers.

        Returns
        -------
        str
            Encoded List of Integers.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Basic case
        ([1, 2, 3, 4], [24, 12, 8, 6]),

        # Case with one zero
        ([0, 1, 2, 3], [6, 0, 0, 0]),

        # Case with two zeros (everything becomes 0)
        ([0, 1, 2, 0], [0, 0, 0, 0]),

        # Case with negative numbers
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),

        # Case with identical numbers
        ([2, 2, 2, 2], [8, 8, 8, 8]),

        # Single element case
        ([5], [1]),

        # Two elements case
        ([2, 3], [3, 2]),

        # Large numbers
        ([100, 200, 300, 400], [24000000, 12000000, 8000000, 6000000]),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.productExceptSelf(nums)
        print(f"Test {i}: nums={nums}")
        print(f"Expected: {expected}")
        print(f"Got     : {result}")
        print("✅ PASSED\n" if result == expected else "❌ FAILED\n")
