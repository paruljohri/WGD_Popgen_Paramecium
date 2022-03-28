#

import sys

def read_fasta(file):
        sequence = ""
        data = {}
        for line in file:

                if line[0] != '>':
                        line0 = line.strip('\n')
                        #linem = linew.strip('\r')
                        line1 = line0.strip('\r')
                        sequence = sequence + line1

                else:

                        if sequence != "":
                                data[name[1:]] = sequence
                                sequence = ""
                        name = line.strip('\n').split()[0]

        data[name[1:]] = sequence
        return data

l_species = ["pprim", "pbi", "ptet", "ppent", "psex", "psept", "poct", "pnov", "pdec", "pdodec", "ptre", "pquad", "pjen", "pson"]
#l_species = ["ptet", "poct", "pdec", "pdodec", "pbi"]
#read the family neames:
for species in l_species:
        print species
        
        l_families = []
        f_list = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + ".list", 'r')
        for line in f_list:
                line1 = line.strip('\n')
                l_families.append(line1)
        f_list.close()
        for fam in l_families:
		print fam
                fam_name = fam.split(".")[0]
		f_fasta = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_aln/" + fam, 'r')
		d_fasta = read_fasta(f_fasta)
		f_fasta.close()
		result = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_aln/" + fam_name + "_ordered.fasta", 'w+')
		for x in d_fasta.keys():
			if "CAUD" in x or "MMN" in x:
				out = x
			else:
				result.write(">" + x + '\n' + d_fasta[x] + '\n')
		result.write(">" + out + '\n' + d_fasta[out] + '\n')
		result.close()

print "Finished"













