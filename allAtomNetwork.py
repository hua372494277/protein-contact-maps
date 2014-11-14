# calculate the clustering coefficient, characteristic path length, entropy, assortativity coefficient, Diameter and Radius
# of the network based on the coordinate of all atoms
import math
import networkx as nx

def distance(node1, node2):
    dist = 0.0
    distC = 0.0
    for atom1 in node1:
        for atom2 in node2:
            distC = pow( node1[atom1]['x'] - node2[atom2]['x'], 2 )
            distC += pow( node1[atom1]['y'] - node2[atom2]['y'], 2 )
            distC += pow( node1[atom1]['z'] - node2[atom2]['z'], 2 )
            distC = math.sqrt( distC )
            if dist == 0.0 or dist > distC:
                dist = distC               
    
    return dist

coordinateP = r'D:\NextIdea\allAtomCoordinate'

fr = open(r'D:\NextIdea\Dataset\scopClassHelixSheetpercentageNew.csv')
fw = open(r'D:\NextIdea\Dataset\allatomNetworkAddProperties.csv','w')


G = nx.Graph()
    
countL = 0    
while True:
    countL += 1
    print(countL)
    line = fr.readline()
    if not line:
        break
    
    line = line.rstrip()
    items = line.split(',')
    pdbname = items[0]

    #all atoms' coordinates
    frCoordinate = open( coordinateP + '\\' + pdbname + 'AllAtoms')

    coordinate = {}
    
    while True:
        lineCoordinate = frCoordinate.readline()
        if not lineCoordinate:
            break

        itemsC = lineCoordinate.split()
        numR = int(itemsC[1])
        coordinate.setdefault(numR,{})
        coordinate[numR].setdefault(int(itemsC[0]),{})
        coordinate[numR][int(itemsC[0])]['x'] = float(itemsC[-3])
        coordinate[numR][int(itemsC[0])]['y'] = float(itemsC[-2])
        coordinate[numR][int(itemsC[0])]['z'] = float(itemsC[-1])

    frCoordinate.close()

    for i in coordinate:
        for j in coordinate:
            if i < j:                           
                dis = distance(coordinate[i], coordinate[j])

                if dis <= 5.0 :
                    G.add_edge(i,j)#, weight = distance)

    if not nx.is_connected(G):
        scc = nx.connected_component_subgraphs(G)
        for sub in scc:
            input(sub.nodes())           
        
    
    degreeAssor = nx.degree_assortativity_coefficient(G)
    #print(degreeAssor)
    fw.write(str(degreeAssor) + ',')
    diameter = nx.diameter(G)
    #print(diameter)
    fw.write(str(diameter) + ',')
    radius = nx.radius(G)
    #input(radius)
    fw.write(str(radius) + '\n')
    
##    clusteringc = 0.0
##    averageLength = 0.0
##    entropy = 0
##    for ii in range(0, 10):
##        while True:
##            Gtest = nx.gnm_random_graph(G.number_of_nodes(), G.number_of_edges())
##            if nx.is_connected(Gtest):
##                break
##            
##        clusteringc += nx.average_clustering(Gtest)
##        averageLength += nx.average_shortest_path_length(Gtest)
##        
##        degreeSeq = nx.degree_histogram(Gtest)
##        
##        for degreeI in range(0,len(degreeSeq)):
##            percent = degreeSeq[degreeI]/nodeNum
##            if percent > 0:
##                entropy -=  percent * math.log( percent, 2)
##                
##        Gtest.clear()
##
##    
##    fw.write(str(entropy/10.0) + ',')        
##    fw.write(str(clusteringc/10.0) + ',')
##    fw.write(str(averageLength/10.0) + '\n')


    frCoordinate.close()
    G.clear()

fr.close()
fw.close()



        

        
