from main import *
from Hash import *

import matplotlib.pyplot as plt
import random

# Experiment
data_sizes = [10_000, 100_000, 1_000_000, 10_000_000]
linear_times = []
binary_times = []
hash_table_times = []

for size in data_sizes:
    # Generate random dataset
    database = [f"user{i}" for i in range(size)]
    target = database[random.randint(0, size - 1)]  # Random target

    # Linear Search
    start = time.time()
    linear_search(database, target)
    linear_times.append(time.time() - start)

    # Binary Search
    sorted_database = sorted(database)
    start = time.time()
    binary_search(sorted_database, target)
    binary_times.append(time.time() - start)

    # Hash Table Search
    hash_table = create_hash_table(database)
    start = time.time()
    search_in_hash_table(hash_table, target)
    hash_table_times.append(time.time() - start)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, linear_times, label="Linear Search", marker='o')
plt.plot(data_sizes, binary_times, label="Binary Search", marker='s')
plt.plot(data_sizes, hash_table_times, label="Hash Table Search", marker='^')

plt.title("Comparison of Search Algorithms", fontsize=14)
plt.xlabel("Number of Records", fontsize=12)
plt.ylabel("Execution Time (seconds)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()