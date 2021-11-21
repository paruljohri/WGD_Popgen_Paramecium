#This is to get any indels larger than 30 bp in CDSs to check for large protein deletions:

import sys

species = sys.argv[1]
subtype = sys.argv[2]  #_subset, _subset2
#cutoff_length = sys.argv[2]
#read the annotation file:
f_list = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/annotation.list", 'r')
for line in f_list:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        if species == line2[0]:
		name = line2[1]
                f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/" + species + "/" + name, 'r')
f_list.close()

print "reading the annotation file"
#read the annotation file
d_juncn, d_gene = {}, {}
for line in f_ann:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[2] == "CDS":
		start = int(line2[3]) - 10
		end = int(line2[4])
		gene = line2[8].split(":")[0]
		CDS = line2[0] + "-" + line2[3] + "-" + line2[4]
		d_gene[CDS] = gene
		i = start
		while i <= end:
			try:
				d_juncn[line2[0]][CDS].append(str(i))
				
			except:
				try:
					d_juncn[line2[0]][CDS] = []
					d_juncn[line2[0]][CDS].append(str(i))
				except:
					d_juncn[line2[0]] = {}
					d_juncn[line2[0]][CDS] = []
					d_juncn[line2[0]][CDS].append(str(i))
				
			i = i + 1
		#l_juncn.append(line2[0] + '_' + line2[3])
		#l_juncn.append(line2[0] + '_' + line2[4])
f_ann.close()
#print d_juncn["scaffold_001"]
#if "7730" in d_juncn["scaffold_001"]:
#	print "yes"
#else:
#	print "no"
f_ind = open("/N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped_protect/" + species + subtype + "/POPN3/" + species + "_indelsfiltQfinal.vcf", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes_protect/large_indels_VCF/" + species + "_large_indels_CDS.vcf", 'w+')
for line in f_ind:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "#CHROM":
		result.write(line1 + '\t' + "indel_length" + '\t' + "CDS" + '\t' + "gene" + '\n')
	elif line[0] != "#":
		#line1 = line.strip('\n')
		#line2 = line1.split('\t')
		#if line2[0] == "#CHROM":
		#	result.write(line1 + '\t' + "indel_length" + '\t' + "CDS" + '\t' + "gene" + '\n')
		if "," not in line2[4]:
			if len(line2[3]) > len(line2[4]):
				ind_len = len(line2[3]) - len(line2[4])
			else:
				ind_len = len(line2[4]) - len(line2[3])
			#print ind_len
			if ind_len >= 30: #10 amino acids
				try:
					#print d_juncn[line2[0]]
					#if line2[0] == "scaffold_001" and line2[1] == "7730":
					#	print "yes"
					for CDS in d_juncn[line2[0]].keys():
						if line2[1] in d_juncn[line2[0]][CDS]:
							#print line2[0] + '_' + line2[1]
							result.write(line1 + '\t' + str(ind_len) + '\t' + CDS + '\t' + d_gene[CDS] + '\n')
				except:
					print line2[0]
f_ind.close()
result.close()
print "Finished"














