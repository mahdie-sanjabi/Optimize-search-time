class Node:
    """A node in the B+ Tree"""
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []        # Stores the keys in the node
        self.children = []    # Stores the children (if non-leaf node)

class BPlusTree:
    """B+ Tree for storing and searching usernames"""
    def __init__(self, t=4):  # t is the minimum degree of the tree
        self.root = Node(is_leaf=True)
        self.t = t

    def search(self, key, node=None):
        """Search for a key in the tree"""
        if node is None:
            node = self.root
        for i, item in enumerate(node.keys):
            if key < item:
                if node.is_leaf:
                    return False
                else:
                    return self.search(key, node.children[i])
            elif key == item:
                return True
        if node.is_leaf:
            return False
        else:
            return self.search(key, node.children[-1])

    def insert(self, key):
        """Insert a key into the tree"""
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = Node(is_leaf=False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        """Insert into a node that is not full"""
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        """Split a full child node"""
        t = self.t
        node = parent.children[index]
        mid = t - 1
        new_node = Node(is_leaf=node.is_leaf)
        parent.keys.insert(index, node.keys[mid])
        parent.children.insert(index + 1, new_node)

        # Move keys and children to the new node
        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        if not node.is_leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

class UserManager:
    """Manage usernames with B+ Tree and hashing"""
    def __init__(self):
        self.tree = BPlusTree(t=4)  # Initialize the B+ tree
        self.hash_map = {}          # Hash map for fast existence checks

    def add_user(self, username):
        """Add a new username"""
        if username in self.hash_map:
            print(f"Username '{username}' already exists!")
        else:
            self.hash_map[username] = True  # Add to hash map
            self.tree.insert(username)      # Add to B+ tree
            print(f"Username '{username}' added successfully!")

    def check_username(self, username):
        """Check if a username exists"""
        if self.tree.search(username):  # Search in the B+ tree
            print(f"Username '{username}' exists!")
        else:
            print(f"Username '{username}' does not exist!")

# Test the implementation
if __name__ == "__main__":
    manager = UserManager()
    while True:
        action = input("Enter 'add' to add a username, or 'check' to check if a username exists: ").strip().lower()
        username = input("Enter username: ").strip()

        if action == 'add':
            manager.add_user(username)
        elif action == 'check':
            manager.check_username(username)
        else:
            print("Invalid action. Try again.")
