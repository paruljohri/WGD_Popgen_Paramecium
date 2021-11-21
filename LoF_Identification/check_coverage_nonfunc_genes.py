#This is simply to test 2 things- if the coverage of such genes is higher or if they are over-represented in strin-specific dulications:

import sys

species = sys.argv[1]
subtype = sys.argv[2]

#read the annotation file:
f_list = open("/N/slate/pjohri/Paramecium/genomes/annotation.list", 'r')
for line in f_list:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        if species == line2[0]:
                f_ann = open("/N/slate/pjohri/Paramecium/genomes/" + species + "/" + line2[1], 'r')
f_list.close()

#read the gene coordinates
print ("reading the gene coordinates")
d_dp, d_coord = {}, {}
for line in f_ann:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[2] == "gene":
		gene = line2[8].split(";")[0][3:]
		gene1 = gene.replace("GNG", "GNC")
		gene2 = gene1.replace("CAUDG", "CAUDC")
		#print gene2
		scf = line2[0]
		start = int(line2[3])
		end = int(line2[4])
		while start <= end:
			d_coord[scf + '\t' + str(start)] = gene2
			start = start + 1
f_ann.close()

#get pop coverage from gfe file
print ("reading the pop coverage")
d_dp_sum, d_dp_num = {}, {}
f_gfe = open("/N/slate/pjohri/Paramecium/GFE_analysis/" + species + subtype + "/Out_GFE_" + species + ".pi", 'r')
for line in f_gfe:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0]!="scaffold":
		site = line2[0] + '\t' + line2[1]
		gene = d_coord.get(site, "NA")
		if gene != "NA" and line2[5]!="NA" and line2[6]!="NA":
			try:
				if float(line2[6]) > 0.0:
					d_dp_sum[gene] = d_dp_sum[gene] + (float(line2[5])/float(line2[6]))
					d_dp_num[gene] = d_dp_num[gene] + 1
			except:
				if float(line2[6]) > 0.0:
					d_dp_sum[gene] = float(line2[5])/float(line2[6])
					d_dp_num[gene] = 1
f_gfe.close()
#print d_dp_num
#get their cnvnator status from those files
print ("reading the duplication status")
f_cnv = open("/N/slate/pjohri/Paramecium/CNVnator/" + species + "/" + species + ".genes.cnv", 'r')
d_dup_status = {}
for line in f_cnv:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0]!="Sample":
		if line2[1] == "duplication":
			if int(line2[3]) <= 2000:
				#l_genes = line2[10].split(";")
				for x in line2[10:]:
					y = x.split(";")[0]
					print (y)
					try:
						d_dup_status[y] += 1
					except:
						d_dup_status[y] = 1
						
f_cnv.close()
#write it as another column in all_char file
print ("writing in file")
f_char = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_depth.char", 'w+')

for line in f_char:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		result.write(line1 + '\t' + "pop_coverage" + '\t' + "duplication_num_indv" + '\n')
	else:
		result.write(line1)
		gene = line2[0]
		try:
			result.write('\t' + str(d_dp_sum[gene]/d_dp_num[gene]))
		except:
			result.write('\t' + "NA")
		result.write('\t' + str(d_dup_status.get(gene, "NA")) + '\n')
f_char.close()
result.close()

print ("Finished")
