class HashTableChaining:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

        # Universal hash parameters
        self.a = 31
        self.b = 17
        self.p = 10**9 + 7

    def _hash(self, key):
        """
        Universal-style hash function.
        """
        return ((self.a * hash(key) + self.b) % self.p) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def load_factor(self):
        return self.size / self.capacity

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"{i}: {bucket}")
        return "\n".join(result)


# =========================
# Manual Testing (Required)
# =========================

if __name__ == "__main__":
    ht = HashTableChaining(capacity=5)

    print("Initial hash table:")
    print(ht)
    print("Load factor:", ht.load_factor())
    print("-" * 40)

    print("Inserting elements...")
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    ht.insert("grape", 40)
    ht.insert("melon", 50)

    print(ht)
    print("Load factor:", ht.load_factor())
    print("-" * 40)

    print("Searching keys:")
    print("apple ->", ht.search("apple"))
    print("banana ->", ht.search("banana"))
    print("cherry ->", ht.search("cherry"))
    print("-" * 40)

    print("Deleting key 'banana'")
    ht.delete("banana")
    print(ht)
    print("Load factor:", ht.load_factor())
