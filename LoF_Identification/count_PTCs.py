# This is to count genes with pre-termination stop codons:

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
	f_fasta = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_prot_VCF/" + indv, 'r')
	result1 = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_PTC_VCF/" + indv, 'w+')
	#result2 = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_noSTART_VCF/" + indv, 'w+')
	result3 = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_noSTOP_VCF/" + indv, 'w+')
	result4 = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_NK_VCF/" + indv, 'w+')
        d_fasta = read_fasta(f_fasta)
        for gene in d_fasta.keys():
		seq = d_fasta[gene]
		length = len(seq)
		if seq.count("-")/float(length) > 0.3:
			result4.write(">" + gene + '\n' + seq + '\n')
		else:
			#if seq[0] != "M" and seq[0] != "I" and seq[0] != "V" and seq[0] != "-":
				#result2.write(">" + gene + '\n' + seq + '\n')
			if seq[length-4:length] == "Stop":
				 
				num = d_fasta[gene].count("Stop")
				if num > 1:
					#print gene
					result1.write(">" + gene + '\n' + seq + '\n')
			else:
				if seq[length-1] != "-":
					result3.write(">" + gene + '\n' + seq + '\n')
				if "Stop" in seq:
					result1.write(">" + gene + '\n' + seq + '\n')
	f_fasta.close()
        result1.close()
	#result2.close()
	result3.close()
	result4.close()

print "Finished"













