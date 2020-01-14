"""Search insert position in a sorted array"""
# as in https://leetcode.com/problems/search-insert-position/


class Solution:
    def search_insert(self, nums: list, target: int) -> int:
        n = len(nums)
        mid = n//2
        left = 0
        right = n-1
        while left <= right:
            mid = (right+left)//2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid

        right = max(right, 0)
        if target > nums[right]:
            return left
        else:
            return right

    def search_binary(self, nums: list, target: int) -> int:
        n = len(nums)
        mid = n//2
        left = 0
        right = n-1
        while left <= right:
            mid = (right+left)//2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid
        return -1


class Tests(object):
    def run_all(self):
        self.search_binary()
        self.search_insert()

    def search_insert(self):
        temp = Solution()
        # present in the array
        assert temp.search_insert([1, 3, 5, 6], 5) == 2
        assert temp.search_insert([1, 3, 5, 6], 1) == 0
        assert temp.search_insert([1, 3, 5, 6], 6) == 3

        # not found in the array
        assert temp.search_insert([1, 3, 5, 6], 2) == 1
        assert temp.search_insert([1, 3, 5, 6], 7) == 4
        assert temp.search_insert([1, 3, 5, 6], 0) == 0
        print("search_insert_test: passed")

    def search_binary(self):
        temp = Solution()
        # present in the array
        assert temp.search_binary([1, 3, 5, 6], 5) == 2
        assert temp.search_binary([1, 3, 5, 6], 1) == 0
        assert temp.search_binary([1, 3, 5, 6], 6) == 3

        # not found in the array
        assert temp.search_binary([1, 3, 5, 6], 2) == -1
        assert temp.search_binary([1, 3, 5, 6], 7) == -1
        assert temp.search_binary([1, 3, 5, 6], 0) == -1
        print("search_binary_test: passed")


if __name__ == "__main__":
    tests = Tests()
    tests.run_all()
