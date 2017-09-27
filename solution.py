#The following class is used to describe the various states of the river crossing problem
class rcState():
    #Parameters:
    #Let mLeft = # Missionaries on left side of river (int)
    #Let mRight = # Missionaries on right side of river (int)
    #Let cLeft = # Cannibals on left side of river (int)
    #Let cRight = # Cannibals on right side of river (int)
    #Let boatPos = location of boat, either "Right" or "Left" (String)
    def __init__(self, mLeft, cLeft, mRight, cRight, boatPos):
        self.mLeft = mLeft
        self.cLeft = cLeft
        self.mRight = mRight
        self.cRight = cRight
        self.boatPos = boatPos
        
    def describeState(self):
        print("-----------------------------------------------------------------------------------------")
        print("Missionaries on left side of the river: %d" % (self.mLeft))
        print("Missionaries on right side of the river: %d" % (self.mRight))
        print("Cannibals on left side of the river: %d" % (self.cLeft))
        print("Cannibals on right side of the river: %d" % (self.cRight))
        print("The boat is currently on the " + self.boatPos + " side of the river.")

        
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
