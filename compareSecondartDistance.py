# calculating the Euclidean distance between residues with different sequence distance
import math
def distance(point1x, point1y, point1z, point2x, point2y, point2z):    
    return math.sqrt( math.pow(point1x - point2x, 2) +  math.pow(point1y - point2y, 2) + math.pow(point1z - point2z, 2))

fromP = r'E:\NextIdea\pdbChain'

fr = open(r'E:\NextIdea\Dataset\scopClassHelixSheetpercentageNew.csv')

##fw = open(r'E:\NextIdea\Dataset\EdgeRest.csv', 'w')

Distance = { 'H':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'G':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'I':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'N':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'S':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'T':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
             }
DistanceSame = { 'H':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'G':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'I':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'N':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'S':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},
             'T':{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
             }
normal = ['N', 'S', 'H', 'G', 'I', 'T']
Edistance = {}
EdistanceSame = {}
EdistanceSeq = {}
EdistanceSameSeq = {}

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
    coordinate = {}

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
        
        coordinate.setdefault( numR, {})
        coordinate[numR]['x'] = float(itemsD[-3])
        coordinate[numR]['y'] = float(itemsD[-2])
        coordinate[numR]['z'] = float(itemsD[-1])

        l = itemsD[3].rstrip()
        l = l.lstrip()

        coordinate[numR]['second'] = l
        if l == 'E' or l == 'B': 
            coordinate[numR].setdefault('Neighbors',[])
            if int(itemsD[4]) > 0:
                coordinate[numR]['Neighbors'].append(int(itemsD[4]))
            if int(itemsD[5][0:-1]) > 0:
                coordinate[numR]['Neighbors'].append(int(itemsD[5][0:-1]))
            #input(str(numR) +'---' + str(coordinate[numR]['Neighbors']))
      

    
    
    for itemN in coordinate:
##        if coordinate[itemN]['second'] in normal:
##            for itemNN in range(itemN + 1, itemN + 9):
##                if itemNN in coordinate and coordinate[itemNN]['second'] in normal:
##                    dis = distance( coordinate[itemN]['x'], coordinate[itemN]['y'], coordinate[itemN]['z'], coordinate[itemNN]['x'], coordinate[itemNN]['y'],coordinate[itemNN]['z'] )
##                    Distance[coordinate[itemN]['second']][itemNN - itemN].append(dis)
##                    if coordinate[itemNN]['second'] == coordinate[itemN]['second']:
##                        DistanceSame[coordinate[itemN]['second']][itemNN - itemN].append(dis)

        if coordinate[itemN]['second'] in ['E', 'B']:
            for itemNN in coordinate[itemN]['Neighbors']:
                for itemNNN in range(itemNN - 6, itemNN + 7):
                    if itemNNN > itemN and itemNNN in coordinate:
                        dis = distance( coordinate[itemN]['x'], coordinate[itemN]['y'], coordinate[itemN]['z'], coordinate[itemNNN]['x'], coordinate[itemNNN]['y'],coordinate[itemNNN]['z'] )
                        Edistance.setdefault(abs(itemNN - itemNNN), [])
                        Edistance[abs(itemNN - itemNNN)].append(dis)

                        EdistanceSeq.setdefault(abs(itemNN - itemNNN), [])
                        EdistanceSeq[abs(itemNNN - itemNN)].append(abs(itemN - itemNNN))
                        

                        if coordinate[itemNNN]['second'] in ['E', 'B']:
                            EdistanceSame.setdefault(abs(itemNN - itemNNN), [])
                            EdistanceSame[abs(itemNN - itemNNN)].append(dis)
                            EdistanceSameSeq.setdefault(abs(itemNN - itemNNN), [])
                            EdistanceSameSeq[abs(itemNNN - itemNN)].append(abs(itemN - itemNNN))
                        


    frpdb.close()


fr.close()

##path = r'E:\NextIdea\Dataset\Distance'
##for secondaryS in Distance:
##    for itemS in Distance[secondaryS]:
##        fwN = open(path + secondaryS + str(itemS)+ '.csv', 'w')
##        for itemNum in Distance[secondaryS][itemS]:
##            fwN.write(str(itemNum) + '\n')
##
##        fwN.close()
##
##path = r'E:\NextIdea\Dataset\DistanceSame'
##for secondaryS in DistanceSame:
##    for itemS in DistanceSame[secondaryS]:
##        fwN = open(path + secondaryS + str(itemS)+ '.csv', 'w')
##        for itemNum in DistanceSame[secondaryS][itemS]:
##            fwN.write(str(itemNum) + '\n')
##
##        fwN.close()
        
path = r'E:\NextIdea\Dataset\SheetDistance'
for itemS in Edistance:
    fwN = open(path + str(itemS)+ '.csv', 'w')
    for itemNum in Edistance[itemS]:
        fwN.write(str(itemNum) + '\n')

    fwN.close()
path = r'E:\NextIdea\Dataset\SheetDistanceSame'
for itemS in EdistanceSame:
    fwN = open(path + str(itemS)+ '.csv', 'w')
    for itemNum in EdistanceSame[itemS]:
        fwN.write(str(itemNum) + '\n')

    fwN.close()

        
path = r'E:\NextIdea\Dataset\SheetDistanceSeq'
for itemS in EdistanceSeq:
    fwN = open(path + str(itemS)+ '.csv', 'w')
    for itemNum in EdistanceSeq[itemS]:
        fwN.write(str(itemNum) + '\n')

    fwN.close()
path = r'E:\NextIdea\Dataset\SheetDistanceSameSeq'
for itemS in EdistanceSameSeq:
    fwN = open(path + str(itemS)+ '.csv', 'w')
    for itemNum in EdistanceSameSeq[itemS]:
        fwN.write(str(itemNum) + '\n')

    fwN.close()
