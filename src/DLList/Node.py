class Node:
    element = None
    nextNode, prevNode = None, None

    def __init__(self, element, nextNode, prevNode):
        self.element = element
        self.nextNode = nextNode
        self.prevNode = prevNode

    # setters
    def setElement(self, element):
        self.element = element

    def setNextNode(self, nextNode):
        self.nextNode = nextNode

    def setPrevNode(self, prevNode):
        self.prevNode = prevNode

    # getters
    def getElement(self):
        return self.element

    def getNextNode(self):
        return self.nextNode

    def getPrevNode(self):
        return self.prevNode
