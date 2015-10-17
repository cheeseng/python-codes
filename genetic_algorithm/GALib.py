from __future__ import division
import random, re, bisect

chromosomLength = 44
crossover = 0.7
mutate = 0.09
populationSize = 100
iterations = 4000

population = []
format_str = '{0:0'+str(chromosomLength)+'b}'
optimizerFunction = 0

def init(optimizer_function, chromosome_length, crossover_probability = 0.7, 
		mutation_probability = 0.05, population_size = 100, no_of_iterations = 500):

	global chromosomLength, crossover, mutate
	global populationSize, iterations, optimizerFunction
	global population

	optimizerFunction = optimizer_function
	chromosomLength = chromosome_length
	crossover = crossover_probability
	mutate = mutation_probability
	populationSize = population_size
	iterations = no_of_iterations


	for i in range(populationSize):
		s = ''
		# Create random chromosome
		for j in range(chromosomLength):
			j = random.randint(0, 1)
			s += str(j)
		population.append(s)

def iterateOnce():
	global population
	total = 0
	wt = []
	values = []
	for ch in population:
		w = optimizerFunction(ch)
		total += w
		wt.append(w)
		
	ind = wt.index(max(wt))
	ret = zip(population, wt)
	prev = 0
	for i in range(len(population)):
		wt[i] += prev
		prev = wt[i]

	temp = []
	temp.append(population[ind])
	
	#create next generation
	for i in range(len(population) - 1):

		#selection
		j = random.random() * total
		index1 = bisect.bisect_left(wt, j)

		j = random.random() * total
		index2 = bisect.bisect_left(wt, j)

		#crossover
		j = random.random()
		if j < crossover:	
			j=random.randint(0, chromosomLength)
			t_chrome = population[index1][:j] + population[index2][j:]
		else:
			t_chrome = population[index1]

		#mutate
		for k in range(chromosomLength):
			j = random.random()
			if j < mutate:
				try:
					t_chrome = t_chrome[:k] + str(1 - int(t_chrome[k])) + t_chrome[k+1:]
				except:
					print k, len(t_chrome)

		temp.append(t_chrome)

	population = temp
	return ret

def iterate():
	for loops in range(iterations): #total no of iterations
		chrome = iterateOnce()
	return chrome
