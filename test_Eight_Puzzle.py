import unittest
import Eight_Puzzle
import random

class test_eight_puzzle(unittest.TestCase):
    def setUp(self):
        self.state={}

    def test_addfrontier(self):
        
        for i in range(10000):
            node={}
            node["stateno"]=i+1
            node["cost"]=10000-i
            Eight_Puzzle.addfrontier(node)
        #print(Eight_Puzzle.frontier)
        for i in range(5):
            self.assertLessEqual(Eight_Puzzle.frontier[i]["cost"],Eight_Puzzle.frontier[2*i+1]["cost"])
            if i==4:
                continue
            self.assertLessEqual(Eight_Puzzle.frontier[i]["cost"],Eight_Puzzle.frontier[2*i+2]["cost"])


    def test_getfrontier(self):
        
        for i in range(10000):
            #print(Eight_Puzzle.frontier)
            self.assertEqual(Eight_Puzzle.getfrontier()["cost"],i+1)
            self.assertEqual(len(Eight_Puzzle.frontier),10000-i-1)

##    def test_checkvisited(self):
##        for i in range(10):
##            state={}
##            a=list(range(1,64))
##            a.append(None)
##            random.shuffle(a)
##            state["pos"]=a
##            Eight_Puzzle.states[i+1]=state
##            node={}
##            node["stateno"]=i+1
##            node["cost"]=10-i
##            Eight_Puzzle.addfrontier(node)
##        for i in range(10):
##            node=Eight_Puzzle.getfrontier()
##            Eight_Puzzle.explored.append(node)
##            #Eight_Puzzle.addfrontier(node)
##            self.assertTrue(Eight_Puzzle.states[node["stateno"]])

        

if __name__=="__main__":
    unittest.main()
