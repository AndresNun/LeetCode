from typing import List

class Solution:
    def trappingWater(self, height: List[int]) -> int:
        """
        Return the max water that can be trapped

        Parameters
        ----------
        height: List[int]
            Input list of integers.
        
        Returns
        -------
        Integer 
            Max water possible being trapped.

        Complexity
        ----------
        Time:  O(n)
        Space: O(1)
        """
        
        l_wall, r_wall = 0, 0
        n = len(height)
        max_left, max_right = n * [0], n * [0]

        for i in range(n):
            j = -i -1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        sum = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            sum += max(0, pot - height[i])
        return sum

     
if __name__ == "__main__":
    sol = Solution()

    # 🧪 Test cases
    tests = [
        {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], "expected": 6},
    ]

    for i, test in enumerate(tests, start=1):
        result = sol.trappingWater(test["height"])
        print(f"Test {i}: Input = {test['height']}")
        print(f"Expected = {test['expected']}, Got = {result}")
        print("✅ PASS\n" if result == test["expected"] else "❌ FAIL\n")
