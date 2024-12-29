# پیاده‌سازی فیلتر بلوم در پایتون

این اسکریپت پایتون یک **فیلتر بلوم** ساده را برای بررسی اینکه آیا یک نام کاربری در یک فایل از نام‌های کاربری وجود دارد یا خیر، پیاده‌سازی می‌کند. این فیلتر از یک آرایه بیتی و چندین تابع هش برای بررسی عضویت استفاده می‌کند. فیلتر بلوم ممکن است خطای **False Positive** داشته باشد، یعنی ممکن است به اشتباه بگوید که یک نام کاربری در مجموعه وجود دارد، در حالی که در واقع وجود ندارد.

## توضیح کد

```python
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
    """
    خواندن نام‌های کاربری از یک فایل و بازگرداندن آن‌ها به صورت یک لیست.
    :param file_path: مسیر فایل حاوی نام‌های کاربری
    :return: لیست نام‌های کاربری
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


# استفاده نمونه
if __name__ == "__main__":
    bf = BloomFilter(size=10000, hash_count=5)

    file_path = "usernames.txt"
    
    # خواندن نام‌های کاربری از فایل و افزودن آن‌ها به فیلتر بلوم
    usernames = read_database_from_file(file_path)
    for username in usernames:
        bf.add(username)

    # درخواست از کاربر برای وارد کردن نام کاربری برای بررسی
    username_to_check = input("Enter a username to check: ")

    # بررسی اینکه آیا نام کاربری وارد شده در فیلتر بلوم موجود است یا نه
    if bf.check(username_to_check):
        print(f"The username '{username_to_check}' may be in the database.")
    else:
        print(f"The username '{username_to_check}' is definitely not in the database.")
