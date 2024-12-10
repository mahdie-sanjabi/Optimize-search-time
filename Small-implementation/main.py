from create_database import start_database
from BPTree import UserManager, BPlusTree

# Test the implementation
if __name__ == "__main__":
    start_database()

    bptree = BPlusTree(t=4)
    manager = UserManager(bptree, 'usernames.txt')

    while True:
        action = input("Enter '+' to add a username, 'C' to check if a username exists and '00' for exit: ").strip().lower()
        if action == '+':
            username = input("Enter username: ").strip()
            manager.add_user(username)
        elif action == 'C':
            username = input("Enter username: ").strip()
            manager.check_username(username)
        elif action == '00':
            break
        else:
            print("Invalid action. Try again.")
