"""Sqrt using binary search"""
# as in https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 1
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1


class Tests:
    def run_all(self):
        self.sqrt()

    def sqrt(self):
        sol = Solution()
        assert sol.mySqrt(0) == 0
        assert sol.mySqrt(1) == 1
        assert sol.mySqrt(4) == 2
        assert sol.mySqrt(8) == 2
        assert sol.mySqrt(9) == 3
        assert sol.mySqrt(16) == 4
        assert sol.mySqrt(64) == 8


if __name__ == "__main__":
    tests = Tests()
    tests.run_all()
