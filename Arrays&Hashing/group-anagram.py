from typing import List
from collections import defaultdict

class Solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        """
        Return list of groups of anagrams.

        Parameters
        ----------
        strs : List[str]
            List of strings.

        Returns
        -------
        List[List[str]]
            Groups of anagrams.

        Complexity
        ----------
        Time:  O(n * m)
        Space: O(n * m)
        """

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # a...z
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())


# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
