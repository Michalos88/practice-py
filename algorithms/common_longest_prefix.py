class Solution:
    def longestCommonPrefix(self, strs: list) -> str:

        count = len(strs)
        if count < 1:
            return ""
        elif count == 1:
            return strs[0]

        # Find shortest length
        n = 0
        for word in strs:
            n = min(n, len(word))

        prev = strs[0][0]
        prefix = []
        for idx in range(n):
            for word in strs:
                if word[idx] != prev:
                    return "".join(prefix)
            prefix.append(prev)
            prev = strs[0][idx+1]
        return "".join(prefix)
