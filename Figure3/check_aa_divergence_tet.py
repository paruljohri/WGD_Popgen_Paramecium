#This is to get aa divergence between the copy that has nonfunctional polymorphism versus intact copies:
#only for tet
import sys

species = sys.argv[1]
if species == "ptet":
	full_name = "tetraurelia"
#read all genes with ninfunctional polymorphisms:
f_char = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/CNSGenomes_new_annotation/tetraurelia/all_genes.char", 'r')
d_status = {}
for line in f_char:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	d_status[line2[0].replace(".T", ".P")] = line2[1]

f_char.close()

#get change in aa
f_rate = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/results/" + species + "_rates.txt", 'r')
d_aa, d_aa_len, d_p = {}, {}, {}
for line in f_rate:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "family":
		gene1 = line2[2].replace(".C", ".P")
		gene2 = line2[3].replace(".C", ".P")
		tot = line2[4]
		d_aa[gene1] = line2[5]
		d_aa[gene2] = line2[6]
		d_p[gene1] = line2[7]
		d_p[gene2] = line2[7]
		d_aa_len[gene1] = str(float(line2[5])/float(tot))
		d_aa_len[gene2] = str(float(line2[6])/float(tot))	
		
f_rate.close()

result = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/aa_divergence_tet/" + species + ".txt", 'w+')
result_len = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/aa_divergence_tet/" + species + "_per_len.txt", 'w+')
result.write("state" + '\t' + "gene1" + '\t' + "gene2" + '\t' + "diff_aa1" + '\t' + "diff_aa2" + '\t' + "pval" + '\n')
result_len.write("state" + '\t' + "gene1" + '\t' + "gene2" + '\t' + "diff_aa1" + '\t' + "diff_aa2" + '\t' + "pval" + '\n')

#write it
f_para = open("/N/dc2/projects/paramecium/BigProject/FILES/" + species + ".WGD1.tree", 'r')
for line in f_para:
	line0 = line.strip('\n')
	line1 = line0.strip('\r')
	line2 = line1.split('\t')
	gene1 = line2[3]
	gene2 = line2[4]
	if gene1 != "." and gene2 != "." and "Paralogon" in line2[0]:
		if d_status[gene1] == "NA" and d_status[gene2] == "NA":
			result.write("intact" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa.get(gene1, "NA") + '\t' + d_aa.get(gene2, "NA") + '\t' + d_p.get(gene1, "NA") + '\n')
			result_len.write("intact" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa_len.get(gene1, "NA") + '\t' + d_aa_len.get(gene2, "NA") + '\t' + d_p.get(gene1, "NA") + '\n')
		else:
			if d_status[gene1] != "NA" and d_status[gene2]!="NA":
				result.write("nonfunc12" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa.get(gene1, "NA") + '\t' + d_aa.get(gene2, "NA") +'\t' + d_p.get(gene1, "NA") + '\n')
				result_len.write("nonfunc12" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa_len.get(gene1, "NA") + '\t' + d_aa_len.get(gene2, "NA") +'\t' + d_p.get(gene1, "NA") + '\n')
			elif d_status[gene1] != "NA":
				result.write("nonfunc1" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa.get(gene1, "NA") + '\t' + d_aa.get(gene2, "NA") +'\t' + d_p.get(gene1, "NA")  + '\n')
				result_len.write("nonfunc1" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa_len.get(gene1, "NA") + '\t' + d_aa_len.get(gene2, "NA") +'\t' + d_p.get(gene1, "NA")  + '\n')
			else:
				result.write("nonfunc2" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa.get(gene1, "NA") + '\t' + d_aa.get(gene2, "NA") +'\t' + d_p.get(gene1, "NA")  + '\n')
				result_len.write("nonfunc2" + '\t' + gene1 + '\t' + gene2 + '\t' +  d_aa_len.get(gene1, "NA") + '\t' + d_aa_len.get(gene2, "NA") +'\t' + d_p.get(gene1, "NA")  + '\n')


result.close()
result_len.close()
f_para.close()
print "Finished"








