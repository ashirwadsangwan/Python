class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data=data, next=None)

    def insert_values(self, array):
        self.head = None
        for data in array:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        linked_list = ""
        while itr:
            linked_list += str(itr.data) + "-->"
            itr = itr.next
        print(linked_list)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_end(10)
    ll.insert_at_end(15)
    ll.print()
    ll.remove_at(2)
    ll.insert_at(0, "mango")
    ll.print()
