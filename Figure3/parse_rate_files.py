#This is to parse through the rate files to get at some stats:

import sys

species = sys.argv[1]

#read family names:
l_families = []
f_list = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + ".list", 'r')
for line in f_list:
	line1 = line.strip('\n')
	fam = line1.split(".")[0]
	l_families.append(fam)
f_list.close()
result = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/results/" + species + "_rates.txt", 'w+')
result.write("family" + '\t' +"outgroup" + '\t' + "geneA" + '\t' + "geneB" + '\t' + "total_sites" + '\t' + "unique_diffA" + '\t' + "unique_diffB" + '\t' + "pval" + '\n')
#go trhough mega's results:
for fam in l_families:
	print fam
	f_sum = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + species + "_rate/" + fam + "_summary.txt", 'r')
	for line in f_sum:
		line0 = line.strip('\n')
		line3 = line0.replace("ATCC 30", "ATCC_30")
		line2 = line3.replace("AZ8 4", "AZ8_4")
		line1 = line2.replace("V1 4", "V1_4")
		if "No. of Sites" in line1:
			s1 = line1.split("=")[1]
			tot = s1.split()[0]
		elif "Unique differences in Sequence A" in line1:
			s1 = line1.split("=")[1]
			diffA = s1.split()[0]
		elif "Unique differences in Sequence B" in line1:
			s1 = line1.split("=")[1]
			diffB = s1.split()[0]
		elif "Sequence A" in line1:
			s1 = line1.split("=")[1]
			geneA = s1.split()[0]
		elif "Sequence B" in line1:
			s1 = line1.split("=")[1]
			geneB = s1.split()[0]
		elif "Sequence C (outgroup)" in line1:
			s1 = line1.split("=")[1]
			out = s1.split()[0]
		elif "Chi Square P" in line1:
			s1 = line1.split("=")[1]
			p = s1.split()[0]
	f_sum.close()
	result.write(fam + '\t' + out + '\t' + geneA + '\t' + geneB + '\t' + tot + '\t' + diffA + '\t' + diffB + '\t' + p + '\n')


result.close()
print "Finished"



