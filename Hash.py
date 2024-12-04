import time

def create_hash_table(database):
    """
    Create a hash table from a list of usernames.
    :param database: List of usernames
    :return: Hash table (dictionary) mapping usernames to their indices
    """
    hash_table = {}
    for index, username in enumerate(database):
        hash_table[username] = index
    return hash_table

def read_database_from_file(file_path):
    """
    Read usernames from a file and return them as a list.
    :param file_path: Path to the file containing usernames
    :return: List of usernames
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def search_in_hash_table(hash_table, target):
    """
    Search for a username in the hash table.
    :param hash_table: Hash table containing usernames
    :param target: The username to find
    :return: Index of the username if found, otherwise -1
    """
    return hash_table.get(target, -1)


# Example Usage
if __name__ == "__main__":
    file_path = "usernames.txt"  # Path to the file containing usernames
    target_username = "zigzag"   # Username to search for

    # Read the database from the file
    database = read_database_from_file(file_path)

    # Create a hash table and measure time
    start_time = time.perf_counter()
    hash_table = create_hash_table(database)
    end_time = time.perf_counter()

    # Search for the target username and measure time
    search_start_time = time.perf_counter()
    result = search_in_hash_table(hash_table, target_username)
    search_end_time = time.perf_counter()

    # Output the result
    if result != -1:
        print(f"Username '{target_username}' found at index {result}.")
    else:
        print(f"Username '{target_username}' not found.")

    # Print execution times
    print(f"Hash table creation time: {end_time - start_time:.6f} seconds")
    print(f"Search execution time: {search_end_time - search_start_time:.9f} seconds")