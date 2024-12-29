import hashlib


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        hashes = []
        for i in range(self.hash_count):
            hash_result = int(hashlib.md5(f"{item}{i}".encode()).hexdigest(), 16)
            hashes.append(hash_result % self.size)
        return hashes

    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))


def read_database_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

if __name__ == "__main__":
    bf = BloomFilter(size=10000, hash_count=5)

    file_path = "usernames.txt"

    usernames = read_database_from_file(file_path)
    for username in usernames:
        bf.add(username)

    username_to_check = input("Enter a username to check: ")

    if bf.check(username_to_check):
        print(f"The username '{username_to_check}' may be in the database.")
    else:
        print(f"The username '{username_to_check}' is definitely not in the database.")
