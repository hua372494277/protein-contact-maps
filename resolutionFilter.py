# filter out the resolution of protein is more than 2.0 or R work > 0.2
fromP = r'E:\NextIdea\Data'
import os, shutil
file = os.listdir(fromP)
fw = open(r'E:\NextIdea\Dataset\pdb2angstroms.txt', 'w')
for item in file:
    fr = open(fromP + '\\' + item)
    resolution = 0.0
    rwork = 0.0

    #input(item + '\t' + str(resolution) + '\t' + str(rwork))
    while True:
        line = fr.readline()
        if not line:
            break

        if 'REMARK   2 RESOLUTION.' in line and 'ANGSTROMS.' in line:
            items = line.split()
            try:
                resolution = float(items[3])
            except:
                print(item + '  resolution')

            #input(item + '\t' + str(resolution) + '\t' + str(rwork))
            
            
        if 'REMARK   3   R VALUE' in line:
            pos = line.find(':')  
            rw = line[pos + 1:]

            try:
                rwork = float(rw)
            except:
                line = fr.readline()
                if 'REMARK   3   R VALUE' in line:
                    pos = line.find(':')  
                    rw = line[pos + 1:]

                    try:
                        rwork = float(rw)
                    except:
                        print(item + '  rwork' + '   ' + line)
                        break

            if rwork < 0.2 and resolution < 2.0:
                fw.write(item + '\t' + str(resolution) + '\t' + str(rwork) + '\n')
                #input(item + '\t' + str(resolution) + '\t' + str(rwork))

            break
                

    fr.close()

fw.close()
            
