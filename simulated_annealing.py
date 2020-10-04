import random
import numpy as np
from math import exp

Max=1

def Fitness(list):
	one=list.count(1)
	fitness_value=abs((14*one)-190)
	return fitness_value


def randomflip(list):
	if list==0:
		return 1
	else:
		return 0	

Temp = 100

while(Max<=200):
	
	local=False
	values_list=[]
	
	

	for i in range(50):
		a=random.randint(0,1)
		values_list.append(a)


	values_list_fitness = Fitness(values_list)


	while(local!=True and Temp>50):
		t=0
		neighbour_list_best_fitness=0

		all_lists=[]

		while(t<=50):
			neighbour_list=values_list.copy()
			randpos = random.randint(0,39)
			neighbour_list[randpos]= randomflip(neighbour_list[randpos])
			all_lists.append(neighbour_list)
		  
		  for neighbour_list in all_lists:
		  	neighbour_list_fitness = Fitness(neighbour_list)
		  	exp_value= exp((neighbour_list_fitness - values_list_fitness)/Temp)
		  	if(neighbour_list_fitness > values_list_fitness):
		  		values_list_fitness=neighbour_list_fitness
		  		values_list=neighbour_list
		  	elif(np.random.uniform(0,1)<exp_value):
		  		values_list_fitness=neighbour_list_fitness
		  		values_list=neighbour_list
		  	else:
		  		local = True
		  			
	print(values_list_fitness, end=",")	  		 
	Temp = Temp*0.95			
	Max=Max+1





















































			#print(all_lists)


			# create a bigger list and then 

		# 	neighbour_list_fitness = Fitness(neighbour_list)

		# 	if(neighbour_list_fitness>neighbour_list_best_fitness):
		# 		neighbour_list_best_fitness=neighbour_list_fitness
		# 		best_list=neighbour_list.copy()
		# 	t= t+1
			
		# if(neighbour_list_best_fitness>values_list_fitness):
		# 	values_list =best_list.copy()
		# 	values_list_fitness=Fitness(values_list)
		# else:
		# 	local = True
		
		
	#print(values_list_fitness, end=",")			
	
	# Temp = Temp*0.95			
	# Max=Max+1
















		





