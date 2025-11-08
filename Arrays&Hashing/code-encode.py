from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Return encoded string.

        Parameters
        ----------
        strs : List[str]
            List of Strings.

        Returns
        -------
        str
            Encoded string.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        """
        Return decoded List of strings.

        Parameters
        ----------
        s : str
            Encoded string.

        Returns
        -------
        List[str]
            Decoded list of strings.

        Complexity
        ----------
        Time:  O(n)
        Space: O(n)
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# --- Execution example ---
if __name__ == "__main__":
    sol = Solution()
    words = ["hello", "world", "#hash#", ""]
    encoded = sol.encode(words)
    print("Encoded:", encoded)
    decoded = sol.decode(encoded)
    print("Decoded:", decoded)