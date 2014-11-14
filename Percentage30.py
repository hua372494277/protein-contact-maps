# get the PDB IDs from SCOP data set, which their sequence identity is less than 30%.
# then, save the results to idPDBchain.txt
fr = open(r'E:\NextIdea\Dataset\scopeseq-2.03-astral-scopedom-seqres-sel-gs-bib-30-2.03.id')
fw = open(r'E:\NextIdea\Dataset\idPDBchain.txt','w')


while True:
    line = fr.readline()
    if not line:
        break

    line = line.rstrip()

    if line[0] == 'd':
        domainKey = line[1:6].upper()
        fw.write(domainKey + '\n')
        
    
