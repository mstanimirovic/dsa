from trees import binary_tree


def test_depth():
    tree = binary_tree.BinaryTree(1)
    tree.left = binary_tree.BinaryTree(2, 4, 5)
    tree.right = binary_tree.BinaryTree(3, 6, 7)
    assert binary_tree.depth(tree) == 3


def test_depth_with_empty_tree():
    tree = None
    assert binary_tree.depth(tree) == 0


def test_depth_with_single_node():
    tree = binary_tree.BinaryTree(1)
    assert binary_tree.depth(tree) == 1


def test_max_width():
    tree = binary_tree.BinaryTree(1)
    tree.left = binary_tree.BinaryTree(2, 4, 5)
    tree.right = binary_tree.BinaryTree(3, 6, 7)
    assert binary_tree.max_width(tree) == 4


def test_max_width_with_single_node():
    tree = binary_tree.BinaryTree(1)
    assert binary_tree.max_width(tree) == 1


def test_max_width_with_empty_tree():
    tree = None
    assert binary_tree.max_width(tree) == 0


def test_level_order():
    tree = binary_tree.BinaryTree(1)
    tree.left = binary_tree.BinaryTree(2, 4, 5)
    tree.right = binary_tree.BinaryTree(3, 6, 7)
    assert binary_tree.level_order(tree) == [[1], [2, 3], [4, 5, 6, 7]]


def test_level_order_with_empty_tree():
    tree = None
    assert binary_tree.level_order(tree) == []


def test_level_order_with_single_node():
    tree = binary_tree.BinaryTree(1)
    assert binary_tree.level_order(tree) == [[1]]
