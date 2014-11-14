#filter out the chain with holes - missing residues
fromP = r'E:\NextIdea\pdbChain'
import os
file = os.listdir(fromP)

lengthOf2Colume = len('    1    3')

fw = open(r'E:\NextIdea\Dataset\holePDBId.txt', 'w')
for itemF in file:
    fr = open(fromP + '\\' + itemF)
    countLine = 0
    
    while True:
        line = fr.readline()
        if not line:
            break

        column3 = line[0:lengthOf2Colume]

        itemC = column3.split()
        lenItem = len(itemC)
        
        if lenItem == 1:
##            print(itemF)
            fw.write(itemF + '  ---- a hole' + '\n')
            break

        countLine += 1

    if countLine < 50:
        fw.write(itemF + '  ---- too short' + '\n')
    fr.close()


fw.close()
                    
                

                
                
            
