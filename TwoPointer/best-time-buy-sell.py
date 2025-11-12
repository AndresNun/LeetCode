from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Return the max profit for buy and sell stocks

        Parameters
        ----------
        prices: List[int]
            Input list of integers.
        
        Returns
        -------
        Integer 
            Max profit possible.

        Complexity
        ----------
        Time:  O(n)
        Space: O(1)
        """
        
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            # Profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            else:
                l += 1
            r += 1

        return max_profit

     
if __name__ == "__main__":
    sol = Solution()

    # 🧪 Test cases
    tests = [
        {"prices": [7, 1, 5, 3, 6, 4], "expected": 5},
    ]

    for i, test in enumerate(tests, start=1):
        result = sol.maxProfit(test["prices"])
        print(f"Test {i}: Input = {test['prices']}")
        print(f"Expected = {test['expected']}, Got = {result}")
        print("✅ PASS\n" if result == test["expected"] else "❌ FAIL\n")
