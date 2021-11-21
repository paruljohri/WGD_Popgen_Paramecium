#This is to get properties of genes with deletions/ insertions. Esp the percentage of the protein that is affected.

import sys

species = sys.argv[1]

f_ind = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/large_indels_VCF/" + species + "_large_indels_CDS.vcf", 'r')
d_len = {}

for line in f_ind:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2.pop()[3:]
	line2.pop()
	ind_len = int(line2.pop())
	try:
		d_len[gene] = d_len[gene] + ind_len
	except:
		d_len[gene] = ind_len
f_ind.close()
print d_len

f_char = open("/N/dc2/scratch/pjohri/Paramecium/genomes/" + species + "/" + species + "_genes_CDS.char", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/large_indels_analysis/" + species + "_large_indels_CDS.char", 'w+')
result.write("gene	gene_length	indel_length	indel_perc	status	ext_status" + '\n')

for line in f_char:
	print line
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[0]
	try:
		print d_len[gene]
		result.write(gene + '\t' + line2[1] + '\t' + str(d_len[gene]) + '\t' + str((d_len[gene]/float(line2[1]))*100.00) + '\t' + line2[3] + '\t' + line2[4] + '\n')
	except:
		print gene
f_char.close()
result.close()
print "Finished"





















