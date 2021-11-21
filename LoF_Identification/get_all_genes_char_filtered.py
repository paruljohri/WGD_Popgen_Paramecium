#This is to filter the all_genes_char file to exclude genes 
#1. with too low or too high coverage
#2. present as tandem duplicates
#3. present as duplicates in CNVnator

import sys

species = sys.argv[1]

if species == "tetraurelia":
	upper_dp = 60
elif species == "biaurelia":
	upper_dp = 100
elif species == "sexaurelia":
	upper_dp = 90
elif species == "caudatum":
	upper_dp = 160
#get depth of cov information
f_dp = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_depth.char", 'r')
d_col = {}
d_dp, d_cnv, d_pop = {}, {}, {}
for line in f_dp:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		col = 0
		for x in line2:
			d_col[x] = col
			col += 1
	else:
		gene = line2[0]
		pop_cov = line2[d_col["pop_coverage"]]
		d_pop[gene] = pop_cov
		if pop_cov!="NA":
			#print line2[12]
			if float(pop_cov) >= 10 and float(pop_cov) <= float(upper_dp):
				d_dp[gene] = "T"
		if line2[d_col["duplication_num_indv"]] != "NA":
			if int(line2[d_col["duplication_num_indv"]]) > 1:
				d_cnv[gene] = "T"
f_dp.close()
print (d_cnv)
#get tandem duplicates
d_tan = {}
if species == "tetraurelia" or species == "biaurelia" or species == "sexaurelia": 
	f_tan = open("/N/slate/pjohri/Paramecium/tandem_duplicates/" + species + "_PTC.txt", 'r')

	for line in f_tan:
		line1 = line.strip('\n')
		line2 = line1.split('\t')
		if line2[0]!= "gene":
			d_tan[line2[0]] = "T"
	f_tan.close()
print (d_tan)
#get CNVnator duplicate information:
#f_char = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes.char", 'r')
#result = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_filtered.char", 'w+')
f_char = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_cnv_2000.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_cnv_2000_filtered.char", 'w+')

for line in f_char:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "gene":
		result.write(line1 + '\t' + "cov_per_ind" + '\n')
	else:
		gene = line2[0]
		result.write(gene + '\t')
		if d_dp.get(gene, "NA") == "T":#has enough coverage to be used
			if d_tan.get(gene, "NA") == "T":#this gene has tandem duplicate
				result.write("NA" + '\t')
				print ("tandem")
			elif d_cnv.get(gene, "NA") == "T":#this gene has isolate specific duplicate
				result.write("NA" + '\t')
				print ("cnv")
			else:
				if line2[1] == "NA":#this gene has no nonfunctional poly, so let it be (can reconsider it)
					result.write("intact" + '\t')
				else:
				#if d_tan.get(gene, "NA") == "T":#this gene has tandem duplicate
				#	result.write("NA" + '\t')
				#elif d_cnv.get(gene, "NA") == "T":#this gene has isolate specific duplicate
				#	result.write("NA" + '\t')
				#else:
					result.write(line2[1] + '\t')
				
				
		else:#not enough coverage to say anything
			result.write("NA" + '\t')
			print (gene)
		for x in line2[2:]:
			result.write(x + '\t')
		result.write(d_pop[gene] + '\n')

result.close()

print ("Finished")

