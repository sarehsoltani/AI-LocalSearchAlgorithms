import random
import math


class SimulatedAnnealing(object):

    def __init__(self, problem):
        self.problem = problem
        self.problem_solver(problem.initialState())

    def problem_solver(self, initial_state):
        number_of_expanded_nodes = 0
        number_of_visited_nodes = 0
        current_state = initial_state
        initial_temperature = 100
        current_temperature = initial_temperature
        while current_temperature > 1:
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            neighbors = self.problem.results(self.problem.actions(current_state),current_state)
            number_of_visited_nodes = number_of_visited_nodes + len(neighbors)
            chosen_neighbor = random.choice(neighbors)
            efficiency = self.problem.heuristic(chosen_neighbor) - self.problem.heuristic(current_state)
            if efficiency >= 0:
                current_state = chosen_neighbor
            else:
                if math.exp(efficiency/current_temperature) > random.random():
                    current_state = chosen_neighbor
            # 1
            #current_temperature = current_temperature - 1
            # 2
            #current_temperature = current_temperature * 0.99
            # 3
            current_temperature = math.sqrt(current_temperature)

        print("Last state: ")
        print('\t' + "Top  : " + str(current_state[1:10]))
        print('\t' + "Front: " + str(current_state[10:19]))
        print('\t' + "Down : " + str(current_state[19:28]))
        print('\t' + "Back : " + str(current_state[28:37]))
        print('\t' + "Left : " + str(current_state[37:46]))
        print('\t' + "Right: " + str(current_state[46:55]))
        print("Heuristic: " + str(self.problem.heuristic(current_state)))
        print("Number of visited nodes: " + str(number_of_visited_nodes))
        print("Number of expanded nodes: " + str(number_of_expanded_nodes))
