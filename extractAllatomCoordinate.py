# extract the coordinates of all atoms
fromP = r'E:\NextIdea\Data'
toP = r'E:\NextIdea\allAtomCoordinate'
fr = open(r'E:\NextIdea\Dataset\scopClassHelixSheetpercentageNew.csv')

while True:
    line = fr.readline()

    if not line:
        break

    line = line.rstrip()
    items = line.split(',')
    #get the pdb files' name
    pdbname = items[0][0:4]
    chain = items[0][-1]
    #open the pdb files
    frpdb = open(fromP + '\\' + pdbname+'.pdb')
    fw = open(toP + '\\' + pdbname + chain + 'AllAtoms', 'w')
    #input(toP + '\\' + pdbname + chain + 'AllAtoms')
    #extract all atoms' coordinates
    while True:
        contentLine = frpdb.readline()
        if not contentLine:
            break

        contentLine = contentLine.rstrip()

        if 'MODEL        2' in line:
            break

        if 'ATOM' == contentLine[:4] and chain == contentLine[21]:
                ssseqi = contentLine[22:26].lstrip()
                ssseqi = ssseqi.rstrip()
                try:
                    atomseq = int(contentLine[4:11])
                except:
                    print(pdbname + chain )
                    input(contentLine + '\t' + ssseqi)
                        
                try:
                    int(ssseqi)
                except ValueError:
                    print(pdbname + chain )
                    input(contentLine + '\t' + ssseqi)
                    
                x = contentLine[30:38].lstrip()
                x = x.rstrip()
                y = contentLine[38:46].lstrip()
                y = y.rstrip()
                z = contentLine[46:54].lstrip()
                z = z.rstrip()
                try:
                    float(x)
                    float(y)
                    float(z)
                except ValueError:
                    print(pdbItem + '------float')
                    input(contentLine)
##                input(str(atomseq))    
##                input(ssseqi + '\t' + x + '\t' + y + '\t' + z + '\n')
                fw.write( str(atomseq) + '\t' + str(ssseqi) + '\t' + str(x) + '\t' + str(y))
                fw.write( '\t' + str(z) + '\n')
        

    frpdb.close()
    #input('ok')
    fw.close()

fr.close()
