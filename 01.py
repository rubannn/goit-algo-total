class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" → ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            if not sorted_head or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_head

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# Створення списків
llist1 = LinkedList()
llist1.append(3)
llist1.append(1)
llist1.append(5)

llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)

# Друк початкових списків
print("List 1:")
llist1.print_list()

print("List 2:")
llist2.print_list()

# Реверсування першого списку
llist1.reverse()
print("\nReversed List 1:")
llist1.print_list()

# Сортування списків
llist1.insertion_sort()
llist2.insertion_sort()
print("\nSorted List 1:")
llist1.print_list()
print("Sorted List 2:")
llist2.print_list()

# Об'єднання відсортованих списків
merged = LinkedList.merge_sorted_lists(llist1, llist2)
print("Merged Sorted List:")
merged.print_list()
