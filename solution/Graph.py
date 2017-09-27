
#following class is to represent a directed graph 
class DirectedGraph():
    #function shall instantiate graph by taking in a list of tuples where each tuple is two nodes, the first node points to the second node 
    def __init__(self, nodetupleArray):
        #for each tuple in array connect the tuple of nodes
        self.initalNode = nodetupleArray[0][0]
        for node, nodeNext in nodetupleArray: 
            node.addNode(nodeNext)
    
    #breadth first search where the target node is passed in as a parameter      
    def bfs(self,targetNode):
        frontier = [[self.initalNode]]
        visited = []
    
        while (len(frontier) != 0):
            path = frontier.pop(0)
            node = path[-1]
            if (node == targetNode):
                return path
      
            elif (node not in visited):
                for nextNode in node.next:
                    new_path = list(path)
                    new_path.append(nextNode)
                    frontier.append(new_path)
          
          
                visited.append(node)