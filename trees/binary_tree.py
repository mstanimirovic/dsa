from collections import deque


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = BinaryTree(left) if left is not None else None
        self.right = BinaryTree(right) if right is not None else None


def max_width(tree: BinaryTree) -> int:
    if tree is None:
        return 0

    max_width = 0
    q = deque()
    q.append(tree)

    while q:
        level_size = len(q)
        if level_size > max_width:
            max_width = level_size

        for _ in range(level_size):
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    return max_width


def level_order(tree):
    if tree is None:
        return []
    res = []
    q = deque()
    q.append(tree)
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.value)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res


def depth(tree):
    if tree is None:
        return 0
    return max(depth(tree.left), depth(tree.right)) + 1


def inorder(tree):
    if tree is None:
        return
    inorder(tree.left)
    print(tree.value)
    inorder(tree.right)


def preorder(tree):
    if tree is None:
        return
    print(tree.value)
    preorder(tree.left)
    preorder(tree.right)


def postorder(tree):
    if tree is None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.value)


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.left = BinaryTree(2, 4, 5)
    tree.right = BinaryTree(3, 6, 7)
    # tree.inorder()
    # tree.preorder()
    # tree.postorder()
    print(max_width(tree))
