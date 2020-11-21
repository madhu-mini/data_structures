class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def print_list(self):
        if self.is_empty():
            print("List is empty.")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end="->")
            temp = temp.next_element
        print(temp.data, "->None")
        return True

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next_element = self.head_node
        self.head_node = new_node
        return self.head_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head_node = new_node
        else:
            temp_node = self.get_head()
            while temp_node.next_element:
                temp_node = temp_node.next_element
            temp_node.next_element = new_node
        return self.head_node

    def search(self, search_value):
        if self.is_empty():
            return False
        temp_node = self.get_head()
        while temp_node:
            if temp_node.data == search_value:
                return True
            temp_node = temp_node.next_element
        return False

    def delete_at_head(self):
        if self.head_node is not None:
            temp_node = self.head_node
            self.head_node = self.head_node.next_element
            temp_node.next_element = None
            return temp_node.data
        return None

    def delete_by_value(self, value):
        if self.is_empty() or not self.search(value):
            return False
        temp_node = self.get_head()
        prev_node = None
        while temp_node:
            if temp_node.data == value:
                if prev_node is None:
                    self.delete_at_head()
                else:
                    prev_node.next_element = temp_node.next_element
                    temp_node.next_element = None
                return True
            prev_node = temp_node
            temp_node = temp_node.next_element
        return False

    def length(self):
        if self.head_node is None:
            return 0
        count = 0
        temp_node = self.head_node
        while temp_node:
            count += 1
            temp_node = temp_node.next_element
        return count

    def reverse(self):
        if self.get_head() is not None:
            temp_node = self.head_node
            prev_node = None
            next_node = None
            while temp_node:
                next_node = temp_node.next_element
                temp_node.next_element = prev_node
                prev_node = temp_node
                temp_node = next_node
            self.head_node = prev_node

    def is_loop(self):
        slow = self.get_head()
        if slow:
            fast = slow.next_element
        while slow and fast and fast.next_element:
            slow = slow.next_element
            fast = fast.next_element.next_element
            if slow == fast:
                return True
        return False

    def find_mid(self):
        if self.is_empty():
            print("Empty List.")
            return
        slow = self.get_head()
        fast = slow.next_element
        while slow and fast and fast.next_element:
            slow = slow.next_element
            fast = fast.next_element.next_element
        return slow.data

    def remove_duplicates(self):
        if self.is_empty():
            print("Empty List.")
            return
        current = self.get_head()
        prev = None
        s = set()
        while current:
            if current.data in s:
                temp_node = current
                prev.next_element = temp_node.next_element
                current = current.next_element
                temp_node.next_element = None
            else:
                s.add(current.data)
                prev = current
                current = current.next_element

    def union(self, new_list):
        if new_list.is_empty():
            return self.head_node
        if self.is_empty():
            return new_list
        head_list = new_list.get_head()
        while head_list.next_element:
            head_list = head_list.next_element
        head_list.next_element = self.get_head()
        new_list.remove_duplicates()
        return new_list

    def intersection(self, new_list):
        if self.is_empty() or new_list.is_empty():
            return None
        intersection_list = LinkedList()
        head = self.get_head()
        while head:
            if new_list.search(head.data):
                intersection_list.insert_at_tail(head.data)
            head = head.next_element
        return intersection_list

    def get_nth_node_from_end(self, pos):
        head = self.get_head()
        while head and pos > 0:
            head = head.next_element
            pos -= 1
        if pos:
            return -1
        temp = self.get_head()
        while temp and head:
            temp = temp.next_element
            head = head.next_element
        return temp.data


def search_recursive(node, value):
    """
    Recursive search for the linked list
    :param node:
    :param value:
    :return:
    """
    if node is None:
        return False
    if node.data == value:
        return True
    return search_recursive(node.next_element, value)


if __name__ == "__main__":
    lst = LinkedList()
    while True:
        print("1. Print linked list.")
        print("2. Check list is empty or not.")
        print("3. Insert at head of Linked List.")
        print("4. Insert at tail of Linked List.")
        print("5. Delete at head of Linked List.")
        print("6. Delete given value in Linked List.")
        print("7. Search in Linked List.")
        print("8. Stop")
        print("\n")
        n = int(input())
        if n == 8:
            print("Execution Done..!!")
            break
        elif n == 1:
            lst.print_list()
        elif n == 2:
            if lst.is_empty():
                print("List is empty.")
            else:
                print("List is not empty.")
        elif n == 3 or n == 4:
            data = int(input("Enter the data to be inserted..!!"))
            if n == 3:
                lst.insert_at_head(data)
            else:
                lst.insert_at_tail(data)
        elif n == 5:
            lst.delete_at_head()
        elif n == 6:
            data = int(input("Enter the data to be deleted..!!"))
            if lst.delete_by_value(data):
                print("Data is deleted.")
            else:
                print("No such value in the list.")
        else:
            data = int(input("Enter the data to be searched..!!"))
            if lst.search(data):
                print("Element found in list.")
            else:
                print("element is not in the list.")
