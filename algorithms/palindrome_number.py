"""Check if a number is a palindrom"""
# As in https://leetcode.com/problems/palindrome-number/
import math


class PalindromeNumber:
    def __init__(self,
                 number: int,
                 check_type: str):
        if isinstance(number, int) and self.is_palindrome(number, check_type):
            self.number = number
        else:
            raise ValueError("This number is not int or palindrome")

    def is_palindrome(self, x: int, check_type):
        if check_type == "numerical":
            return self.is_palindrome_numerical(x)
        elif check_type == "char_comp":
            return self.is_palindrome_char_comp(x)
        else:
            raise RuntimeError('Wrong palindrome check type')

    def is_palindrome_numerical(self, x: int) -> bool:
        """Palindome check - numerical"""
        # Check if negative, return negative, as 121- is not a valid int
        if x < 0:
            return False

        # Check how many digits
        n = 0
        while int(x/(10**n)) >= 10:
            n += 1
        n += 1
        for digit in range(0, math.floor(n/2), 1):
            left = int(int(x % 10**(digit+1))/10**digit)
            right = int(int(x % 10**(n-digit))/10**(n-digit-1))
            if left != right:
                return False
        return True

    def is_palindrome_char_comp(self, x: int) -> bool:
        """Palindome check - compering characters"""
        # Check if negative, return negative, as 121- is not a valid int
        if x < 0:
            return False
        x_mutable = str(x)
        n = len(x_mutable)
        for idx in range(0, math.floor(n/2), 1):
            if x_mutable[idx] != x_mutable[n-idx-1]:
                return False
        return True


class PalindromeNumberTests(object):
    def __init__(self,
                 palindrome_check_type='numerical'):
        self.check_type = palindrome_check_type

    def run_all(self):
        self.input_test()
        self.is_palindrome_test()

    def input_test(self):
        # Wrong Type inputs
        test_cases = ["c", "353-", "11111", 10001.22]
        for x in test_cases:
            try:
                PalindromeNumber(x, self.check_type)
                raise RuntimeError("input_test: failure")
            except ValueError:
                pass
        print("input_test: success")

    def is_palindrome_test(self):
        # True Palindromes - Positve - odd N
        test_cases = [1, 121, 353, 11111, 10001, 22522, 1000110001]
        for x in test_cases:
            try:
                PalindromeNumber(x, self.check_type)
            except ValueError as e:
                print(e)
                raise RuntimeError("is_palindrome_test: failure")

        # True Palindromes - Positve - even N
        test_cases = [1221, 3553, 11, 101101, 225522, 100010010001]
        for x in test_cases:
            try:
                PalindromeNumber(x, self.check_type)
            except ValueError as e:
                print(e)
                raise RuntimeError("is_palindrome_test: failure")

        # False Palindromes - Negative - odd N
        test_cases = [-121, -353, -11111, -10001, -22522]
        for x in test_cases:
            try:
                PalindromeNumber(x, self.check_type)
                raise RuntimeError("is_palindrome_test: failed")
            except ValueError:
                pass

        # False Palindromes - Positive - odd N
        test_cases = [120, 553, 10111, 20201, 23522]
        for x in test_cases:
            try:
                PalindromeNumber(x, self.check_type)
                raise RuntimeError("is_palindrome_test: failed")
            except ValueError:
                pass

        # False Palindromes - Positive - even N
        test_cases = [1201, 5553, 1011, 2222102222, 12344391]
        for x in test_cases:
            try:
                PalindromeNumber(x, self.check_type)
                raise RuntimeError("is_palindrome_test: failed")
            except ValueError:
                pass

        print("is_palindrome_test: success")


if __name__ == "__main__":
    tests = PalindromeNumberTests('numerical')
    tests.run_all()
