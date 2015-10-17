Genetic Algoritm Library
========================

This is a very simple to use Genetic Algorithm Library with few simple usages
Library implements core part of algorithm viz. creation of chromosomes, selection,
crossover, mutation and formation of next generation. But the functionality of 
determination of weightages is given to user program. The Library tends to select 
high weight chromosomes. For sake of continuity, chromosome with max weight is 
inserted as is.

Functions
---------
`init` Initializes library and creates first generation population  
__Parameters__:  
`optimizer_function`: Function which will return weight for chromosome. Takes chromosome as argument  
`chromosome_length`: Chromosome length in bits  
`crossover_probability`: Probability of crossover  
`mutation_probability`: Probability of mutation  
`population_size`: total no. of chromosome in any generation  
`no_of_iterations`: no. of iteration per `iterate` call  

`iterateOnce` As the name suggests, just iterate once, creating next generation

`iterate` Iterates for iteration given in `init` function. Default 500

Examples
--------
Some simple implementations of library are provided

###expression-finder.py
Tries to find expression of single digits and arithmetic operators which comes closest
to given target. eg if target is 12, 3\*4, 5\*2+2 are exact matches while 5.2\*2+2
is a close match