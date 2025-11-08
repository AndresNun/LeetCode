from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Return index of nums that add into the target value.

        Parameters
        ----------
        numbers: List[int]
            Input list of integers (sorted ascending).
        
        target: int
            Target sum value.

        Returns
        -------
        List[int]
            List of 1-based indices.

        Complexity
        ----------
        Time:  O(n)
        Space: O(1)
        """

        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


if __name__ == "__main__":
    sol = Solution()

    # 🧪 Test cases
    tests = [
        {"numbers": [2, 7, 11, 15], "target": 9, "expected": [1, 2]},
        {"numbers": [2, 3, 4], "target": 6, "expected": [1, 3]},
        {"numbers": [-1, 0], "target": -1, "expected": [1, 2]},
        {"numbers": [1, 2, 3, 4, 4, 9, 56, 90], "target": 8, "expected": [4, 5]},
    ]

    for i, test in enumerate(tests, start=1):
        result = sol.twoSum(test["numbers"], test["target"])
        print(f"Test {i}: Input = {test['numbers']}, Target = {test['target']}")
        print(f"Expected = {test['expected']}, Got = {result}")
        print("✅ PASS\n" if result == test["expected"] else "❌ FAIL\n")

