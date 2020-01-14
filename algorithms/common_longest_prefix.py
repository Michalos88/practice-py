"""Longest Common Prefix"""
# as in https://leetcode.com/problems/longest-common-prefix


class Solution(object):
    def longest_common_prefix(self, strs: list) -> str:

        word_count = len(strs)
        if word_count < 1:
            return ""
        elif word_count == 1:
            return strs[0]

        # Find shortest length
        n = len(strs[0])
        for word in strs:
            n = min(n, len(word))
        # If one is empty, then there is no common prefix
        if n == 0:
            return ""

        prev = strs[0][0]
        prefix = []
        for position in range(n):
            prev = strs[0][position]
            for word_id in range(1, word_count):
                word = strs[word_id]
                if word[position] != prev:
                    return "".join(prefix)
            prefix.append(prev)
        return "".join(prefix)


class Tests(object):
    def run_all(self):
        self.longest_common_prefix_test()

    def longest_common_prefix_test(self):
        temp = Solution()

        # True prefix
        test_case = ['flower', 'flow', 'flight']
        assert temp.longest_common_prefix(test_case) == 'fl'

        # True prefix
        test_case = ['runner', 'robot', 'resnet', 'racecar', 'romanian']
        assert temp.longest_common_prefix(test_case) == 'r'

        # No prefix
        test_case = ["dog", "racecar", "car"]
        assert temp.longest_common_prefix(test_case) == ''

        # Single word
        test_case = ["dog"]
        assert temp.longest_common_prefix(test_case) == 'dog'

        # Empty input
        test_case = []
        assert temp.longest_common_prefix(test_case) == ''

        # Array of empty strings
        test_case = ["", ""]
        assert temp.longest_common_prefix(test_case) == ''

        # Array with empty string
        test_case = ["hell", "hello", ""]
        assert temp.longest_common_prefix(test_case) == ''

        # Single characters
        test_case = ["c", "c"]
        assert temp.longest_common_prefix(test_case) == 'c'
        print('longest_common_prefix_test: success')


if __name__ == "__main__":
    tests = Tests()
    tests.run_all()
