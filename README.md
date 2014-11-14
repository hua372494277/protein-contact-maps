protein-contact-maps
====================

These codes is used to analyze the protein contact maps.

Percentage30.py  ---  get the PDB IDs from SCOP data set, which their sequence identity is less than 30%.
idPDBchain.txt --- the results got by executing Percentage30.py
resolutionFilter.py --- filter out the resolution of protein is more than 2.0 or R work > 0.
attainDsspInfor.py --- get the DSSP annotations for each protein chain.
detectHole.py --- filter out the chain with holes - missing residues
