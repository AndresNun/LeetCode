from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Return longest consecutive sequence.

        Parameters
        ----------
        nums : List[int]
            List of Integers.

        Returns
        -------
        int
            Longest sequence.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)
        """
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if (num -1) not in num_set:
                current_streak = 1
                while (num + current_streak) in num_set:
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Standard case
        ([100, 4, 200, 1, 3, 2], 4),          # Sequence: 1,2,3,4
        
        # Sequence with negatives
        ([0, -1, 1, 2, -2, -3, 3], 7),        # Sequence: -3,-2,-1,0,1,2,3

        # Duplicate numbers
        ([1, 2, 2, 3], 3),                    # Sequence: 1,2,3

        # Non-consecutive numbers
        ([10, 30, 20], 1),                    # Only single elements
        
        # Single number
        ([5], 1),

        # Empty list
        ([], 0),

        # Already sorted sequence
        ([1, 2, 3, 4, 5], 5),

        # Large unordered consecutive block
        ([9,1,4,7,3,-1,0,5,8,-1,6], 7),       # Sequence: 3,4,5,6,7,8,9
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.longestConsecutive(nums)
        print(f"Test {i}: nums={nums}")
        print(f"Expected: {expected}")
        print(f"Got     : {result}")
        print("✅ PASSED\n" if result == expected else "❌ FAILED\n")
