"""Hash Table Implementation"""


class HashTable(object):
    """
    Hash Table Object
    """
    def __init__(self):
        """
        Initialize Hash Table
        """
        self.key_space = 2096
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        """
        Put
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        """
        Return the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Remove the mapping of the specified value key
        if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


class Bucket(object):
    """
    Bucket with Linear Probing
    """
    def __init__(self):
        """
        Initialize Bucket
        """
        self.bucket = []

    def update(self, key, value) -> None:
        """
        Update the value in a bucket if key found
        """
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Return the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Remove the mapping of the specified value key
        if this map contains a mapping for the key
        """
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
