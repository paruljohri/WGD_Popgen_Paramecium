#This is to get properties of genes with PTCs.

import sys

species = sys.argv[1]

#read the samples
f_list = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/" + species + ".list", 'r')
l_samples = []
for line in f_list:
        line1 = line.strip('\n')
        l_samples.append(line1)
f_list.close()


d_indv, d_num = {}, {}
for sample in l_samples:
	f_fs = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/my_consensus_frameshift/" + sample + ".list", 'r')
	for line in f_fs:
		line1 = line.strip('\n')
		line2 = line1.split('\t')
		#if line1[0] == ">":
		gene = line2[0]
		try:
			d_indv[gene].append(sample)
			d_num[gene] = d_num[gene] + 1
		except:
			d_indv[gene] = []
			d_indv[gene].append(sample)
			d_num[gene] = 1
	f_fs.close()

f_char = open("/N/dc2/scratch/pjohri/Paramecium/piNpiS_protect/cutoff_thetaS_5/" + species + ".charac", 'r')
d_NS = {}
for line in f_char:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        gene = line2[0] #.replace("EGNC", "P")
        #gene = gene0.replace("GNC", "P")
        d_NS[gene] = line2[8]
f_char.close()
#print d_NS
f_char = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/" + species + "/" + species + "_genes_CDS.char", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/frameshift_analysis/" + species + "_frameshift_genes.char", 'w+')

d_char = {}
for line in f_char:
	#print line
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[0]
	if gene == "gene":
		result.write(line1 + '\t' +"piNpiS" + '\t' +  "num_indv" + '\t' + "samples" + '\n') 
	else:
		d_char[gene] = line1
f_char.close()

for gene in d_indv.keys():
	print gene
	#print d_NS[gene]
	result.write(d_char[gene] + '\t' + d_NS.get(gene, "NA") + '\t' + str(d_num[gene]) + '\t' + ";".join(d_indv[gene]) + '\n')
result.close()
print "Finished"





















