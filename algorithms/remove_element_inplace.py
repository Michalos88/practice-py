"""Removing values from array in-place"""


class Remover(object):
    "Methods for removing objects from data structures"
    def val_from_list(self, nums: list, val: int) -> int:
        n = len(nums)
        idx = 0
        while idx < n:
            if nums[idx] == val:
                nums[idx], nums[n-1] = nums[n-1], nums[idx]
                n -= 1
            else:
                idx += 1
        return n, nums


class RemoverTests(object):
    def run_all(self):
        self.val_from_list_test()

    def val_from_list_test(self):
        test_cases = [([3, 2, 2, 3], 3), ([0, 1, 2, 2, 3, 0, 4, 2], 2)]
        remove = Remover()
        for test_case in test_cases:
            target = test_case[1]
            nums = test_case[0]
            front, nums = remove.val_from_list(nums, target)
            for val in nums[:front]:
                if val == target:
                    raise RuntimeError('val_from_list_test: failed')

        print('val_from_list_test: passed')


if __name__ == "__main__":
    tests = RemoverTests()
    tests.run_all()
