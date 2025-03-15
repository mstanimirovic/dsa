import pytest

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


def test_linked_list_iterator():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    iterator = iter(linked_list)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator, None) is None


def test_linked_list_iterator_empty():
    linked_list = LinkedList()
    iterator = iter(linked_list)
    assert next(iterator, None) is None


def test_linked_list_length():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert linked_list.length == 3
    linked_list.pop_back()
    assert linked_list.length == 2
    linked_list.pop_front()
    assert linked_list.length == 1
    linked_list.pop_front()
    assert linked_list.length == 0


def test_linked_list_length_empty():
    linked_list = LinkedList()
    assert linked_list.length == 0


def test_linked_list_contains():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert 1 in linked_list
    assert 2 in linked_list
    assert 3 in linked_list
    assert 4 not in linked_list


def test_linked_list_contains_empty():
    linked_list = LinkedList()
    assert 1 not in linked_list


def test_linked_list_getitem():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    assert linked_list[0] == 1
    assert linked_list[1] == 2
    assert linked_list[2] == 3
    assert linked_list[-1] == 3
    assert linked_list[-2] == 2
    assert linked_list[-3] == 1


def test_linked_list_getitem_empty():
    with pytest.raises(IndexError):
        linked_list = LinkedList()
        linked_list[0]
