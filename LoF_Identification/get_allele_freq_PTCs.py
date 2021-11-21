#This is to get the allel frequency of each gene that is being lost:

import sys

species = sys.argv[1]
d_nonfunc = {}

#get list of samples:

f_list = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + ".list", 'r')
l_samples = []
for line in f_list:
	line1 = line.strip('\n')
	l_samples.append(line1)
f_list.close()
#tot_ind = len(l_samples)
#print tot_ind
#initializing
d_NK = {}
for sample in l_samples:
	d_NK[sample] = []

#getting list of genes that are not known (NK)
#These are basically genes that don't have sufficient coverage to call any PTCs

for sample in l_samples:
	f_NK = open("/N/slate/pjohri/Paramecium/CNSGenomes/my_consensus_NK_VCF/" + sample + "_homo.fasta", 'r')
	for line in f_NK:
		line1 = line.strip('\n')
		if line1[0] == ">":
			d_NK[sample].append(line1[1:])
	f_NK.close()

d_NK_ind = {}
for sample in l_samples:
	for gene in d_NK[sample]:
		try:
			d_NK_ind[gene] = d_NK_ind[gene] + 1
		except:
			d_NK_ind[gene] = 1
#print d_NK_ind["PTETEGNC31321"]

#getting total number of individuals that have that gene:
d_tot_ind = {}
d_tot_samples = {}
for sample in l_samples:
	f_prot = open("/N/slate/pjohri/Paramecium/CNSGenomes/my_consensus_prot_VCF/" + sample + "_homo.fasta", 'r')
	for line in f_prot:
		line1 = line.strip('\n')
		if line1[0] == ">":
			gene = line1[1:]
			try:
				d_tot_ind[gene] = d_tot_ind[gene] + 1
				if gene not in d_NK[sample]:
					d_tot_samples[gene] = d_tot_samples[gene] + ";" + sample
			except:
				d_tot_ind[gene] = 1
				if gene not in d_NK[sample]:
					d_tot_samples[gene] = sample
	f_prot.close()



#calculating AFs for PTC genes:
print ("PTCs")
f_PTC = open("/N/slate/pjohri/Paramecium/CNSGenomes/PTC_analysis/" + species + "_PTC_genes.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/PTC_analysis/" + species + "_PTC_genes_af.char", 'w+')

for line in f_PTC:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		result.write(line1 + '\t' + "AF" + '\n')
	else:
		gene = line2[0]
		d_nonfunc[gene] = "T"
		try:
			print (d_NK_ind[gene])
		except:
			d_NK_ind[gene] = 0
		num_ind = line2[7]
		if d_tot_ind[gene] - d_NK_ind[gene] != 0:
			AF = float(num_ind) / float(d_tot_ind[gene] - d_NK_ind[gene])
		else:
			AF = "NA" 
		result.write(line1 + '\t' + str(AF) + '\n')
f_PTC.close()
result.close()


#calculating AFs for noSTART genes:
print ("noSTART genes")
f_noST = open("/N/slate/pjohri/Paramecium/CNSGenomes/noSTART_analysis/" + species + "_noSTART_genes.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/noSTART_analysis/" + species + "_noSTART_genes_af.char", 'w+')

for line in f_noST:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		result.write(line1 + '\t' + "AF" + '\n')
	else:
		gene = line2[0]
		d_nonfunc[gene] = "T"
		try:
			print (d_NK_ind[gene])
		except:
			d_NK_ind[gene] = 0
		num_ind = line2[6]
		#print tot_ind - d_NK_ind[gene]
		if (d_tot_ind[gene] - d_NK_ind[gene]) != 0:
			AF = float(num_ind) / float(d_tot_ind[gene] - d_NK_ind[gene])
		else:
			AF = "NA"
		result.write(line1 + '\t' + str(AF) + '\n')
f_noST.close()
result.close()	

#calculating AFs for large indel genes:
#print "large indels"
#f_IND = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/large_indels_analysis/" + species + "_large_indels_CDS.char", 'r')
#result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/large_indels_analysis/" + species + "_large_indels_CDS_af.char", 'w+')

#for line in f_IND:
#	 line1 = line.strip('\n')
#	 line2 = line1.split('\t')
#	 if line2[0] == "gene":
#		 result.write(line1 + '\t' + "AF" + '\n')
#	 else:
#		 gene = line2[0]
#		print gene
#		 try:
#			 print d_NK_ind[gene]
#		 except:
#			 d_NK_ind[gene] = 0
#		 num_ind = line2[5]
#		 if tot_ind - d_NK_ind[gene] != "0":
#			 AF = float(num_ind) / float(tot_ind - d_NK_ind[gene])
#		 else:
#			 AF = "NA"
#		 result.write(line1 + '\t' + str(AF) + '\n')
#f_IND.close()
#result.close()


#calculating AFs for noSTOP genes:
print ("noSTOP")
f_noST = open("/N/slate/pjohri/Paramecium/CNSGenomes/noSTOP_analysis/" + species + "_noSTOP_genes.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/noSTOP_analysis/" + species + "_noSTOP_genes_af.char", 'w+')

for line in f_noST:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		result.write(line1 + '\t' + "AF" + '\n')
	else:
		gene = line2[0]
		d_nonfunc[gene] = "T"
		try:
			print (d_NK_ind[gene])
		except:
			d_NK_ind[gene] = 0
		num_ind = line2[6]
		if d_tot_ind[gene] - d_NK_ind[gene] != 0:
			AF = float(num_ind) / float(d_tot_ind[gene] - d_NK_ind[gene])
		else:
			AF = "NA"
		result.write(line1 + '\t' + str(AF) + '\n')
f_noST.close()
result.close()

#calculating AFs for framshift genes:
print ("frameshift")
f_fs = open("/N/slate/pjohri/Paramecium/CNSGenomes/frameshift_analysis/" + species + "_frameshift_genes.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/frameshift_analysis/" + species + "_frameshift_genes_af.char", 'w+')

for line in f_fs:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		result.write(line1 + '\t' + "AF" + '\n')
	else:
		gene = line2[0]
		d_nonfunc[gene] = "T"
		print (gene)
		num_ind = line2[7]
		#print d_tot_ind[gene]
		#print d_NK_ind.get(gene, 0)
		if d_tot_ind.get(gene, "NA") == "NA":
			AF = "NA"
		elif d_tot_ind[gene] - d_NK_ind.get(gene, 0) != 0:
			print (d_tot_ind[gene])
			print (d_NK_ind.get(gene, 0))
			AF = float(num_ind) / float(d_tot_ind[gene] - d_NK_ind.get(gene, 0))
		else:
			AF = "NA"
		result.write(line1 + '\t' + str(AF) + '\n')
f_fs.close()
result.close()

#write out intact genes and their AF:
print ("intact")
#f_fs = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/frameshift_analysis/" + species + "_frameshift_genes.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/intact_analysis/" + species + "_intact_genes_af.char", 'w+')
result.write("gene" + '\t' + "tot_num_indv" + '\t' + "AF" + '\t' + "Samples" + '\n')
for gene in d_tot_ind.keys():
	if d_nonfunc.get(gene,"NA") != "T": #this gene has no nonfunctional mutation
		print (gene)
		if d_tot_ind[gene] - d_NK_ind.get(gene, 0) > 0:
			num_ind = d_tot_ind[gene] - d_NK_ind.get(gene, 0)
			AF = float(num_ind) / float(d_tot_ind[gene] - d_NK_ind.get(gene, 0))
		else:
			num_ind = "NA"
			AF = "NA"
		result.write(gene + '\t' + str(num_ind) + '\t' + str(AF) + '\t' + d_tot_samples.get(gene,"none") + '\n')

result.close()



print ("Finished")













