import random

class Level:
    
   def __init__(self,inputCount,outputCount):
      self.inputs = list((inputCount)) 
      self.outputs = list((outputCount))
      self.biases = list((outputCount))
      
      self.weights = []
      for i in inputCount:
          self.weights[i] = list((outputCount))
          
      Level.randomize(self)
      

def randomize(level):
    for i in len(level.input):
        for j in len(level.output):
            level.weights[i][j] = random * 2 -1
    
        
   
    

