#This is to align protein sequences using mega

import sys
import os

l_species = ["pprim", "pbi", "ptet", "ppent", "psex", "psept", "poct", "pnov", "pdec", "pdodec", "ptre", "pquad", "pjen", "pson"]
#l_species = ["ptet", "poct", "pdec", "pdodec", "pbi"]
#read the family neames:
for species in l_species:
	print species
	os.system("rm -r /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_rate")
	os.system("mkdir /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_rate")
	l_families = []
	f_list = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + ".list", 'r')
	for line in f_list:
		line1 = line.strip('\n')
		l_families.append(line1)
	f_list.close()
	for fam in l_families:
		fam_name = fam.split(".")[0]
		os.system("/N/dc2/scratch/pjohri/Tools_protect/mega/./megacc -a ../megaproto_commandfiles/tajima_rel_rate_test_protein.mao -d /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_aln/" + fam_name + "_ordered.fasta -o /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_rate/" + fam_name)


print "Finished"






