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
