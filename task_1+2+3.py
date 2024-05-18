
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def search_max(root):
    if root is None:
        return None
    
    current = root
    while current.right:
        current = current.right
    
    return current.val

def search_min(root):
    if root is None:
        return None
    
    current = root
    while current.left:
        current = current.left
    
    return current.val

def sum(root):
    if root is None:
        return 0
    return root.val + sum(root.left) + sum(root.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root, 5)
root = insert(root, 9)
root = insert(root, 0)
root = insert(root, 1)


print(search_max(root))
print(search_min(root))
print(sum(root))