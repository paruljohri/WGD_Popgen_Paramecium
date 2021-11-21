#This is to get properties of genes with PTCs.

import sys

species = sys.argv[1]

#read the samples
f_list = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + ".list", 'r')
l_samples = []
for line in f_list:
        line1 = line.strip('\n')
        l_samples.append(line1)
f_list.close()


d_indv, d_num = {}, {}
for sample in l_samples:
	f_nostop = open("/N/slate/pjohri/Paramecium/CNSGenomes/my_consensus_noSTOP_VCF/" + sample + "_homo.fasta", 'r')
	for line in f_nostop:
		line1 = line.strip('\n')
		if line1[0] == ">":
			gene = line1[1:]
			try:
				d_indv[gene].append(sample)
				d_num[gene] = d_num[gene] + 1
			except:
				d_indv[gene] = []
				d_indv[gene].append(sample)
				d_num[gene] = 1
	f_nostop.close()



f_char = open("/N/slate/pjohri/Paramecium/genomes/" + species + "/" + species + "_genes_CDS.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/noSTOP_analysis/" + species + "_noSTOP_genes.char", 'w+')

d_char = {}
for line in f_char:
	#print line
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[0]
	if gene == "gene":
		result.write(line1 + '\t' + "num_indv" + '\t' + "samples" + '\n') 
	else:
		d_char[gene] = line1
f_char.close()

for gene in d_indv.keys():
	print (gene)
	print (d_char[gene])
	print (d_num[gene])
	print (d_indv[gene])
	result.write(d_char[gene] + '\t' + str(d_num[gene]) + '\t' + ";".join(d_indv[gene]) + '\n')
result.close()
print ("Finished")





















