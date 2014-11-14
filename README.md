protein-contact-maps
====================

These codes is used to analyze the protein contact maps.

Percentage30.py  ---  get the PDB IDs from SCOP data set, which their sequence identity is less than 30%.

idPDBchain.txt --- the results got by executing Percentage30.py

resolutionFilter.py --- filter out the resolution of protein is more than 2.0 or R work > 0.

attainDsspInfor.py --- get the DSSP annotations for each protein chain.

detectHole.py --- filter out the chain with holes - missing residues

compareSecondartDistance.py --- calculating the Euclidean distance between residues with different sequence distance

extractAllatomCoordinate.py --- extract the coordinates of all atoms

allAtomNetwork.py --- calculate the clustering coefficient, characteristic path length, entropy, assortativity coefficient, Diameter and Radius of the network based on the coordinate of all atoms

networkCatom.py ---  calculate the clustering coefficient, characteristic path length, entropy, assortativity coefficient, Diameter and Radius of the network based on the coordinate of C atoms

randomNNcontactmap.py --- randomNN algorithm

randSSAndRandSN.py --- RandSS and RandSN algorithms

