from typing import List

class Solution:
    def containerWater(self, height: List[int]) -> int:
        """
        Return the max area possible with most water

        Parameters
        ----------
        numbers: List[int]
            Input list of integers.
        
        Returns
        -------
        Integer 
            Max area possible.

        Complexity
        ----------
        Time:  O(n)
        Space: O(1)
        """
        res = 0
        l, r = 0, len(height) - 1

        while l<r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
            

if __name__ == "__main__":
    sol = Solution()

    # 🧪 Test cases
    tests = [
        {"height": [1, 2, 3, 4, 5], "expected": 6},
    ]

    for i, test in enumerate(tests, start=1):
        result = sol.containerWater(test["height"])
        print(f"Test {i}: Input = {test['height']}")
        print(f"Expected = {test['expected']}, Got = {result}")
        print("✅ PASS\n" if result == test["expected"] else "❌ FAIL\n")
