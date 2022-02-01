'''
A combinational lock has three rings. YOu input the ring characters when initializing the program.

Write api's to find if the target word can be formed in the combination lock 
Write API to check if the combination can be formed 
Write api to rotate the rings to reach the combination and find out how many turns are made 
'''

class combinationalLock():
    def __init__(self,ring1,ring2,ring3) -> None:
        self.ring1 = [char for char in ring1]
        self.ring2 = [char for char in ring2]
        self.ring3 = [char for char in ring3]

    def getCurrentCombination(self):
        if not (len(self.ring1) == len(self.ring2) == len(self.ring3)):
            return "Ring character lengths are not equal"
        elif self.ring1 and self.ring2 and self.ring3:
            return self.ring1[0]+self.ring2[0]+self.ring3[0] 
        else:
            return "Empty rings provided"
    def isValidCombination(self,word):
        if (len(word) == 3) and (word[0] in self.ring1) and (word[1] in self.ring2) and (word[2] in self.ring3):
            return True
        return False
def driver():
    cl = combinationalLock('CMME','ABOF','TMPM')
    # cl = combinationalLock('','','')
    print(cl.getCurrentCombination())
    print(cl.isValidCombination('MOASSS'))
if __name__ == '__main__':
    driver()