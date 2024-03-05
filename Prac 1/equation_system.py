import numpy as np
import pygad

A = np.matrix([[16, -6, 4, 1],
				[1, -8, 1, 1],
				[16, 2, -4, 1], 
				[9, 8, -3, 1]])
#x = np.matrix([[0, 0, 0, 0]])
b = np.matrix([[-36, 64, -4, -64]])



"""
	Ax = b
"""
def fitness_function(ga_instance, x, solution_idx):
	result = np.sqrt(np.power(A.dot(x) - b, 2))
	return 1/(result.sum())

if __name__ == '__main__':
	
	num_generations = 300
	num_parents_mating = 2

	sol_per_pop = 8
	num_genes = 4

	init_range_low = -20
	init_range_high = 20

	parent_selection_type = "rws"
	keep_parents = 2

	crossover_type = "single_point"

	mutation_type = "random"
	mutation_percent_genes = 76

	ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
					   gene_type=float,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)
	
	ga_instance.run()

	solution, solution_fitness, solution_idx = ga_instance.best_solution()
	print("Genetic Algorithm")
	print("Solution x : {solution}".format(solution=solution))
	print("Fitness value  = {solution_fitness}".format(solution_fitness=solution_fitness))

	prediction = A.dot(solution)
	print("Ax = : {prediction}".format(prediction=prediction))
	print("Error", np.power((A.dot(solution) - b), 2).sum()) 
	
	print("Random Number solution")
	sol = np.random.randint(-100, 100, size=(4, 1))
	print("x = ", sol)
	print("Ax = ", A.dot(sol))
