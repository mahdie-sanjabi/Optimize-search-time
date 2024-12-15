"main.py"
from create_database import start_database, add_username
from BPTree import UserManager, BPlusTree

# Test the implementation
if __name__ == "__main__":
    start_database()

    bptree = BPlusTree(t=4)
    manager = UserManager(bptree, 'usernames.txt')

    while True:
        action = input("Enter '+' to add a username, 'c' to check if a username exists and '00' for exit: ").strip().lower()
        if action == '+':
            username = input("Enter username: ").strip()
            new_manager=manager.add_user(username)
        elif action == 'c':
            username = input("Enter username: ").strip()
            manager.check_username(username)
        elif action == '00':
            answer = input("Do you want to save the changes to the database (y/n)?").strip()
            if answer == 'y':
                add_username(username)
                print("Database saved")
            else:
                print("Not saved")
        else:
            print("Invalid action. Try again.")
