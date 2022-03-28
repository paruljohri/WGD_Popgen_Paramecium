#This is to get a simple summary of different gene types or sites. This is because the file is too large to read in R.

import sys
species = sys.argv[1]
if species == "sexaurelia":
	tot_chr = 20
if species == "biaurelia":
	tot_chr = 18

f_sfs = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis/" + species + "3/" + species + "_SFS_0AF_corrected.txt", 'r')
l_4_dup, l_0_dup, l_4_sin, l_0_sin, l_4_ret, l_0_ret = [], [], [], [], [], []
l_4_high, l_0_high, l_4_low, l_0_low = [], [], [], []
d_col = {}
for line in f_sfs:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "chrom":
		col = 0
		for x in line2:
			d_col[x] = col
			col = col + 1
	else:
		if line2[d_col["num_chr_tot"]] == str(tot_chr):
			if line2[d_col["heterozygous"]] == "no":
				if line2[d_col["status"]] == "duplicate":
					if line2[d_col["site"]] == "4":
						l_4_dup.append(line2[d_col["num_chr_minor_allele"]])
					elif line2[d_col["site"]] == "1":
						l_0_dup.append(line2[d_col["num_chr_minor_allele"]])
				elif line2[d_col["status"]] == "single":
                                        if line2[d_col["site"]] == "4":
                                                l_4_sin.append(line2[d_col["num_chr_minor_allele"]])
                                        elif line2[d_col["site"]] == "1":
                                                l_0_sin.append(line2[d_col["num_chr_minor_allele"]])
				if line2[d_col["ext_status"]] == "retained":
					if line2[d_col["site"]] == "4":
                                                l_4_ret.append(line2[d_col["num_chr_minor_allele"]])
                                        elif line2[d_col["site"]] == "1":
                                                l_0_ret.append(line2[d_col["num_chr_minor_allele"]])
				if line2[d_col["exp_category"]] == "higher":
					if line2[d_col["site"]] == "4":
                                                l_4_high.append(line2[d_col["num_chr_minor_allele"]])
                                        elif line2[d_col["site"]] == "1":
                                                l_0_high.append(line2[d_col["num_chr_minor_allele"]])
				elif line2[d_col["exp_category"]] == "lower":
                                        if line2[d_col["site"]] == "4":
                                                l_4_low.append(line2[d_col["num_chr_minor_allele"]])
                                        elif line2[d_col["site"]] == "1":
                                                l_0_low.append(line2[d_col["num_chr_minor_allele"]])
f_sfs.close()

#Make histgram:
print("For all duplicates, 4-fold:" + '\t' + str(len(l_4_dup)))
print("For all duplicates, 0-fold:" + '\t' + str(len(l_0_dup)))
print("For all singlecopy, 4-fold:" + '\t' + str(len(l_4_sin)))
print("For all singlecopy, 0-fold:" + '\t' + str(len(l_0_sin)))
print("For all duplicates retained in all, 4-fold:" + '\t' + str(len(l_4_ret)))
print("For all duplicates retained in all, 0-fold:" + '\t' + str(len(l_0_ret)))
print("For all duplicates with higher expression, 4-fold:" + '\t' + str(len(l_4_high)))
print("For all duplicates with higher expression, 0-fold:" + '\t' + str(len(l_0_high)))
print("For all duplicates with lower expression, 4-fold:" + '\t' + str(len(l_4_low)))
print("For all duplicates with lower expression, 0-fold:" + '\t' + str(len(l_0_low)))
print ("done")

