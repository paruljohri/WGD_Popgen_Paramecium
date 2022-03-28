#This is to make files for scaffolds of different species

import sys
species = sys.argv[1]

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
                        name = line.strip('\n')

        data[name[1:]] = sequence
        return data

#get annotation file:
f_list = open("/N/dc2/scratch/pjohri/assembly_protect/assembly.list", 'r')
for line in f_list:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == species:
		f_ass = open("/N/dc2/scratch/pjohri/assembly_protect/" + species + "/" + line2[1], 'r')
f_list.close()
if species == "caudatum":
	f_ass = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/caudatum/caudatum_43c3d_assembly_v1.fasta", 'r')

d_ass = read_fasta(f_ass)

f_ass.close()

for scaffold in d_ass.keys():
	result = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + scaffold + ".fa", 'w+')
	result.write(">" + scaffold + '\n')
	result.write(d_ass[scaffold])
	result.close()

print "Finished"











