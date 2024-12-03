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
target_username = "zl"   # Username to search for

# Read the database from the file
database = read_database_from_file(file_path)

# Measure execution time
start_time = time.time()
result = linear_search(database, target_username)
end_time = time.time()

# Output the result
if result != -1:
    print(f"Username '{target_username}' found at index {result}.")
else:
    print(f"Username '{target_username}' not found.")

# Print execution time
print(f"Execution time: {end_time - start_time:.6f} seconds")
