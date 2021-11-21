# This is to translate the consensus CDS:

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

def translate(s_ntds):
        s_aa = ""
        i = 0
        while i < len(s_ntds):
                #print s_ntds[i:i+3]
                if 'N' in s_ntds[i:i+3]:
                        s_aa = s_aa + '-'
                else:
			try:
                        	s_aa = s_aa + d_aa[s_ntds[i:i+3]]
			except:
				s_aa = s_aa + 'X'
                        #s_aa = s_aa + d_aa[s_ntds[i:i+3]]
                        #s_aa = s_aa + d_aa[s_ntds[i:i+3]]
                i = i + 3
        return s_aa

f_list = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_CDS_VCF.list", 'r')
l_samples = []
for line in f_list:
	line1 = line.strip('\n')
	l_samples.append(line1)
f_list.close()

#Reading the ciliate_nuclear_codon.table, ciliate code:
f_table = open("/N/dc2/scratch/pjohri/Paramecium/CNSgenomes/ciliate_nuclear_codon.degeneracy", 'r')
d_aa = {}
for line in f_table:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        #print line2
        if line2[0] != "Codon":
                d_aa[line2[0]] = line2[1]
                #l_codon.append(line2[0])
                #d_fold1[line2[0]] = line2[2]
                #d_fold2[line2[0]] = line2[3]
                #d_fold3[line2[0]] = line2[4]
f_table.close()
l_start = ["ATG", "ATC", "ATT", "ATA", "GTG", "GTA", "ATN", "ATV", "ATH", "ATD", "ATB", "ATM", "ATR", "ATW", "ATS", "ATY", "ATK", "GTR"]
for indv in l_samples:
	print indv
	f_fasta = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_CDS_VCF/" + indv, 'r')
	result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_prot_VCF/" + indv, 'w+')
	result_ST = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_noSTART_VCF/" + indv, 'w+')
	d_fasta = read_fasta(f_fasta)
	for gene in d_fasta.keys():
		i = 0
		mark = 0
		seq = d_fasta[gene][:]
		while i < 9:
			codon = d_fasta[gene][i:i+3]
			if codon in l_start:
				seq = d_fasta[gene][i:]
				mark = 1
				break
				#result.write(">" + gene + '\n' + translate(seq) + '\n')
			i = i + 1
		result.write(">" + gene + '\n' + translate(seq) + '\n')
		if mark == 0: #writing it in another file, if there is no start codon found within the first 12 ntds
			if seq[0] in "ATGC" and seq[1] in "ATGC" and seq[2] in "ATGC":
				result_ST.write(">" + gene + '\n' + d_fasta[gene] + '\n')
			
		#result.write(">" + gene + '\n' + translate(d_fasta[gene]) + '\n')
		
	f_fasta.close()
	result.close()
	result_ST.close()

print "Finished"










