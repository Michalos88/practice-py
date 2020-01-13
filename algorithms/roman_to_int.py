"""Roman Number to Int conversion"""
# As in https://leetcode.com/problems/roman-to-integer/


class RomanNumberConverter(object):
    def __init__(self):
        self.roman_char_to_int = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                    }

    def roman_to_int(self, number: str) -> int:
        if not isinstance(number, str):
            raise TypeError

        sum = 0
        sub_sum = 0
        idx = 0
        n = len(number)

        while idx < n:
            sub_sum += self.roman_char_to_int[number[idx]]
            if idx+1 < n and self.roman_char_to_int[number[idx+1]] > sub_sum:
                sub_sum = self.roman_char_to_int[number[idx+1]] - sub_sum
                idx += 2
            else:
                idx += 1
            sum += sub_sum
            sub_sum = 0
        return sum


class RomanNumberConverterTests(object):
    def run_all(self):
        self.roman_to_int_test()

    def roman_to_int_test(self):
        # Simple - Forward only
        conv = RomanNumberConverter()
        test_cases = ['III', 'X', 'CLV', 'DCL']
        ground_truth = [3, 10, 155, 650]
        assert len(test_cases) == len(ground_truth)
        for idx in range(len(test_cases)):
            assert conv.roman_to_int(test_cases[idx]) == ground_truth[idx]

        # More Complex
        conv = RomanNumberConverter()
        test_cases = ['IV', 'IX', 'XCV', 'MCMXCIV']
        ground_truth = [4, 9, 95, 1994]
        assert len(test_cases) == len(ground_truth)
        for idx in range(len(test_cases)):
            assert conv.roman_to_int(test_cases[idx]) == ground_truth[idx]

        print('roman_to_int_test: success')


if __name__ == "__main__":
    tests = RomanNumberConverterTests()
    tests.run_all()
