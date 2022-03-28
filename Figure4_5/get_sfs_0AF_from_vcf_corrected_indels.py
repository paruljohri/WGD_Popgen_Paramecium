#This is to get SFS of indels particulalry from intronic and intergenic regions.
#For introns: we take out 3 bps both sides and use only small introns (<30 bp)
#For intergenic regions: use only sites 500 bp away from genes?

import sys

species = sys.argv[1]
inter_dist = 500

if species == "sexaurelia":
	l_samples = ["BAM_SORTED/Sample_126.sorted.bam", "BAM_SORTED/Sample_127.sorted.bam", "BAM_SORTED/Sample_128.sorted.bam", "BAM_SORTED/Sample_130.sorted.bam", "BAM_SORTED/Sample_131.sorted.bam", "BAM_SORTED/Sample_134.sorted.bam", "BAM_SORTED/Sample_137.sorted.bam", "BAM_SORTED/Sample_265.sorted.bam", "BAM_SORTED/Sample_Indo1-7I.sorted.bam", "BAM_SORTED/Sample_Moz13BIII.sorted.bam"]
elif species == "biaurelia":
	l_samples = ["BAM_SORTED/Sample_256-UB2.sorted.bam", "BAM_SORTED/Sample_31.sorted.bam", "BAM_SORTED/Sample_379.sorted.bam", "BAM_SORTED/Sample_44.sorted.bam", "BAM_SORTED/Sample_45.sorted.bam", "BAM_SORTED/Sample_562alpha.sorted.bam", "BAM_SORTED/Sample_76.sorted.bam", "BAM_SORTED/Sample_7K.sorted.bam", "BAM_SORTED/Sample_USBL-36I1.sorted.bam"]
elif species == "tetraurelia":
	l_samples = ["BAM_SORTED/Sample_116.sorted.bam","BAM_SORTED/Sample_47.sorted.bam", "BAM_SORTED/Sample_99.sorted.bam", "BAM_SORTED/Sample_A30.sorted.bam", "BAM_SORTED/Sample_B.sorted.bam"]

#Get the relevant sites from annotation files:
if species == "sexaurelia":
	f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes/sexaurelia/sexaurelia_AZ8-4_annotation_v1_intron_intergenic.gff", 'r')
elif species == "biaurelia":
	f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes/biaurelia/biaurelia_V1-4_annotation_v1_intron_intergenic.gff", 'r')

count_intron, count_inter = 0, 0
d_posn = {}
for line in f_ann:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[2] == "intron":
		start = int(line2[3])
		end = int(line2[4])
		if end - start + 1 <= 30:
			i = start + 3
			while i <= end-3:
				posn = line2[0] + '\t' + str(i)
				d_posn[posn] = "intron"
				count_intron = count_intron + 1
				i = i + 1
	elif line2[2] == "intergenic":
		start = int(line2[3])
		end = int(line2[4])
		if end - start + 1 > 2*inter_dist:
			if line2[8].count("GNG") > 1:#the intergenic is not at the end
				i = start + inter_dist
				while i <= end - inter_dist:
					posn = line2[0] + '\t' + str(i)
					d_posn[posn] = "intergenic"
					count_inter = count_inter + 1
					i = i + 1
f_ann.close()

print (count_intron)
print (count_inter)

#getting the SFS
print ("getting SFS")
f_all = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis/" + species + "3/" + species + "_allfiltQ_genes.recode.vcf.sites", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis/" + species + "3/" + species + "_SFS_0AF_corrected_indels.txt", 'w+')
d_col = {}
d_indel = {}
for line in f_all:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] == "CHROM" or line2[0] == "#CHROM" or "BAM" in line1:
		result.write("chrom" + '\t' + "posn" + '\t' + "num_chr_tot" + '\t' + "num_chr_minor_allele" + '\t' + "MAF"+ '\t' + "heterozygous" + '\t' + "site" + '\n')
		i = 0
		for x in line2:
			d_col[x] = i
			i = i + 1
		print (d_col)
	else:
		s_site = line2[0] + '\t' + line2[1]
		if d_posn.get(s_site, "NA") != "NA":
			#result.write(line2[0] + '\t' + line2[1] + '\t')
			s_het, s_tot, s_snp = 0, 0, 0
			l_gts = []
			for sample in l_samples:
				col = d_col[sample]
				gt = line2[col].split(":")[0]
				l_gts.append(gt)
				if gt == "0/0":
					s_tot = s_tot + 2
			if "1/1" not in l_gts and "0/1" not in l_gts and "1/0" not in l_gts:
				result.write(line2[0] + '\t' + line2[1] + '\t')
				result.write(str(s_tot) + '\t')
				if s_tot > 0:
					af = float(s_snp)/float(s_tot)
					if af <= 0.5:
						result.write(str(s_snp) + '\t' + str(af) + '\t')
					else:
						result.write(str(s_tot-s_snp) + '\t' + str(1.0 - af) + '\t')
				else:
					result.write("NA" + '\t' + "NA" + '\t')
				if s_het == 1:
					result.write("yes" + '\t' + d_posn[s_site] + '\n')
				else:
					result.write("no" + '\t' + d_posn[s_site] + '\n')

f_all.close()
result.close()
print ("done")

