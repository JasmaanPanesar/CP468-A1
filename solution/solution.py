from Graph import *
from rcState import *
from Node import * 
        
#Initializing all states in state space
#state = rcState(mLeft,cLeft,mRight,cRight,boatPos)
state0 = rcState(3,3,0,0,"left")

state1 = rcState(3,1,0,2,"right")
state2 = rcState(2,2,1,1,"right")
state3 = rcState(3,2,0,1,"right")

state4 = rcState(3,2,0,1,"left")

state5 = rcState(3,0,0,3,"right")

state6 = rcState(3,1,0,2,"left")

state7 = rcState(1,1,2,2,"right")

state8 = rcState(2,2,1,1,"left")

state9 = rcState(0,2,3,1,"right")

state10 = rcState(0,3,3,0,"left")

state11 = rcState(0,1,3,2,"right")

state12 = rcState(0,2,3,1,"left")
state13 = rcState(1,1,2,2,"left")
#state14 is the goal state 
state14 = rcState(0,0,3,3,"right")

state15 = rcState(0,1,3,2,"left")

#create nodes where values are the various states in the state space 
node0 = Node(state0)
node1 = Node(state1)
node2 = Node(state2)
node3 = Node(state3)
node4 = Node(state4)
node5 = Node(state5)
node6 = Node(state6)
node7 = Node(state7)
node8 = Node(state8)
node9 = Node(state9)
node10 = Node(state10)
node11 = Node(state11)
node12 = Node(state12)
node13 = Node(state13)
node14 = Node(state14)
node15 = Node(state15)

#Initialize the graph represented by the following adjacency list 
#node0 -> node1, node2, node3
#node1 -> node4
#node2 -> node4
#node4 -> node5
#node5 -> node6
#node7 -> node8
#node8 -> node9
#node9 -> node10
#node10 -> node11
#node11 -> node12, node13
#node12 -> node14
#node13 -> node14
#node14 -> node15

rcStateConnections = [(node0,node1), (node0,node2), (node0,node3), 
                      (node1,node4),(node2,node4),
                      (node4,node5), (node5,node6), (node6,node7), (node7,node8), (node8,node9), (node9,node10), (node10,node11), 
                      (node11,node12), (node11,node13),
                      (node12,node14), (node13,node14), 
                      (node14,node15)]

rcStateGraph = DirectedGraph(rcStateConnections)

#get shortest path from breadth first search on graph 
path = rcStateGraph.bfs(node14)

#print solution
for node in path: 
    node.value.describeState()

