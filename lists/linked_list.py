
from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head: Optional[Node] = head
        self.tail: Optional[Node] = tail
        self.length = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        return self.length

    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_back(self):
        value = None
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            value = self.tail.value
            self.tail = current
            self.tail.next = None

        self.length -= 1
        return value

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_front(self):
        value = None
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next
        self.length -= 1
        return value


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    # print(linked_list.pop_back())  # Output: 3
    # print(linked_list.pop_back())  # Output: 2
    # print(linked_list.pop_back())  # Output: 1
    # print(linked_list.pop_front()) # Output: None
    for value in linked_list:
        print(value)
    linked_list.pop_front()
    for value in linked_list:
        print(value)
