from src.DLList.Node import Node


class DLLinkedList:
    head, last, size, curr = None, None, 0, None

    def __init__(self, head=None, last=None, size=0, curr=None):
        self.head = head
        self.last = last
        self.size = size
        self.curr = curr

    def is_empty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def __set_current(self, index):
        self.curr = self.head
        for i in range(1, index):
            self.curr = self.curr.getNextNode()

    def get(self, index):
        self.__set_current(index)
        return self.curr

    def remove(self, index):
        if self.size > 0:
            if index == 1:
                self.head = self.head.getNextNode()
                self.head.setPrevNode(None)
            elif index == self.size:
                self.last = self.last.getPrevNode()
                self.last.setNextNode(None)
            else:
                self.__set_current(index)
                prev = self.curr.getPrevNode()
                next_node = self.curr.getNextNode()
                prev.setNextNode(next_node)
                next_node.setPrevNode(prev)
            self.size -= 1
        else:
            print("There is no nodes in the DL List. Can't removed " + index + " index")

    def add(self, index, element):
        if self.size == 0:
            new_node = Node(element, None, None)
            self.head = new_node
            self.last = new_node
        elif index == 1:
            new_node = Node(element, None, None)
            new_node.setNextNode(self.head)
            self.head.setPrevNode(new_node)
            self.head = new_node
        elif index == self.size+1:
            new_node = Node(element, None, None)
            new_node.setPrevNode(self.last)
            self.last.setNextNode(new_node)
            self.last = new_node
        else:
            self.__set_current(index)
            new_node = Node(element, None, None)
            new_node.setNextNode(self.curr)
            self.prev = self.curr.getPrevNode()
            new_node.setPrevNode(self.prev)
            self.prev.setNextNode(new_node)
            self.curr.setPrevNode(new_node)
        self.size += 1

    def print_list(self):
        for i in range(self.size):
            self.__set_current(i+1)
            print(self.curr.getElement())

    def print_list_backwards(self):
        for i in range(self.size):
            self.__set_current((self.size - i))
            print(self.curr.getElement())

