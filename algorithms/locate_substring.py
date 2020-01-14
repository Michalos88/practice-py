"""Implementation of C's strStr"""
# as in https://leetcode.com/problems/implement-strstr/


class Solution(object):
    def locate_substring(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        # O(n*m)
        for start in range(n-m+1):
            if haystack[start] == needle[0]:
                match = True
                for step in range(1, m):
                    if haystack[start+step] != needle[step]:
                        match = False
                        break
                if match:
                    return start
        return -1


class Tests(object):
    def run_all(self):
        self.locate_substring_test()

    def locate_substring_test(self):
        temp = Solution()
        assert temp.locate_substring('hello', 'll') == 2
        assert temp.locate_substring('hello', 'hello') == 0
        assert temp.locate_substring('hello', 'o') == 4
        assert temp.locate_substring('hello', 'h') == 0

        # No common substring
        assert temp.locate_substring('aaaaa', 'bba') == -1
        assert temp.locate_substring('aaaaa', 'aaab') == -1
        assert temp.locate_substring('a', 'aaab') == -1
        assert temp.locate_substring('', '') == 0
        assert temp.locate_substring('', 'a') == -1
        assert temp.locate_substring('bbb', 'aaa') == -1
        print('locate_substring_test: passed')


if __name__ == "__main__":
    tests = Tests()
    tests.run_all()
