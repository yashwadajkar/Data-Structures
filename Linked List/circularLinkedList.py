class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def addHead(self, data):
        """
        Add a node with the given data at the beginning of the circular linked list.
        """
        head_node = Node(data)
        if self.head is None:
            # If the list is empty, make the new node the head and point it to itself
            self.head = head_node
            self.head.next = self.head
        self.length += 1

    def addNode(self, data):
        """
        Add a node with the given data at the end of the circular linked list.
        """
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, make the new node the head and point it to itself
            self.head = new_node
            self.head.next = self.head
        else:
            # Traverse to the end and link the last node to the new node
            itr_node = self.head
            while itr_node.next is not self.head:
                itr_node = itr_node.next
            itr_node.next = new_node
            new_node.next = self.head
        self.length += 1

    def insertTail(self, data):
        """
        Alias for addNode. Adds a node with the given data at the end of the circular linked list.
        """
        self.addNode(data)

    def showCircularLinkedList(self):
        """
        Display the circular linked list.
        """
        if self.head is None:
            print("Empty Circular Linked List")
            return

        itr_node = self.head.next
        print(self.head.data, end="---->")
        while itr_node is not self.head:
            print(itr_node.data, end="---->")
            itr_node = itr_node.next
        print(f"Head({itr_node.data})")

    def insertAtIndex(self, index, data):
        """
        Insert a node with the given data at the specified index in the circular linked list.
        """
        if index < 1 or index > self.length + 1:
            print("Invalid index")
            return

        new_node = Node(data)
        itr_node = self.head

        # Traverse to the node before the desired index
        for i in range(index - 2):
            itr_node = itr_node.next

        temp = itr_node.next.next
        itr_node.next = new_node
        new_node.next = temp
        self.length += 1

    def replace_data_at_index(self, data, index):
        """
        Replace the data of the node at the specified index with the given data.
        """
        if index < 1 or index > self.length:
            print("Invalid index")
            return

        itr_node = self.head
        for i in range(index - 1):
            itr_node = itr_node.next
        itr_node.data = data

    def pop(self):
        """
        Remove the last node from the circular linked list.
        """
        if self.head is None:
            print("Cannot pop from an empty list")
            return

        itr_node = self.head
        while itr_node.next.next is not self.head:
            itr_node = itr_node.next
        itr_node.next = self.head
        self.length -= 1

    def deleteHead(self):
        """
        Delete the head node from the circular linked list.
        """
        if self.head is None:
            print("Cannot delete from an empty list")
            return

        itr_node = self.head
        temp_node = self.head.next
        while itr_node.next is not self.head:
            itr_node = itr_node.next
        self.head = temp_node
        itr_node.next = self.head
        self.length -= 1

    def deleteAtIndex(self, index):
        """
        Delete the node at the specified index from the circular linked list.
        """
        if index < 1 or index > self.length:
            print("Invalid index")
            return

        itr_node = self.head
        for i in range(index - 2):
            itr_node = itr_node.next
        temp_node = itr_node.next.next
        itr_node.next = temp_node
        self.length -= 1

    def search(self, value):
        """
        Search for a node with the specified value in the circular linked list.
        """
        itr_node = self.head.next
        count = 0
        if self.head.data == value:
            count += 1
        while itr_node is not self.head:
            if itr_node.data == value:
                count += 1
            itr_node = itr_node.next
        if count >= 1:
            print("Present")
        else:
            print("Not Present")


def main():
    # Create an instance of CircularLinkedList
    l1 = CircularLinkedList()

    # Menu for user interaction
    while True:
        print("\nCircular Linked List Operations:")
        print("1. Add Head")
        print("2. Add Node")
        print("3. Insert Tail (Alias for Add Node)")
        print("4. Show Circular Linked List")
        print("5. Insert at Index")
        print("6. Replace Data at Index")
        print("7. Pop (Remove Last Node)")
        print("8. Delete Head")
        print("9. Delete at Index")
        print("10. Search")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data for the head node: "))
            l1.addHead(data)
        elif choice == 2:
            data = int(input("Enter data for the new node: "))
            l1.addNode(data)
        elif choice == 3:
            data = int(input("Enter data for the new node: "))
            l1.insertTail(data)
        elif choice == 4:
            l1.showCircularLinkedList()
        elif choice == 5:
            index = int(input("Enter index for insertion: "))
            data = int(input("Enter data for the new node: "))
            l1.insertAtIndex(index, data)
        elif choice == 6:
            index = int(input("Enter index for data replacement: "))
            data = int(input("Enter new data: "))
            l1.replace_data_at_index(data, index)
        elif choice == 7:
            l1.pop()
        elif choice == 8:
            l1.deleteHead()
        elif choice == 9:
            index = int(input("Enter index for deletion: "))
            l1.deleteAtIndex(index)
        elif choice == 10:
            value = int(input("Enter value to search: "))
            l1.search(value)
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()