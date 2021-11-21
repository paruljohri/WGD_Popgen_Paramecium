#This is to get genes that have frame-shift indels (of size non 3n), but only one indel in one individual or such that the sum of them is not 3n

import sys

species = sys.argv[1]
folder = sys.argv[2]

#store information on which individuals have indels:
f_vcf = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis_protect/" + species + folder + "/" + species + "_indelsfiltQfinal_genes.vcf", 'r')
d_indv, d_gt = {}, {}
d_mark_hetero = {}
d_sp = {}
l_cols = []
for line in f_vcf:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2.pop()
	if line2[0] == "CHROM":
		i = 0
		for x in line2:
			if "BAM_SORTED" in x:
				y1 = x.split(".")[0]
				y = y1.split("/")[1]
				d_sp[i] = y
				l_cols.append(i)
			i = i + 1
	else:
		site = line2[0] + '\t' + line2[1]
		l_ind, l_gt = [], []
		j = 0
		for x in line2:
			if j in l_cols:
				gt = x.split(":")[0]
				if gt == "1/1":
					l_ind.append(d_sp[j])
					#l_gt.append(gt)
				elif gt == "0/1" or gt == "1/0":
					d_mark_hetero[d_sp[j] + '_' + gene] = 1
			j = j + 1
		d_indv[site] = l_ind
		#d_gt[site] = l_gt
f_vcf.close()
print "These are genes in strains that have heterozygous indels:"
print d_mark_hetero

#get isolates of species:
f_list = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/" + species + ".list", 'r')
d_strain_ind = {}
l_strains = []
d_posn = {}#this is to try to record the position of the indels causing frameshift
for line in f_list:
	line1 = line.strip('\n')
	d_strain_ind[line1] = {}
	d_posn[line1] = {}
	l_strains.append(line1)
f_list.close()

#adding all indel lengths in each gene for each strain to check if they result in a frame shift eventually
f_ind = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis_protect/" + species + folder + "/" + species + "_indelsfiltQfinal_genes.summary", 'r')
for line in f_ind:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "scaffold":
		site = line2[0] + '\t' + line2[1]
		length = line2[5]
		gene = line2[7]
		#if length%3 != 0: #is not mod3
		
		for strain in d_indv[site]:
			d_strain_ind[strain][gene] = d_strain_ind[strain].get(gene, 0) + int(length)
			try:
				d_posn[strain][gene].append(site)
			except:
				d_posn[strain][gene] = []
				d_posn[strain][gene].append(site)
f_ind.close()

#writing:
result_posn = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/my_consensus_frameshift/" + species + "_frameshift_posn.txt", 'w+')
for strain in l_strains:
	result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/my_consensus_frameshift/" + strain + ".list", "w+")
	for gene in d_strain_ind[strain]:
		if d_mark_hetero.get(strain + '_' + gene, "NA") != 1:#these genes did not have any heterozygous indel SNP
			if int(d_strain_ind[strain][gene])%3!=0:
				result.write(gene + '\t' + str(d_strain_ind[strain][gene]) + '\n')
				result_posn.write(strain + '\t' + gene)
				for x in d_posn[strain][gene]:
					result_posn.write('\t' + x)
				result_posn.write('\n')
	result.close()
result_posn.close()
print "Finished"






