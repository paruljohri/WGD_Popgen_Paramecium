#This is to get the names of the genes that are present in the deletions and duplications:

import sys

species = sys.argv[1]

#open the annotation file:
if species == "tetraurelia":
	f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/tetraurelia/tetraurelia51_EuGene_annotation_edit.gff", 'r')
elif species == "biaurelia":
	f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/biaurelia/biaurelia_V1-4_annotation_v1.gff3", 'r')
elif species == "sexaurelia":
	f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/sexaurelia/sexaurelia_AZ8-4_annotation_v1.gff3", 'r')
elif species == "caudatum":
	f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/caudatum/caudatum_43c3d_annotation_v1.gff3", 'r')
d_gene = {}
d_len = {}
d_start, d_end = {}, {}
d_strand = {}
for line in f_ann:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	scaffold = line2[0]
	if line2[2] == "CDS":
		gene0 = line2[8].split(":")[0]
		gene = gene0[3:]
		d_strand[gene] = line2[6]
		start = int(line2[3])
		end = int(line2[4])
		if d_start.get(gene, "NA") == "NA":
			d_start[gene] = start
		if d_end.get(gene, 0) < end:
			d_end[gene] = end
		while start <= end:
			site = scaffold + '\t' + str(start)
			d_gene[site] = gene
			d_len[gene] = d_len.get(gene, 0) + 1
			start = start + 1
f_ann.close()
#print d_len
#print d_start["PTETEGNC38487"]
#print d_end["PTETEGNC38487"]
#open the CNVnator result file:
f_cnv = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + species + ".filter1.cnv", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + species + ".genes.position.cnv", 'w+')
#d_len_affected = {}

for line in f_cnv:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "Sample":
		result.write(line1 + '\t' + "gene;deleted_position" + '\n')
	else:
		result.write(line1)
		scaffold = line2[2].split(":")[0]
		coord = line2[2].split(":")[1]
		start = int(coord.split("-")[0])
		end = int(coord.split("-")[1])
		l_genes = []
		d_len_affected = {}
		while start <= end:
			site = scaffold + '\t' + str(start)
			gene = d_gene.get(site, "NA")
			if gene != "NA":
				try:
					d_len_affected[gene].append(start)
				except:
					d_len_affected[gene] = []
					d_len_affected[gene].append(start)
				if gene not in l_genes:
					l_genes.append(gene)
			start = start + 1
		print l_genes
		#print d_len_affected
		#write in file:
		for x in l_genes:
			s_min = min(d_len_affected[x])
			s_max = max(d_len_affected[x])
			pos_min = float(s_min - d_start[x])/float(d_end[x] - d_start[x])
			pos_max = float(s_max - d_start[x])/float(d_end[x] - d_start[x])
			#print x + '\t' + d_len_affected[x] + '\t' + d_len[x]
			if d_strand[x] == "+":
				result.write('\t' + x + ';' + str(len(d_len_affected[x])) + ";" + str(pos_min) + "-" + str(pos_max))
			elif d_strand[x] == "-":
				result.write('\t' + x + ';' + str(len(d_len_affected[x])) + ";" + str(1.0 - pos_max) + "-" + str(1.0 - pos_min))
		result.write('\n')

f_cnv.close()
result.close()
print "Finished"

