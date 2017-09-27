class Node(): 
    #initial node with a value 
    def __init__(self, value):
        self.value = value
        self.next = []
    #define node to which this node points to
    def addNode(self,nextNode):
        self.next.append(nextNode)
    #print node's value
    def printNode(self):
        print(self.value)
    #print node's connections
    def printConnections(self):
        for i in self.next: 
            print(i.value)
      
            

