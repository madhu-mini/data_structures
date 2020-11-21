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

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_element = self.head_node
        self.head_node = new_node
        return self.head_node

    def insert_at_tail(self, value):
        # Write - Your - Code
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
