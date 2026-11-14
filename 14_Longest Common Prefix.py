class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # ind the shortest string manually
        shortest = strs[0]

        for word in strs:
            if len(word) < len(shortest):
                shortest = word

        # vertical scaning
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return shortest[:i]

        return shortest