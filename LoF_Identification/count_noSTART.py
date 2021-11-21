# This is to get genes that don't have the right start codon:

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
                        name = line.strip('\n')

        data[name[1:]] = sequence
        return data

#read the samples:
f_list = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_CDS_VCF.list", 'r')
l_samples = []
for line in f_list:
        line1 = line.strip('\n')
        l_samples.append(line1)
f_list.close()

for indv in l_samples:
	print indv
	f_fasta = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_CDS_VCF/" + indv, 'r')
	result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_noSTART_VCF/" + indv, 'w+')
	d_fasta = read_fasta(f_fasta)
	for gene in d_fasta.keys():
		start = d_fasta[gene][0:3]
		if start[0] in "ATGC" and start[1] in "ATGC" and start[2] in "ATGC":
			if start[0:2] == "AT" or start == "GTG" or start == "GTA":
				print gene
			else:
				result.write(">" + gene + '\n' + d_fasta[gene] + '\n')
	result.close()
	f_fasta.close()

print "Finished"	
		















