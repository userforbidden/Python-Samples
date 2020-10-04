import random
from operator import itemgetter
# import numpy as np
import matplotlib.pyplot as plt

## __ Random Orientation __ ##
## __ Input binary chromosome sequence __ ##
## __ Output chromosome with x,y co-oridinates in a list of tuples __ ##
def generate_chromosome(modified_sequence):
    chromosome=[(int(modified_sequence[0]), (0,0))]
    chromosome_cor={(0,0)}
    current_pos=(0,0)

    for gene in modified_sequence[1:]:
        options=[]
        valid_options=[]
        left=(current_pos[0]-1,current_pos[1])
        options.append(left)
        right=(current_pos[0]+1,current_pos[1])
        options.append(right)
        up=(current_pos[0],current_pos[1]+1)
        options.append(up)
        down=(current_pos[0],current_pos[1]-1)
        options.append(down)
    
        for cor in options:
            if cor not in chromosome_cor:
                valid_options.append(cor)
     
        next_pos=random.choice(valid_options)
        chromosome.append((int(gene), next_pos))
        chromosome_cor.add(next_pos)
        current_pos=next_pos

    return chromosome



## __ Chromosome Fitness Value Generator __ ##
## __ Input: each chromosome in the chromosome_list __ ##
## __ Output: chromosome fitness value __ ##
def calculate_fitness(chromosome):
    chromose_dict={}
    for pos_gene,gene in enumerate(chromosome):
        chromose_dict[gene[1]]=(pos_gene,gene[0])
    # print(chromose_dict)
    fitness=0
    for key_co,gene_val_pos in chromose_dict.items():
        left=(key_co[0]-1,key_co[1])
        fitness=fitness+fitness_per_gene(key_co,left,chromose_dict)
        right=(key_co[0]+1,key_co[1])
        fitness=fitness+fitness_per_gene(key_co,right,chromose_dict)
        up=(key_co[0],key_co[1]+1)
        fitness=fitness+fitness_per_gene(key_co,up,chromose_dict)
        down=(key_co[0],key_co[1]-1)
        fitness=fitness+fitness_per_gene(key_co,down,chromose_dict)
    return fitness
def fitness_per_gene(main_cor,surround_cor,chromose_dict):
    if surround_cor in chromose_dict:
        main_gene=chromose_dict[main_cor]
        surround_gene=chromose_dict[surround_cor]
        if main_gene[0]<surround_gene[0]:
            if abs(main_gene[0]-surround_gene[0])>1:
                if main_gene[1]==1 and surround_gene[1]==1:
                    return 1
    return 0


######## changing the sequence of hp into h as 1 and p as 0   ######

def mod_seq(sequence):

    modified_sequence=""
    for gene in sequence:
        if gene=="h":
            modified_sequence=modified_sequence+"0"
        else:
            modified_sequence=modified_sequence+"1"
    return modified_sequence


## __ Roulette_Wheel_Selection __ ##
## __ Input: Mid chromosomes __ ##
## __ Output: Roulette wheel selected chromosome __ ##
def roulette_selection(ready_for_Crossover):

    max=0
    for i in ready_for_Crossover:
        max=max+i[1]
    pick=random.uniform(0,max)
    current=0
    for i in ready_for_Crossover:
        current=current+i[1]
        if current>pick:
            return i[0]



## __ Crossover __ ##
## __ Input: two chromosomes __ ##
## __ Output: One crossed chromosome __##
def crossover(chromosomeX1,chromosomeX2):
    # print ("chromosomeX1 " +str(chromosomeX1))
    # print ("chromosomeX2 " +str(chromosomeX2))

    random_node=random.randint(1,len(chromosomeX1)-2)
    # print ("random_node "+str(random_node))
    selected_geneone=chromosomeX1[random_node]
    # print ("selected_geneone "+str(selected_geneone))
    selected_geneone_cor=selected_geneone[1]


    genes_constant1=chromosomeX1[:random_node+1]
    first_chrome1_cor={i[1] for i in chromosomeX1[:random_node+1]}    
    second_chrome2_cross=chromosomeX2[random_node+1:]
    # print ("second_chrome2_cross" +str(second_chrome2_cross)) 

    ########### Previous Direction Detection ##############
    PrevDir=0
    Ax=[0,0,0]
    Ay=[0,0,0]
    if chromosomeX1[random_node][1][0]==chromosomeX1[random_node-1][1][0]:
        y_dir_dis = chromosomeX1[random_node-1][1][1]-chromosomeX1[random_node][1][1]
        if y_dir_dis == 1:
            PrevDir = 3
        else:
            Prevdir = 4

        # print ("*** PrevDir *** " +str(PrevDir))
    else:
        x_dir_dis = chromosomeX1[random_node-1][1][0]-chromosomeX1[random_node][1][0]
        if x_dir_dis == 1:
            PrevDir = 1
        else:
            PrevDir = 2
        # print ("*** PrevDir *** " +str(PrevDir))

    if PrevDir==1:#right
        Ax=[-1,0,0]
        Ay=[0,1,-1]
    elif PrevDir==2:#left
        Ax=[1,0,0]
        Ay=[0,1,-1]
    elif PrevDir==3:#up
        Ax=[1,-1,0]
        Ay=[0,0,-1]
    elif PrevDir==4:#down
        Ax=[1,-1,0]
        Ay=[0,0,1]

# ########### First Crossover ##############
    first_xover_list = second_chrome2_cross
    xover_first_dx = chromosomeX1[random_node][1][0]+Ax[0]-chromosomeX2[random_node+1][1][0]
    xover_first_dy = chromosomeX1[random_node][1][1]+Ay[0]-chromosomeX2[random_node+1][1][1]

    first_xover_list[0]= (first_xover_list[0][0],(chromosomeX1[random_node][1][0]+Ax[0], chromosomeX1[random_node][1][1]+Ay[0]))

    for x in range(len(first_xover_list)-1):
        first_xover_list[x+1]= (chromosomeX2[random_node+x+2][0],(chromosomeX2[random_node+x+2][1][0]+xover_first_dx, chromosomeX2[random_node+x+2][1][1]+xover_first_dy))
    first_xover_cor={i[1] for i in first_xover_list}

    if (collision(first_chrome1_cor,first_xover_cor)):
        # print ("First Crossover" +str(genes_constant1+first_xover_list))
        return genes_constant1+first_xover_list


########### Second Crossover ##############
    second_xover_list = second_chrome2_cross
    xover_second_dx = chromosomeX1[random_node][1][0]+Ax[1]-chromosomeX2[random_node+1][1][0]
    xover_second_dy = chromosomeX1[random_node][1][1]+Ay[1]-chromosomeX2[random_node+1][1][1]

    second_xover_list[0]= (second_xover_list[0][0],(chromosomeX1[random_node][1][0]+Ax[1], chromosomeX1[random_node][1][1]+Ay[1]))

    for x in range(len(second_xover_list)-1):
        second_xover_list[x+1]= (chromosomeX2[random_node+x+2][0],(chromosomeX2[random_node+x+2][1][0]+xover_second_dx, chromosomeX2[random_node+x+2][1][1]+xover_second_dy))
    second_xover_cor={i[1] for i in second_xover_list}


    if (collision(first_chrome1_cor,second_xover_cor)):
        # print ("Second Crossover" +str(genes_constant1+second_xover_list))
        return genes_constant1+second_xover_list


########### Third Crossover ##############
    third_xover_list = second_chrome2_cross
    xover_third_dx = chromosomeX1[random_node][1][0]+Ax[2]-chromosomeX2[random_node+1][1][0]
    xover_third_dy = chromosomeX1[random_node][1][1]+Ay[2]-chromosomeX2[random_node+1][1][1]

    third_xover_list[0]= (third_xover_list[0][0],(chromosomeX1[random_node][1][0]+Ax[2], chromosomeX1[random_node][1][1]+Ay[2]))

    for x in range(len(second_chrome2_cross)-1):
        third_xover_list[x+1]= (chromosomeX2[random_node+x+2][0],(chromosomeX2[random_node+x+2][1][0]+xover_third_dx, chromosomeX2[random_node+x+2][1][1]+xover_third_dy))
    third_xover_cor={i[1] for i in third_xover_list}

    if (collision(first_chrome1_cor,third_xover_cor)):
        # print ("Third Crossover" +str(genes_constant1+third_xover_list))
        return genes_constant1+third_xover_list

    else:
        return None

####  checking for if there is any collision ################
def collision(first_chrome1_cor,new_cor):
    for cor in new_cor:
        if cor in first_chrome1_cor:
            return False
    return True

##########  mutation function ##########
def mutation(Mchromosome):

    # print ("chromose " +str(Mchromosome))
    random_pivot=random.randint(1,len(Mchromosome)-2)
    # print ("random_pivot "+str(random_pivot))
    selected_gene=Mchromosome[random_pivot]
    # print ("selected_gene "+str(selected_gene))
    selected_gene_cor=selected_gene[1]

    genes_constant=Mchromosome[:random_pivot+1]
    collision_cor={i[1] for i in Mchromosome[:random_pivot+1]}    
    genes_to_rotate=Mchromosome[random_pivot+1:]

    #a=selected_gene_cor[0]
    #b=selected_gene_cor[1]
    #x=cor[0]
    #y=cor[1]

    #90    
    nd=[(value,(selected_gene_cor[0]+selected_gene_cor[1]-cor[1],cor[0]+selected_gene_cor[1]-selected_gene_cor[0])) for value,cor in genes_to_rotate]
    nd_cor={i[1] for i in nd}
    if (no_collision(collision_cor,nd_cor)):
        return genes_constant+nd

    #180
    oed=[(value,(2*selected_gene_cor[0]-cor[0],2*selected_gene_cor[1]-cor[1])) for value,cor in genes_to_rotate]
    oed_cor={i[1] for i in oed}
    if (no_collision(collision_cor,oed_cor)):
        return genes_constant+oed

    #270
    tsd=[(value,(cor[1]+selected_gene_cor[0]-selected_gene_cor[1],selected_gene_cor[0]+selected_gene_cor[1]-cor[0])) for value,cor in genes_to_rotate]
    tsd_cor={i[1] for i in tsd}
    if (no_collision(collision_cor,tsd_cor)):
        return genes_constant+tsd

    #All rotations failed -------------------------------------need to have some lines   
    return None


#######  checking if there is collision ######################
def no_collision(collision_cor,new_cor):
  for cor in new_cor:
    if cor in collision_cor:
        return False
    return True


#######  Print function ###########################
def printlist(print_list):
    print ("***____List___*** \n")
    for i in print_list:
        print(str(i)+" Next Line \n")

####### Plot function to draw the best confirmation ############################
def plot_best_confirmation(last_list):
    plot_chrome_list=last_list

    x=[]
    y=[]

    x0=[]
    y0=[]

    x1=[]
    y1=[]

    for value in plot_chrome_list:
        if value[0]==0:
            x0.append(value[1][0])
            y0.append(value[1][1])
        else:
            x1.append(value[1][0])
            y1.append(value[1][1])
        x.append(value[1][0])
        y.append(value[1][1])


    # Create the figure and axes objects
    fig, ax = plt.subplots(1, figsize=(8, 6))
    # fig.suptitle('Sequence = hhhhhhhhhhhhphphpphhpphhpphpphhpphhpphpphhpphhpphphphhhhhhhhhhhh and highest fitness = -9',fontsize=18)

    # Plot the data
    ax.plot(x0,y0,'ro',x1,y1,'bo',x,y)

    # Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-')

    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.savefig('Figure_Plot.jpg')
    plt.show()
    plt.close(fig)
    # return None



############ Main FUnction of the Program #########################

def main_GA(sequence, max_fitness):
    #sequence = "hhhpphphphpphphphpph"
    #max_fitness = 42
    global_count=0
    global_generation=0
    global_difference=0
    modified_sequence=mod_seq(sequence)
    chromosome_list=[] #Initilize chromosome list
    top_fitness_list=[]

    #_________________________________________________________
    #
    # Generate 1st generation of randomly oriented chromosomes
    ###################################################
    while(len(chromosome_list)<200):
       try: 
        random_seq=generate_chromosome(modified_sequence)
        chromosome_list.append(random_seq)
       except:
           continue
    chromosome_fitness_list=[] #Initilize chromosome fitness list

    # print ("lenght of chrome list ",len(chromosome_list))
    #
    # Compute chromosome fitness
    ###################################################    
    for chrome in chromosome_list:
        chromosome_fitness_list.append((chrome,calculate_fitness(chrome)))



    # Sorting chromosome according to their fitness
    chromosome_fitness_list_sorted=sorted(chromosome_fitness_list,key=itemgetter(1),reverse=True)

    # Extracting First 5%  elements to elite_list
    elite_list=chromosome_fitness_list_sorted[:10]

    # print("Elite list "+str(elite_list))

    # Extracting the 90%  chromosomes to make crossover 
    ready_for_Crossover = chromosome_fitness_list_sorted[10:180]


    # Extracting the remaining 5% chromosomes to leftover 
    leftover_chromosome=chromosome_fitness_list_sorted[180:]


    # the ready to crossover chromosomes are crosseover using roulette wheel selection process and send to crossed_seq_list
    crossed_seq_list=[]
    while(len(crossed_seq_list)<180):
        try:
            selected_two_chromosomes=[]
            for i in range(2):
                result_select=roulette_selection(ready_for_Crossover)
                selected_two_chromosomes.append(result_select)
            
            crossed_chrome=crossover(selected_two_chromosomes[0],selected_two_chromosomes[1])
            if not (crossed_chrome==None):
                crossed_seq_list.append(crossed_chrome)
            # print("Function Output " +str(crossed_chrome))

        except:
            continue
    # print("crossed_seq_list")
    # printlist(crossed_seq_list)

    crossed_chromosome_fitness_list=[]
    # Compute chromosome fitness   
    for chrome_xover in crossed_seq_list:
        crossed_chromosome_fitness_list.append((chrome_xover,calculate_fitness(chrome_xover)))

    # Combining the crossover elements and leftover that is 90% which are in non-elite region
    Random_chromosome_fitness=crossed_chromosome_fitness_list+leftover_chromosome

    # selecting a random chromosome for doing mutation 
    sel_muted_index=random.randint(2,len(Random_chromosome_fitness)-1)

    ###### selected ramdom chromosome is removed from the non-elite region
    random_chromosome=Random_chromosome_fitness.pop(sel_muted_index)

    # Trying to mutation and checking if there is any empty chromosome selected for mutation
    muted_counter=0
    while muted_counter<100:
        muted_counter+=1
        muted_chromosome=mutation(random_chromosome[0])
        # print (muted_chromosome)
        if not(muted_chromosome==None):
            C_mutation=muted_chromosome
            break
    # if still mutation is none replace with random chromosome
    if C_mutation==None:
        C_mutation=random_chromosome

    # print(C_mutation)
    #####  muted chromosome is added to the non-elite region
    Random_chromosome_fitness.append((muted_chromosome,calculate_fitness(muted_chromosome)))

    #####  this combines both elite and non- elite region after mutation
    new_chromosome_fitness=elite_list+Random_chromosome_fitness


##### While loop from generation #2 to generation 90,000 ##### 
##### THE BIG LOOP #######

    while(global_generation<90000):

        global_generation=global_generation+1

        print ("Generation # "+str(global_generation))

        # Sorting chromosome according to their fitness
        chromosome_fitness_list_sorted=sorted(chromosome_fitness_list,key=itemgetter(1),reverse=True)
        # printing the first chromosome of the new generation    
        # print("new_chromosome_fitness")
        # printlist(chromosome_fitness_list_sorted[0])

        # print("Highest Fitness "+str(chromosome_fitness_list_sorted[0][1]))

        # plot_return=plot_best_confirmation(chromosome_fitness_list_sorted[0][0])




        # # ##### getting highest fitness value
        highest_fitness=chromosome_fitness_list_sorted[0][1]

        top_fitness_list.append(highest_fitness)
        print("highest fitness value  "+str(highest_fitness))



        # checking for exit conditons
        if global_generation>90000:
            break
        if highest_fitness== max_fitness:
            break
        if len(top_fitness_list)>20:
            last_top_five_fitness_list = top_fitness_list[-20:]
            if len(set(last_top_five_fitness_list))==1:
                break
        


        # Extracting First 5%  elements to elite_list
        elite_list=chromosome_fitness_list_sorted[:10]
        # print("Elite list "+str(elite_list))

        # Extracting the 90%  chromosomes to make crossover 
        ready_for_Crossover = chromosome_fitness_list_sorted[10:180]


        # Extracting the remaining 5% chromosomes to leftover 
        leftover_chromosome=chromosome_fitness_list_sorted[180:]


        # the ready to crossover chromosomes are crosseover using roulette wheel selection process and send to crossed_seq_list
        crossed_seq_list=[]
        while(len(crossed_seq_list)<180):
            try:
                selected_two_chromosomes=[]
                for i in range(2):
                    result_select=roulette_selection(ready_for_Crossover)
                    selected_two_chromosomes.append(result_select)
                
                crossed_chrome=crossover(selected_two_chromosomes[0],selected_two_chromosomes[1])
                if not (crossed_chrome==None):
                    crossed_seq_list.append(crossed_chrome)
                # print("Function Output " +str(crossed_chrome))

            except:
                continue
        # print("crossed_seq_list")
        # printlist(crossed_seq_list)

        crossed_chromosome_fitness_list=[]
        # Compute chromosome fitness  
        for chrome_xover in crossed_seq_list:
            crossed_chromosome_fitness_list.append((chrome_xover,calculate_fitness(chrome_xover)))

        # Combining the crossover elements and leftover that is 90% which are in non-elite region
        Random_chromosome_fitness=crossed_chromosome_fitness_list+leftover_chromosome

        # selecting a random chromosome for doing mutation 
        sel_muted_index=random.randint(2,len(Random_chromosome_fitness)-1)

        ###### selected ramdom chromosome is removed from the non-elite region
        random_chromosome=Random_chromosome_fitness.pop(sel_muted_index)

        # Trying to mutation and checking if there is any empty chromosome selected for mutation
        muted_counter=0
        while muted_counter<100:
            muted_counter+=1
            muted_chromosome=mutation(random_chromosome[0])
            # print (muted_chromosome)
            if not(muted_chromosome==None):
                C_mutation=muted_chromosome
                break
        # if still mutation is none replace with random chromosome
        if C_mutation==None:
            C_mutation=random_chromosome

        # print(C_mutation)
        #####  muted chromosome is added to the non-elite region
        Random_chromosome_fitness.append((muted_chromosome,calculate_fitness(muted_chromosome)))

        #####  this combines both elite and non- elite region after mutation
        new_chromosome_fitness=elite_list+Random_chromosome_fitness





if __name__ == "__main__":
    # execute only if run as a script
    with open("Python-Samples\\Input.txt") as f:
        content = f.readlines()

    contents = [x.strip() for x in content]

    for line in contents:
        if len(line)>0:
            if "Comment" in line:
                continue
            if "Seq" in line:
                seq=line.replace("Seq = ","")
            if "Fitness =" in line:
                max_fit=abs(int(line.replace("Fitness = ","")))

    main_GA(seq,max_fit)
