import numpy as np 


class Pagerank():

    def __init__(self):
        print("Program to calculate Pagerank")
        self.graph_dict = {}
        self.nodes = []
        self.inputMatrix = None
    
    def formSourceDestDict(self,lines):
        for links in lines:
            source,dest = [int(x) for x in links.split(",")]
            if source not in self.nodes:
                self.nodes.append(source)
            if dest not in self.nodes:
                self.nodes.append(dest)
            if source in self.graph_dict:
                self.graph_dict[source].append(dest)
            else:
                dest_list = []
                dest_list.append(dest)
                self.graph_dict[source]= dest_list
    def formGraphMatrix(self,vertices):
        # print(vertices)
        elementList = []
        for v in range(vertices):
            if v not in self.graph_dict:
                elementList.append([0]*vertices)
            else:
                points_List = []
                for j in range(vertices):
                    if j not in self.graph_dict[v]:
                        points_List.append(0.0)
                    else:
                        points_List.append(1.0/len(self.graph_dict[v]))
                elementList.append(points_List)
        self.inputMatrix = np.transpose(np.array(elementList))
    def calculatePagerankScore(self,vertices):
        initialPagerankScore = np.full((vertices,1),1.0/vertices)
        iteratedMatrix = np.dot(self.inputMatrix,initialPagerankScore)
        for i in range(100):
            tempMatrix = iteratedMatrix
            iteratedMatrix = np.dot(self.inputMatrix, iteratedMatrix)
            # calculate convergence value
            newValue = np.linalg.norm((iteratedMatrix-tempMatrix), ord=1)
            oldValue= np.linalg.norm(tempMatrix, ord=1)
            threshold = newValue/oldValue
            if threshold < 0.05:
                break
        return iteratedMatrix, i




def main():
    pr = Pagerank()

    with open("inputwith3vertex.txt") as inputfile:
        graph = inputfile.readlines()
    lines = [x.strip() for x in graph]
    pr.formSourceDestDict(lines)
    pr.formGraphMatrix(len(pr.nodes))
    finalPGScore, ConvergencePoint = pr.calculatePagerankScore(len(pr.nodes))

    outputfile = open("outputwith3vertex.txt","w")

    for vertex, PGValue in enumerate(finalPGScore):
        outputfile.write(str(vertex)+ " " +str(PGValue)+"\n")
    outputfile.write("Iteration where convergence achieved is %d"%(ConvergencePoint))
    outputfile.close()





if __name__ == '__main__':
    main()