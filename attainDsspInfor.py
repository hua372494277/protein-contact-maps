# get the DSSP annotations for each protein chain
import os

fr = open(r'D:\dataForPaper\standardBenchmark\Final\benchmark 156.txt')

allPDB = []
while True:
    line = fr.readline()
    if not line:
        break
    items = line.split()
    allPDB.append(items[0])

fr.close()

for item in allPDB:
    command = "D:\\dataForPaper\\dssp-2.0.4-win32.exe -i D:\\dataForPaper\\domainPDBfiles\\"
    command += item
    command += '.pdb  '
    command += '-o  D:\\dataForPaper\\dsspInfo\\'
    command += item[0:4] + '.dssp'
    input(command)
    try:
        state = os.system(command)
        if state:
            print(item)
    except:
        print(item)
            
