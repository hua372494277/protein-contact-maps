# calculate the clustering coefficient, characteristic path length, entropy, assortativity coefficient, Diameter 
# and Radius of the network based on the coordinate of C atoms
import math
import networkx as nx

fromP = r'E:\NextIdea\pdbChain'

fr = open(r'E:\NextIdea\Dataset\scopClassHelixSheetpercentageNew.csv')
fw = open(r'E:\NextIdea\Dataset\scopClassRealRandomEntropyCCandAL1901.csv','w')

G = nx.Graph()
while True:
    line = fr.readline()
    if not line:
        break
    
    line = line.rstrip()
    items = line.split(',')
    pdbname = items[0]

    #open DSSP file
    frpdb = open(fromP + '\\' + pdbname)
    #all c atoms' coordinates
    #element = {}
    
    while True:
        lineDssp = frpdb.readline()
        if not lineDssp:
            break

        lineDssp = lineDssp.rstrip()
        itemsD = []
        itemsD.append(lineDssp[0:5])
        lineDssp = lineDssp[5:]
        itemsD.append(lineDssp[0:5])
        lineDssp = lineDssp[5:]
        itemsD.append(lineDssp[0:2])
        lineDssp = lineDssp[2:]
        itemsD.append(lineDssp[0:2])
        lineDssp = lineDssp[2:]
        itemsD.append(lineDssp[0:4])
        lineDssp = lineDssp[4:]
        itemsD.append(lineDssp[0:5])
        lineDssp = lineDssp[5:]
        for t in lineDssp.split():
            itemsD.append(t)

        numR = int(itemsD[0])
        G.add_node(numR, x = float(itemsD[-3]), y = float(itemsD[-2]), z= float(itemsD[-1]))
##        input(G.nodes())
##        input(G.node[1])

##        element.setdefault(numR,{})
##        l = itemsD[3].rstrip()
##        l = l.lstrip()
##        element[numR]['second'] = l
            
    nodesList = G.nodes()

    for i in range(0, len(nodesList)):
        for j in range(i+1, len(nodesList)):
            beginN = nodesList[i]
            endN = nodesList[j]
            #if abs(int(beginN) - int(endN)) < 7 or ( abs(int(beginN) - int(endN)) > 29 and abs(int(beginN) - int(endN)) < 41):             
            beginNX = G.node[beginN]['x']
            beginNY = G.node[beginN]['y']
            beginNZ = G.node[beginN]['z']
            
            endNX = G.node[endN]['x']
            endNY = G.node[endN]['y']
            endNZ = G.node[endN]['z']
        
            distance = math.sqrt(math.pow((beginNX - endNX), 2) + math.pow((beginNY - endNY), 2) + math.pow((beginNZ - endNZ), 2))

            if distance <= 7.0 :
                G.add_edge(beginN, endN)#, weight = distance)

    degreeSeq = nx.degree_histogram(G)
    nodeNum = G.number_of_nodes()
    entropy = 0
    for degreeI in range(0,len(degreeSeq)):
        percent = degreeSeq[degreeI]/nodeNum
        if percent > 0:
            entropy -=  percent * math.log( percent, 2)

    fw.write(str(entropy) + ',')
    fw.write(str(nx.average_clustering(G) )+ ',')
    fw.write(str(nx.average_shortest_path_length(G) )+ ',')
    
    clusteringc = 0.0
    averageLength = 0.0

    entropy = 0
    for ii in range(0, 10):
        while True:
            Gtest = nx.gnm_random_graph(G.number_of_nodes(), G.number_of_edges())
            if nx.is_connected(Gtest):
                break
            
        clusteringc += nx.average_clustering(Gtest)
        averageLength += nx.average_shortest_path_length(Gtest)
        
        degreeSeq = nx.degree_histogram(Gtest)
        
        for degreeI in range(0,len(degreeSeq)):
            percent = degreeSeq[degreeI]/nodeNum
            if percent > 0:
                entropy -=  percent * math.log( percent, 2)
                
        Gtest.clear()

    
    fw.write(str(entropy/10.0) + ',')        
    fw.write(str(clusteringc/10.0) + ',')
    fw.write(str(averageLength/10.0) + '\n')

    frpdb.close()
    G.clear()

fr.close()
fw.close()
