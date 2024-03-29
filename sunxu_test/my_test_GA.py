import numpy
from sunxu_test import ga

"""
The y=target is to maximize this equation :
    y = f(x,y) = xsin(4πx) - ysin(4πy+π)+1
"""


num_genes = 2

"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 100
num_parents_mating = 10

# Defining the population size.
pop_size = (sol_per_pop,
            num_genes)  # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
# Creating the initial population.
new_population = numpy.random.uniform(low=-1.0, high=1.0, size=pop_size)
print(new_population)

best_outputs = []
num_generations = 100
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measuring the fitness of each chromosome in the population.
    # fitness = ga.cal_pop_fitness(equation_inputs, new_population)
    fitness = ga.cal_pop_fitness(new_population)
    print("Fitness")
    print(fitness)

    # best_outputs.append(numpy.max(numpy.sum(new_population * equation_inputs, axis=1)))
    # # The best result in the current iteration.
    # print("Best result : ", numpy.max(numpy.sum(new_population * equation_inputs, axis=1)))
    best_outputs.append(numpy.max(fitness))

    # Selecting the best parents in the population for mating.
    parents = ga.select_mating_pool(new_population, fitness,
                                    num_parents_mating)
    print("Parents")
    print(parents)

    # Generating next generation using crossover.
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(pop_size[0] - parents.shape[0], num_genes))
    print("Crossover")
    print(offspring_crossover)

    # Adding some variations to the offspring using mutation.
    offspring_mutation = ga.mutation(offspring_crossover, num_mutations=2)
    print("Mutation")
    print(offspring_mutation)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

# Getting the best solution after iterating finishing all generations.
# At first, the fitness is calculated for each solution in the final generation.
fitness = ga.cal_pop_fitness(new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])

import matplotlib.pyplot

matplotlib.pyplot.plot(best_outputs)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()
