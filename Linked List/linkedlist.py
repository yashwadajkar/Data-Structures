class Node:
    def __init__(self, data=None):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head node and length tracker
        self.head = None
        self.length = 0

    def add_head(self, data):
        # Add a new head node to the linked list
        new_head = Node(data)
        self.head = new_head
        self.length += 1

    def add_node(self, data):
        # Add a new node to the end of the linked list
        new_node = Node(data)
        if self.length == 0:
            print("Please add a head first")
        elif self.length == 1:
            self.head.next = new_node
            self.length += 1
        else:
            itr_node = self.head
            while itr_node.next is not None:
                itr_node = itr_node.next
            itr_node.next = new_node
            self.length += 1

    def insert_tail(self, data):
        # Insert a new node at the end of the linked list
        if self.head is None:
            print("Please add a head node first")
        else:
            itr_node = self.head
            new_tail = Node(data)
            while itr_node.next is not None:
                itr_node = itr_node.next
            itr_node.next = new_tail
            self.length += 1

    def show_linked_list(self):
        # Display the elements of the linked list
        if self.head is None:
            print("The linked list is empty")
        itr_node = self.head
        while itr_node is not None:
            print(itr_node.data, end="--->")
            itr_node = itr_node.next
        print("None")

    def insert_at_index(self, data, index):
        # Insert a new node at a specified index in the linked list
        if index < 1 or index > self.length + 1:
            print("Invalid index")
            return
        itr_node = self.head
        new_node = Node(data)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            for i in range(index - 2):
                itr_node = itr_node.next
            new_node.next = itr_node.next
            itr_node.next = new_node
        self.length += 1

    def replace_data_at_index(self, data, index):
        # Replace the data of a node at a specified index in the linked list
        if index < 1 or index > self.length:
            print("Invalid index")
            return
        itr_node = self.head
        for i in range(index - 1):
            itr_node = itr_node.next
        itr_node.data = data

    def pop(self):
        # Remove and return the last node in the linked list
        if self.head is None:
            print("Cannot pop from an empty linked list")
            return None

        if self.length == 1:
            popped_data = self.head.data
            self.head = None
        else:
            itr_node = self.head
            while itr_node.next.next is not None:
                itr_node = itr_node.next
            popped_data = itr_node.next.data
            itr_node.next = None

        self.length -= 1
        return popped_data

    def delete_head(self):
        # Remove the head node from the linked list
        if self.head is not None:
            temp = self.head.next
            self.head = temp
            self.length -= 1

    def delete_at_index(self, index):
        # Remove a node at a specified index from the linked list
        if index < 1 or index > self.length:
            print("Invalid index for deletion")
            return

        if index == 1:
            self.head = self.head.next
        else:
            itr_node = self.head
            for i in range(index - 2):
                itr_node = itr_node.next
            itr_node.next = itr_node.next.next

        self.length -= 1

    def search(self, value):
        # Search for a value in the linked list and print if present or not
        itr_node = self.head
        while itr_node is not None:
            if itr_node.data == value:
                print("Present")
                return
            itr_node = itr_node.next

        print("Not Present")

def main():
    linked_list = LinkedList()

    while True:
        print("\nLinked List Operations:")
        print("1. Add Head")
        print("2. Add Node")
        print("3. Insert Tail")
        print("4. Show Linked List")
        print("5. Insert at Index")
        print("6. Replace Data at Index")
        print("7. Pop")
        print("8. Delete Head")
        print("9. Delete at Index")
        print("10. Search")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = int(input("Enter data for the head node: "))
            linked_list.add_head(data)
        elif choice == "2":
            data = int(input("Enter data for the new node: "))
            linked_list.add_node(data)
        elif choice == "3":
            data = int(input("Enter data for the tail node: "))
            linked_list.insert_tail(data)
        elif choice == "4":
            linked_list.show_linked_list()
        elif choice == "5":
            data = int(input("Enter data for the new node: "))
            index = int(input("Enter the index to insert at: "))
            linked_list.insert_at_index(data, index)
        elif choice == "6":
            data = int(input("Enter new data: "))
            index = int(input("Enter the index to replace data: "))
            linked_list.replace_data_at_index(data, index)
        elif choice == "7":
            popped_data = linked_list.pop()
            if popped_data is not None:
                print(f"Popped data: {popped_data}")
        elif choice == "8":
            linked_list.delete_head()
        elif choice == "9":
            index = int(input("Enter the index to delete: "))
            linked_list.delete_at_index(index)
        elif choice == "10":
            value = int(input("Enter the value to search: "))
            linked_list.search(value)
        elif choice == "0":
            print("Program Exited")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()