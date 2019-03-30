import random
from SearchAlgorithms.GeneticAlgorithm import *

class Problem():
    """description of class"""
    chrlength=49
    populationSize = 100
    maxcolor = 4
        
    def initialState(self):
        s = []
        graph = []
        lines = ""
        f = open("InputGraph.txt","r")
        lines = f.read()
        f.close()
        lines = lines.split("\n")
        print(lines)
        for line in lines:
            num = line.split(" ")
            l = [int(num[0]), int(num[1])]
            graph.append(l)
        print(len(graph))
        population = []
        k = random.randrange(0,self.maxcolor)
        for i in xrange(self.populationSize):
            population.append([])
            for k in xrange(self.chrlength):
                population[i].append(random.randrange(0,self.maxcolor)) 
        return graph,population
             
    def fitness(self, s, graph):
        sum = 0.0
        for i in range(len(graph)):
            if(state[graph[i][0]] != state[graph[i][1]]):
                sum = sum + 1
        return sum

    def crossover(self,a,b):
        cutPoint = random.randrange(0,self.chrlength)
        newChr = []        
        for i in range(0,cutPoint):
            newChr[i] = a[i]
        for i in range(cutPoint, self.chrlength):
            newChr[i] = b[i]
        return newChr

    def mutate(self,s):
        randomColor = random.randrange(0,self.maxcolor)
        random_index_to_mutation = random.randrange(0,self.chrlength)
        s[random_index_to_mutation] = randomColor
        return s
            

p = Problem()
gn = GeneticAlgorithm(p)
  

