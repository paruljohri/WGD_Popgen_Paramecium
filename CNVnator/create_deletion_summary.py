#This is to create summary file for deletions:

import sys

species = sys.argv[1]
cutoff = sys.argv[2]

f_cnv = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + species + ".genes.cnv", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/deletion_analysis/" + species + "_" + cutoff + ".deletions", 'w+')
d_length = {}
l_genes = []
for line in f_cnv:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "Sample":
		result.write("gene" + '\t' + "samples-bases-fractiondeleted" + '\n')
	else:
		sample = line2[0]
		size = line2[3]
		if line2[1] == "deletion" and int(size) <= int(cutoff):
			for x in line2[10:]:
				gene = x.split(";")[0]
				bases = x.split(";")[1]
				fraction = x.split(";")[2]
				if gene not in l_genes:
					l_genes.append(gene)
				print gene
				try:
					d_length[gene][sample].append(bases)
				except:
					try:
						d_length[gene][sample] = []
						d_length[gene][sample].append(bases)
					except:
						d_length[gene] = {}
						d_length[gene][sample] = []
						d_length[gene][sample].append(bases)
				#try:
				#	d_samples[gene].append(sample + "-" + bases + "-" + fraction)
				#except:
				#	d_samples[gene] = []
				#	d_samples[gene].append(sample + "-" + bases + "-" + fraction)
f_cnv.close()

for gene in l_genes:
	result.write(gene + '\t')
	for sample in d_length[gene].keys():
		result.write(sample + "-" + '+'.join(d_length[gene][sample]) + ";")
	result.write('\n')
result.close()

print "Finished"







