from typing import List

class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        """
        Return list if index if nums that added sum the target value: 0.

        Parameters
        ----------
        numbers: List[int]
            Input list of integers.
        
        Returns
        -------
        List[List[int]]
            List of index.

        Complexity
        ----------
        Time:  O(n)
        Space: O(1)
        """

        res = []
        numbers.sort()
        for i, a in enumerate(numbers):
            if i > 0 and a == numbers[i - 1]:
                continue
            l, r = i + 1, len(numbers) - 1
            while l < r:
                three_summ = a + numbers[l] + numbers[r]
                if three_summ > 0:
                    r -= 1
                elif three_summ < 0:
                    l +=1
                else:
                    res.append([a, numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while numbers[l] == numbers[l - 1] and l < r:
                        l += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    # 🧪 Test cases
    tests = [
        {"numbers": [-1, 1, 0, 1, -1], "expected": [[-1, 0, 1]]},
    ]

    for i, test in enumerate(tests, start=1):
        result = sol.threeSum(test["numbers"])
        print(f"Test {i}: Input = {test['numbers']}")
        print(f"Expected = {test['expected']}, Got = {result}")
        print("✅ PASS\n" if result == test["expected"] else "❌ FAIL\n")

