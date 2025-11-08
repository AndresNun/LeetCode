from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines whether the two input strings are anagrams.

        Parameters
        ----------
        s: String
        t: String
            Strings to be analyzed.

        Returns
        -------
        bool
            True if are valid anagram, False otherwise.

        Complexity
        ----------
        Time:  O(n) -> O(s + t)
        Space: O(n) -> O(s + t)
        """

        # Look same length
        if len(s) != len(t):
            return False
        
        # Create Hasmaps occurrences per char
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True


# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("listen", "silent"))      # ✅ True
    print(sol.isAnagram("anagram", "nagaram"))    # ✅ True
    print(sol.isAnagram("rat", "car"))            # ❌ False
    print(sol.isAnagram("aacc", "ccac"))          # ❌ False
    print(sol.isAnagram("", ""))                  # ✅ True
