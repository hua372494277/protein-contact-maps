# RandSS and RandSN algorithms
import math
import random
import networkx as nx

fromP = r'D:\NextIdea\pdbChain'

fr = open(r'D:\NextIdea\Dataset\scopClassHelixSheetpercentageNew.csv')
fw = open(r'D:\NextIdea\Dataset\propertyOfbackboneSecondaryStructure.csv', 'w')
fw.write('entropy,clustering coefficient, average path length, degree assortativity coefficient, diameter, radius,')
fw.write('entropy,clustering coefficient, average path length, degree assortativity coefficient, diameter, radius\n')
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

    #open DSSP file
    frpdb = open(fromP + '\\' + pdbname)
    #all c atoms' coordinates
       
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
        G.add_node(numR, x = float(itemsD[-3]), y = float(itemsD[-2]), z= float(itemsD[-1]),label = itemsD[3][1])
        
            
    nodesList = G.nodes()
    edgeNum = 0
    
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
                if G.node[beginN]['label'] in {'H', 'G', 'I', 'E', 'B'} and G.node[endN]['label'] in {'H', 'G', 'I', 'E', 'B'}:
                    G.add_edge(beginN, endN)
                else:
                    if abs(beginN - endN) < 3:
                        G.add_edge(beginN, endN)
                    else:
                        edgeNum += 1
    
    nodeNum = G.number_of_nodes()
    #rest = edgeNum
    clusteringc = 0.0
    averageLength = 0.0
    entropy = 0
    degreeATen = 0.0
    diameterTen = 0.0
    radiusTen = 0.0
    for repeat in range(0, 10):
        rest = edgeNum
        H = G.copy()
        while rest > 0:
            nodei = random.choice(nodesList)
            while True:                
                nodeii = random.choice( nodesList )
                if abs(nodei - nodeii) > 0 and random.random() >=  abs(nodei - nodeii) / (nodeNum - 1):
                    break

            nodeI = []
            nodeI.append(nodei)
            nodeII = []
            nodeII.append(nodeii)
                
            if nodei - 1 in nodesList:
                nodeI.append(nodei - 1)

            if nodei + 1 in nodesList:
                nodeI.append(nodei + 1)        
            
            if nodeii - 1 in nodesList:
                nodeII.append( nodeii - 1)
        
            if nodeii + 1 in nodesList:
                nodeII.append( nodeii + 1)

            for beginN in nodeI:
                for endN in nodeII:
                    if beginN != endN and not H.has_edge(beginN, endN):
                        H.add_edge(beginN, endN)
                        rest -= 1
                        if rest == 0:
                            break
                if rest == 0:
                    break

        #then, calculate the entropy, cc, and average path length
        clusteringc += nx.average_clustering(H)
        averageLength += nx.average_shortest_path_length(H)
        degreeSeq = nx.degree_histogram(H)
        
        for degreeI in range(0,len(degreeSeq)):
            percent = degreeSeq[degreeI]/nodeNum
            if percent > 0:
                entropy -=  percent * math.log( percent, 2)
        degreeATen += nx.degree_assortativity_coefficient(H)
        diameterTen += nx.diameter(H)        
        radiusTen += nx.radius(H)
        #nx.write_edgelist(H, "D:\\NextIdea\\contactmap\\"+pdbname+ str(repeat) + "my1", data=False)
        H.clear()

    #input(str(entropy/10.0) + '--' + str(clusteringc/10.0) + '--' + str(averageLength/10.0) + '--' +str(degreeATen/10.0) + '--' +str(diameterTen/10.0) + '--' + str(radiusTen/10.0))
        
    fw.write(str(entropy/10.0) + ',')        
    fw.write(str(clusteringc/10.0) + ',')
    fw.write(str(averageLength/10.0) + ',')
    fw.write(str(degreeATen/10.0) + ',')        
    fw.write(str(diameterTen/10.0) + ',')
    fw.write(str(radiusTen/10.0) + ',')

    clusteringc = 0.0
    averageLength = 0.0
    entropy = 0.0
    degreeATen = 0.0
    diameterTen = 0.0
    radiusTen = 0.0
    Gtest = nx.Graph()
    for i in range(0, 10):
        # add backbone edges i -- i+1, i -- i+2  
        for nodei in nodesList:
            nodeii = nodei + 1
            if nodeii in nodesList:
                Gtest.add_edge(nodei, nodeii)

            nodeiii = nodei + 2
            if nodeiii in nodesList:
                Gtest.add_edge(nodei, nodeiii)

        rest = G.number_of_edges() + edgeNum - Gtest.number_of_edges()
        
        #add the rest edges randomly
        while rest > 0:
            nodei = random.choice(nodesList)
            
            while True:
                nodeii = random.choice( nodesList )
                if abs(nodei - nodeii) > 0 and random.random() >=  abs(nodei - nodeii) / (nodeNum - 1):
                    break
            
            nodeI = []
            nodeI.append(nodei)
            nodeII = []
            nodeII.append(nodeii)
                
            if nodei - 1 in nodesList:
                nodeI.append(nodei - 1)

            if nodei + 1 in nodesList:
                nodeI.append(nodei + 1)        
            
            if nodeii - 1 in nodesList:
                nodeII.append( nodeii - 1)
        
            if nodeii + 1 in nodesList:
                nodeII.append( nodeii + 1)                

            for beginN in nodeI:
                for endN in nodeII:
                    if beginN != endN and not Gtest.has_edge(beginN, endN):
                        Gtest.add_edge(beginN, endN)
                        rest -= 1
                        if rest == 0:
                            break
                if rest == 0:
                    break

        #finish the construction of randomNN
        #then, calculate the entropy, cc, and average path length
        clusteringc += nx.average_clustering(Gtest)
        averageLength += nx.average_shortest_path_length(Gtest)
        degreeSeq = nx.degree_histogram(Gtest)
        
        for degreeI in range(0,len(degreeSeq)):
            percent = degreeSeq[degreeI]/nodeNum
            if percent > 0:
                entropy -=  percent * math.log( percent, 2)
        degreeATen += nx.degree_assortativity_coefficient(Gtest)
        diameterTen += nx.diameter(Gtest)        
        radiusTen += nx.radius(Gtest)
        #nx.write_edgelist(H, "D:\\NextIdea\\contactmap\\"+pdbname+ str(repeat) + "my1", data=False)
        Gtest.clear()

    #input(str(entropy/10.0) + '--' + str(clusteringc/10.0) + '--' + str(averageLength/10.0) + '--' +str(degreeATen/10.0) + '--' +str(diameterTen/10.0) + '--' + str(radiusTen/10.0))
        
    fw.write(str(entropy/10.0) + ',')        
    fw.write(str(clusteringc/10.0) + ',')
    fw.write(str(averageLength/10.0) + ',')
    fw.write(str(degreeATen/10.0) + ',')        
    fw.write(str(diameterTen/10.0) + ',')
    fw.write(str(radiusTen/10.0) + '\n')
        
    G.clear()      
    #input(pdbname)
fr.close()
fw.close()



        

        

            

