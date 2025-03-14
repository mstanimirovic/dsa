
from lists import LinkedList


def test_linked_list_push_back():
    linked_list = LinkedList()
    linked_list.push_back(1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1

def test_linked_list_push_front():
    linked_list = LinkedList()
    linked_list.push_front(2)
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2

def test_linked_list_push_back_multiple():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3

def test_linked_list_push_front_multiple():
    linked_list = LinkedList()
    linked_list.push_front(3)
    linked_list.push_front(2)
    linked_list.push_front(1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3

def test_linked_list_pop_back():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert linked_list.pop_back() == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2

def test_linked_list_pop_front():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert linked_list.pop_front() == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 3

def test_linked_list_pop_front_empty():
    linked_list = LinkedList()
    assert linked_list.pop_front() is None

def test_linked_list_pop_back_empty():
    linked_list = LinkedList()
    assert linked_list.pop_back() is None
