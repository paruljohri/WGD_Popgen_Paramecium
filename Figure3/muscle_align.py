#This is to align protein sequences using mega

import sys
import os

l_species = ["ptet", "poct", "pprim", "pbi", "ppent", "psex", "psept", "pnov", "pdec", "pdodec", "ptre", "pquad", "pjen", "pson"]
#l_species = ["ptet", "poct", "pdec", "pdodec", "pbi"]
#read the family neames:
for species in l_species:
	print species
	os.system("rm -r /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_aln")
	os.system("mkdir /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_aln")
	l_families = []
	f_list = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + ".list", 'r')
	for line in f_list:
		line1 = line.strip('\n')
		l_families.append(line1)
	f_list.close()
	for fam in l_families:
		fam_name = fam.split(".")[0]
		os.system("muscle -in /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "/" + fam + " -out /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_aln/" + fam)
		#os.system("/N/dc2/scratch/pjohri/Tools/mega/./megacc -a ../megaproto_commandfiles/muscle_align_protein.mao -d /N/dc2/scratch/pjohri/Paramecium_all_sp/tajima_rate_test/" + species + "/" + fam + " -o /N/dc2/scratch/pjohri/Paramecium_all_sp/tajima_rate_test/" + species + "_aln/" + fam_name)


print "Finsihed"






