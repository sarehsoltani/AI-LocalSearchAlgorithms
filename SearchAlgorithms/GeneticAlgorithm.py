import random
import math
import sys

class GeneticAlgorithm(object):
    def __init__(self, problem):
        self.problem = problem
    NumGeneration = 50
    populationSize = 100
    population = []
    graph = []
    maxcolor = 4
    newg = []
    tornoment= 10
    chrlength = 49
    mutationRate = 0.02
    mutatedGenomes = (int) (chrlength * mutationRate * populationSize)
    population = []
    selection = []
    selected = []
    bestFitness = []
    worstFitness= []
    avgFitness = []
    
    def initialState(self):
        s = []
        lines = ""
        f = open("InputGraph.txt","r")
        lines = f.read()
        f.close()
        lines = lines.split("\n")
        print(lines)
        for line in lines:
            num = line.split(" ")
            l = [int(num[0]), int(num[1])]
            self.graph.append(l)
        print(len(self.graph))
        
        k = random.randrange(0,self.maxcolor)
        for i in xrange(self.populationSize):
            self.population.append([])
            for k in xrange(self.chrlength):
                self.population[i].append(random.randrange(0,self.maxcolor))          
        return self.graph,self.population

    def fitness(self, s):
        sum = 0.0
        for i in range(len(self.graph)):
           if(self.graph[i][0] == s or self.graph[i][1] == s):
               if(self.graph[i][0] != self.graph[i][1]):
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

    def selectBestParents(self,a):
        fit = []
        cuple = []
        for i in range(len(a)):
            fit[i] = self.fitness(a[i])
        # Sort the given array arr in reverse  
        fit.sort(reverse = True)
        for i in range(2):
            cuple.append(fit[i])
        #select best parents
        self.selected[0] = cuple[0]
        self.selected[1] = cuple[1]
    
    def calculateFitness(self,a,numg):
        fit = []
        sum = 0
        min = 10000
        max = 0
        for i in range(len(a)):
            fit[i] = fitness(a[i])
        for j in range(len(fit)):
            sum = sum + fit[j]
            if(min > fit[j]):
               min = fit[j]
            if(max < fit[j]):
                max = fit[j] 
        average = float(sum) / len(fit)
        self.bestFitness[numg] = max
        self.worstFitness[numg]=min;
        self.avgFitness[numg]=average;

    def run(self):
        numGen = 0
        print("sare",self.selection)
        while(numGen < self.NumGeneration):
            for j in range(self.populationSize):
                for i in range(self.tornoment):
                    cs = random.randrange(0,self.populationSize)
                    print("cs index",cs,i,self.population[cs])
                    self.selection[i] = self.population[cs]     # choice parents
                self.selectBestParents(self.selection) # choising best parents
                self.newg = crossover(self.selected[0],self.selected[1]) #produce new child
                
            for i in range(self.mutatedGenomes):
                cs = random.randrange(0,self.populationSize)
                self.newg[cs] = mutate(self.newg[cs])  #mutate
            
            calculateFitness(self.population,numGen)
            for i in range(self.populationSize):
                for j in range(self.chrlength):
                    self.population[i][j] = self.newg[i][j]
            numGen = numGen + 1

    def report():
        for i in range(self.NumGeneration):
            print("Reporting the generation" + (i+1) + " :\n")
            print("Best Fitness : " + self.bestFitness[i])
            print("Worst Fitness : " + self.worstFitness[i])
            print("Average Fitness : " + self.avgFitness[i])   

