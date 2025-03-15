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

    def __getitem__(self, key):
        if type(key) is not int:
            return
        elif key >= self.length:
            raise IndexError("getitem index out of range")
        elif key < 0:
            if abs(key) > self.length:
                raise IndexError("getitem index out of range")
            key = self.length + key

        if key == 0:
            return self.head.value
        elif key == self.length - 1:
            return self.tail.value

        current = self.head
        for _ in range(key):
            current = current.next
        return current.value

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

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

    def pop(self, index=-1):
        if self.is_empty():
            raise IndexError("pop from empty linked list")
        elif index >= self.length:
            raise IndexError("pop index out of range")
        elif index < 0:
            if abs(index) > self.length:
                raise IndexError("pop index out of range")
            index = self.length + index

        if index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()

        current = self.head
        for _ in range(index - 1):
            current = current.next
        value = current.next.value
        current.next = current.next.next
        self.length -= 1
        return value

    def remove(self, value):
        if self.is_empty():
            raise ValueError("remove from empty linked list")
        elif self.head.value == value:
            return self.pop_front()
        elif self.tail.value == value:
            return self.pop_back()

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return value
            current = current.next
        raise ValueError("value not found in linked list")

    def insert(self, index, value):
        if index < 0:
            index = self.length + index

        if index == 0:
            self.push_front(value)
            return
        elif index >= self.length:
            self.push_back(value)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.is_empty():
            return "[]"
        current = self.head
        result = "["
        while current.next is not None:
            result += str(current.value) + ", "
            current = current.next
        result += str(current.value) + "]"
        return result


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)

    print(linked_list)
