from SearchAlgorithms.ClassicSearchAlgorithms import *
from SearchAlgorithms.SimulatedAnnealing import *
from copy import deepcopy
class Problem():
    def initialState(self):
        rubik =  ('','y', 'y', 'b', 'y', 'y', 'b', 'y', 'y', 'b',
                     'g', 'g', 'y', 'g', 'g', 'y', 'g', 'g', 'y',
                     'w', 'w' ,'g', 'w', 'w', 'g', 'w', 'w', 'g',
                     'b', 'b', 'w', 'b', 'b', 'w', 'b', 'b', 'w',
                     'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
                     'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o') 
        print("initial state")
        print('\t' + "Top  : " + str(rubik[1:10]))
        print('\t' + "Front: " + str(rubik[10:19]))
        print('\t' + "Down : " + str(rubik[19:28]))
        print('\t' + "Back : " + str(rubik[28:37]))
        print('\t' + "Left : " + str(rubik[37:46]))
        print('\t' + "Right: " + str(rubik[46:55]))
        return rubik
        
    def isGoalTest(self,state):
        FaceColor = ''
        for i in range(0, 55):
            if i % 9 == 1:
                FaceColor = state[i]
            elif FaceColor != state[i]:
                return False
        return True

    def heuristic(self,state):
        score1,score2,score3,score4,score5,score6 = 0,0,0,0,0,0
        for i in range(1,10):
            if(state[i] == 'y'):
                score1 = score1 + 1
        for i in range(10,19):
 
            if(state[i] == 'g'):
                score2 = score2 + 1
        for i in range(19,28):
            if(state[i] == 'w'):
                score3 = score3 + 1
        for i in range(28,37):
            if(state[i] == 'b'):
                score4 = score4 + 1
        for i in range(37,46):
            if(state[i] == 'r'):
                score5 = score5 + 1
        for i in range(46,55):
            if(state[i] == 'o'):
                score6 = score6 + 1
        score = score1 + score2 + score3 + score4 + score5 + score6
        return score
                
    def actions(self,state):
        actions= ['T','tC', 'F', 'fC', 'R', 'rC', 'L', 'lC', 'B', 'bC', 'D','dC']
        return actions       

    def results(self,actions,state):
        states = []
        for action in actions:
          state = list(state)
          next_state = deepcopy(state)
          if 'F' in action:
            next_state[10], next_state[11], next_state[12], next_state[15] = state[16], state[13], state[10], state[11]
            next_state[18], next_state[17], next_state[16], next_state[13] = state[12], state[15], state[18], state[17]
            ########
            next_state[7], next_state[8], next_state[9] = state[45],  state[42],  state[39]
            next_state[46], next_state[49],  next_state[52]  = state[7], state[8], state[9]
            next_state[21], next_state[20], next_state[19] = state[46], state[49], state[52]
            next_state[39], next_state[42], next_state[45] = state[19], state[20], state[21]
        
          elif 'fC' in action:
            next_state[10], next_state[11], next_state[12], next_state[15] = state[12], state[15], state[18], state[17]
            next_state[18], next_state[17], next_state[16], next_state[13] = state[16], state[13], state[10], state[11]
            ###
            next_state[7], next_state[8], next_state[9] = state[46],  state[49],  state[52]
            next_state[46], next_state[49], next_state[52] = state[21], state[20], state[19]
            next_state[21], next_state[20], next_state[19] = state[45], state[42], state[39]
            next_state[39],  next_state[42],  next_state[45]  = state[9], state[8], state[7]
              
          elif 'R' in action:
            next_state[46], next_state[47], next_state[48], next_state[49] = state[52], state[49], state[46], state[53]
            next_state[51], next_state[52], next_state[53], next_state[54] = state[47], state[54], state[51], state[48]
            ###
            next_state[12], next_state[15], next_state[18] = state[21], state[24], state[27]
            next_state[3], next_state[6], next_state[9] = state[12], state[15], state[18]
            next_state[30], next_state[33], next_state[36] = state[3], state[6], state[9]
            next_state[21], next_state[24], next_state[27] = state[30], state[33], state[36]          
        
          elif 'rC' in action:
            next_state[46], next_state[47], next_state[48], next_state[49] = state[48], state[51], state[54], state[47]
            next_state[51], next_state[52], next_state[53], next_state[54] = state[53], state[46], state[49], state[52]
            ###
            next_state[12], next_state[15], next_state[18] = state[3], state[6], state[9]
            next_state[3],  next_state[6],  next_state[9]  = state[30], state[33], state[36]
            next_state[21], next_state[24], next_state[27] = state[12], state[15], state[18]
            next_state[30], next_state[33], next_state[36] = state[21], state[24], state[27]          
        
          elif 'L' in action:
            next_state[37], next_state[38], next_state[39], next_state[40] = state[43], state[40], state[37], state[44]
            next_state[42], next_state[43], next_state[44], next_state[45] = state[38], state[45], state[42], state[39]
            ###
            next_state[1],  next_state[4], next_state[7]  = state[28], state[31], state[34]
            next_state[10], next_state[13], next_state[16] = state[1], state[4], state[7]
            next_state[19], next_state[22], next_state[25] = state[10], state[13], state[16]
            next_state[28], next_state[31], next_state[34] = state[19], state[22], state[25]
        
          elif 'lC' in action:
            next_state[37], next_state[38], next_state[39], next_state[40] = state[39], state[42], state[45], state[38]
            next_state[42], next_state[43], next_state[44], next_state[45] = state[44], state[37], state[40], state[43]
            ###
            next_state[1],  next_state[4],  next_state[7]  = state[10], state[13], state[16]
            next_state[10], next_state[13], next_state[16] = state[19], state[22], state[25]
            next_state[19], next_state[22], next_state[25] = state[28], state[31], state[34]
            next_state[28], next_state[31], next_state[34] = state[1],  state[4],  state[7]
        
          elif 'B' in action:
            next_state[28], next_state[29], next_state[30], next_state[31] = state[34], state[31], state[28], state[35]
            next_state[33], next_state[34], next_state[35], next_state[36] = state[29], state[36], state[33], state[30]
            ###
            next_state[1],  next_state[2],  next_state[3]  = state[48], state[51], state[54]
            next_state[37], next_state[40], next_state[43] = state[3],  state[2],  state[1]
            next_state[48], next_state[51], next_state[54] = state[27], state[26], state[25]
            next_state[25], next_state[26], next_state[27] = state[37], state[40], state[43]
        
          elif 'bC' in action:
            next_state[28], next_state[29], next_state[30], next_state[31] = state[30], state[33], state[36], state[29]
            next_state[33], next_state[34], next_state[35], next_state[36] = state[35], state[28], state[31], state[34]
            ###
            next_state[1],  next_state[2],  next_state[3]  = state[43], state[40], state[37]
            next_state[37], next_state[40], next_state[43] = state[25], state[26], state[27]
            next_state[48], next_state[51], next_state[54] = state[1],  state[2],  state[3]
            next_state[25], next_state[26], next_state[27] = state[54], state[51], state[48]
        
          elif "D" in action:
            next_state[19], next_state[20], next_state[21], next_state[22] = state[25], state[22], state[19], state[26]
            next_state[24], next_state[25], next_state[26], next_state[27] = state[20], state[27], state[24], state[21]
            ###
            next_state[43], next_state[44], next_state[45]  = state[30], state[29], state[28]
            next_state[16], next_state[17], next_state[18]  = state[43],  state[44],  state[45]
            next_state[52], next_state[53], next_state[54] = state[16], state[17], state[18]
            next_state[28], next_state[29], next_state[30] = state[54], state[53], state[52]

          elif "dC" in action:
            next_state[19], next_state[20], next_state[21], next_state[22] = state[21], state[24], state[27], state[20]
            next_state[24], next_state[25], next_state[26], next_state[27] = state[26], state[19], state[22], state[25]
            ###
            next_state[43], next_state[44], next_state[45]  = state[16], state[17], state[18]
            next_state[16], next_state[17], next_state[18]  = state[52],  state[53],  state[54]
            next_state[52], next_state[53], next_state[54] = state[30], state[29], state[28]
            next_state[28], next_state[29], next_state[30] = state[45], state[44], state[43]
        
          elif 'T' in action:
            next_state[1], next_state[2], next_state[3], next_state[4] = state[7], state[4], state[1], state[8]
            next_state[6], next_state[7], next_state[8], next_state[9] = state[2], state[9], state[6], state[3]
            ###
            next_state[37], next_state[38], next_state[39]  = state[10], state[11], state[12]
            next_state[10], next_state[11], next_state[12]  = state[46],  state[47],  state[48]
            next_state[46], next_state[47], next_state[48] = state[36], state[35], state[34]
            next_state[34], next_state[35], next_state[36] = state[39], state[38], state[37]
                
          elif 'tC' in action:
            next_state[1], next_state[2], next_state[3], next_state[4] = state[3], state[6], state[9], state[2]
            next_state[6], next_state[7], next_state[8], next_state[9] = state[8], state[1], state[4], state[7]
            ###
            next_state[37], next_state[38], next_state[39]  = state[36], state[35], state[34]
            next_state[10], next_state[11], next_state[12]  = state[37],  state[38],  state[39]
            next_state[46], next_state[47], next_state[48] = state[10], state[11], state[12]
            next_state[34], next_state[35], next_state[36] = state[48], state[47], state[46]
        
          next_state = tuple(next_state)
          states.append(next_state)
          ''' 
          print('\t' + "Top: "+ str(next_state[1:10]))
          print('\t' + "Front: " + str(next_state[10:19]))
          print('\t' + "Down: " + str(next_state[19:28]))
          print('\t' + "Back: " + str(next_state[28:37]))
          print('\t' + "Left: "+ str(next_state[37:46]))
          print('\t' + "Right" + str(next_state[46:55]))
          '''
        return states 


p = Problem()
SearchAlgorithms = ClassicSearchAlgorithm(p) 
#SearchAlgorithms.TBFS(p.initialState())          
SimulatedAnnealing(p)