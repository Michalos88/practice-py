"""Implementation of Resizable Array"""


class Array(object):
    """Resizable Array of Fixed Capacity"""
    def __init__(self,
                 size=0):
        if isinstance(size, int) and size >= 0:
            self.size = size
        else:
            raise ValueError("Array's size can't be non-positive or not int!")

        self.data = list()
        self.last_idx = -1

    def __len__(self):
        return self.size

    def get_capacity(self):
        return self.size - (self.last_idx+1)

    def append(self, val):
        # pdb.set_trace()
        if self.size == 0:
            self.data.append(val)
            self.size = 1
            self.last_idx = 0
        elif self.get_capacity() > 0:
            # O(1)
            self.data.append(val)
            self.last_idx += 1
        else:
            # O(n)
            new_data = list()
            self.last_idx = -1
            for i in range(self.size):
                new_data.append(self.data[i])
                self.last_idx += 1
            del self.data
            self.data = new_data
            self.data.append(val)
            self.last_idx += 1
            self.size = self.size * 2

    def prepend(self):
        pass

    def pop(self):
        # O(1)
        if self.last_idx >= 0:
            temp = self.data[self.last_idx]
            del self.data[self.last_idx]
            self.last_idx -= 1
            return temp
        else:
            raise IndexError("Can't pop from empty list")

    def insert(self):
        pass

    def find(self):
        pass

    def resize(self):
        pass

    def is_empty(self):
        return self.last_idx == 0

    def clean(self):
        del self.data
        self.data = list()
        self.last_idx = 0


class ArrayTests(object):
    """A suite of Array Tests"""
    def __init__(self):
        pass

    def run_all(self):
        self.test_size_init()
        self.test_len()
        self.test_append()
        self.test_clean()
        self.test_pop()

    def test_size_init(self):
        # Should accept sizes > 0
        temp = Array(5)
        assert temp.size == 5

        # Should not accept size that's not int
        try:
            temp = Array(3.0)
            raise RuntimeError("float shouldn't be accepted as size of array")
        except ValueError:
            pass

        # Should not accept size < 0
        try:
            temp = Array(-1)
            raise RuntimeError("-1 shouldn't be accepted as size of array")
        except ValueError:
            pass

        print("test_size_init: passed")

    def test_len(self):
        temp = Array(5)
        assert len(temp) == 5
        print("test_len: passed")

    def test_append(self):
        temp = Array()
        temp.append(2)
        temp.append(3)
        assert len(temp) == 2
        assert temp.data == [2, 3]
        temp.append(4)
        assert len(temp) == 4
        assert temp.data == [2, 3, 4]
        temp.append(1)
        temp.append(5)
        assert len(temp) == 8
        assert temp.data == [2, 3, 4, 1, 5]
        print("test_append: passed")

    def test_clean(self):
        temp = Array(5)
        temp.append(2)
        temp.append(3)
        temp.append(4)
        temp.clean()
        assert temp.is_empty()
        print("test_clean: passed")

    def test_pop(self):
        temp = Array(10)
        temp.append(2)
        temp.append(3)
        temp.append(4)
        assert temp.pop() == 4
        assert temp.pop() == 3
        assert temp.pop() == 2

        try:
            temp.pop()
            raise("Should have been empty")
        except IndexError:
            pass

        print("test_pop: passed")


if __name__ == "__main__":
    tests = ArrayTests()
    tests.run_all()
