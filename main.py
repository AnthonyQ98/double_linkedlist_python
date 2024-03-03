from src.DLList.DLLinkedList import DLLinkedList
from src.DLList.Node import Node

if __name__ == '__main__':
    dll = DLLinkedList()
    print("Is our DL List empty: " + str(dll.is_empty()))

    dll.add(1, "Kimura")
    dll.add(2, "Arm-bar")
    dll.add(3, "Heel hook")
    dll.add(4, "Triangle")
    dll.add(5, "Americana")
    print("Current size " + str(dll.getSize()))

    dll.add(6, "Estima-lock")
    dll.add(7, "Guillotine")

    print("Printing all elements in the list..")
    dll.print_list()

    print("Printng all elements in the list backwards..")
    dll.print_list_backwards()

    dll.remove(4)
    dll.remove(5)

    print("Printing after removal..")
    dll.print_list()
