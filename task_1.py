class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted(self, other):
        result = LinkedList()
        l1_current = self.head
        l2_current = other.head

        while l1_current and l2_current:
            if l1_current.data < l2_current.data:
                result.insert_at_end(l1_current.data)
                l1_current = l1_current.next
            else:
                result.insert_at_end(l2_current.data)
                l2_current = l2_current.next

        while l1_current:
            result.insert_at_end(l1_current.data)
            l1_current = l1_current.next

        while l2_current:
            result.insert_at_end(l2_current.data)
            l2_current = l2_current.next

        return result

    def sort(self):
        if self.head is None or self.head.next is None:
            return self

        mid = self._get_middle_node()
        next_to_mid = mid.next
        mid.next = None

        left_half = LinkedList()
        left_half.head = self.head
        right_half = LinkedList()
        right_half.head = next_to_mid

        left_half = left_half.sort()
        right_half = right_half.sort()

        sorted_list = self._merge(left_half, right_half)
        return sorted_list

    def _get_middle_node(self):
        if self.head is None:
            return None

        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

    def _merge(self, left_half, right_half):
        result = LinkedList()
        left_current = left_half.head
        right_current = right_half.head

        while left_current is not None and right_current is not None:
            if left_current.data < right_current.data:
                result.insert_at_end(left_current.data)
                left_current = left_current.next
            else:
                result.insert_at_end(right_current.data)
                right_current = right_current.next

        while left_current is not None:
            result.insert_at_end(left_current.data)
            left_current = left_current.next

        while right_current is not None:
            result.insert_at_end(right_current.data)
            right_current = right_current.next

        return result


# Створення тестових списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_end(7)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
list2.insert_at_end(8)

# Вивід початкових списків
print("Початковий список 1:")
list1.print_list()

print("Початковий список 2:")
list2.print_list()
print()

# Виклик функцій
print("Реверсування першого списку:")
list1.reverse()
list1.print_list()
print()

print("Реверсування другого списку:")
list2.reverse()
list2.print_list()
print()

print("Сортування першого списку:")
sorted_list1 = list1.sort()
sorted_list1.print_list()
print()

print("Сортування другого списку:")
sorted_list2 = list2.sort()
sorted_list2.print_list()
print()

print("Об'єднання двох відсортованих списків:")
merged_list = sorted_list1.merge_sorted(sorted_list2)
merged_list.print_list()
