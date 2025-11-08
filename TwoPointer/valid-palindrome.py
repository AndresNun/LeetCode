from typing import List

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Return True if the string is a valid palindrome.

        Parameters
        ----------
        s: str
            Input string.

        Returns
        -------
        bool 
            True if the string is a valid palindrome, False otherwise.

        Complexity
        ----------
        Time:  O(n)
        Space: O(1)
        """

        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters
            if not self.alphaNum(s[l]):
                l += 1
                continue
            if not self.alphaNum(s[r]):
                r -= 1
                continue

            # Compare characters
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isPalindrom(self, s: str) -> bool:
        """Check if string is palindrome."""
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return s == s[::-1]

    def alphaNum(self, c):
        """Check if character is alphanumeric."""
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )

if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("A man, a plan, a canal: Panama"))  # ✅ True
    print(sol.validPalindrome("race a car"))                     # ❌ False
    print(sol.validPalindrome(" "))                              # ✅ True
    print(sol.validPalindrome("No 'x' in Nixon"))                # ✅ True
