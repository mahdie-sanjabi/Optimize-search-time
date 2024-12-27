import time

def linear_search(database, target):
    """
    Perform a linear search to find a username in the database.
    :param database: List of usernames
    :param target: The username to find
    :return: Index of the username if found, otherwise -1
    """
    for index, username in enumerate(database):
        if username == target:
            return index  # Username found
    return -1  # Username not found


def binary_search(database, target):
    """
    Perform binary search to find a username in the sorted database.
    :param database: Sorted list of usernames
    :param target: The username to find
    :return: Index of the username if found, otherwise -1
    """
    left, right = 0, len(database) - 1
    while left <= right:
        mid = (left + right) // 2
        if database[mid] == target:
            return mid  # Username found
        elif database[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Username not found


def read_database_from_file(file_path):
    """
    Read usernames from a file and return them as a list.
    :param file_path: Path to the file containing usernames
    :return: List of usernames
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


# Example Usage
file_path = "usernames.txt"  # Path to the file containing usernames

# Get target username
target_username = input("Enter the username to search for: ")  # Username to search for

# Read the database from the file
database = read_database_from_file(file_path)

# Measure execution time
start_time_linear_search = time.time()
result_linear_search = linear_search(database, target_username)
end_time_linear_search = time.time()

# Binary search requires the database to be sorted
database.sort()
start_time_binary_search = time.time()
result_binary_search = binary_search(database, target_username)
end_time_binary_search = time.time()

# Output the result
if result_linear_search != -1:
    print(f"Username in linear_search '{target_username}' found at index {result_linear_search}.")
    print(f"Username in binary_search '{target_username}' found at index {result_binary_search}.")
else:
    print(f"Username '{target_username}' not found.")

# Print execution time
print(f"Execution time in linear_search: {end_time_linear_search - start_time_linear_search:.6f} seconds")
print(f"Execution time in binary_search: {end_time_binary_search - start_time_binary_search:.6f} seconds")
