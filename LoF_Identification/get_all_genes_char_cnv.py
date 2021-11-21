#This is to assemble all genes in a species that might have either PTCs or do not have start codons or stop codons or have large frame-sifting indels:
#This program includes genes that have cnv deletions:

import sys

species = sys.argv[1]
subtype = sys.argv[2]
cutoff = sys.argv[3]
#large indel analysis:
f_ind = open("/N/slate/pjohri/Paramecium/CNSGenomes/large_indels_analysis/" + species + "_large_indels_CDS.char", 'r')
l_ind = []
d_state = {}
for line in f_ind:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "gene":
		if int(line2[2])%3 != 0:
			try:
				d_state[line2[0]].append("IND")
			except:
				d_state[line2[0]] = []
				d_state[line2[0]].append("IND")
f_ind.close()

#PTC analysis:
f_ptc = open("/N/slate/pjohri/Paramecium/CNSGenomes/PTC_analysis/" + species + "_PTC_genes_af.char", 'r')

for line in f_ptc:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "gene" and line2[9] != "NA":
		if float(line2[9]) < 1.0:
			try:
				d_state[line2[0]].append("PTC")
			except:
				d_state[line2[0]] = []
				d_state[line2[0]].append("PTC")
f_ptc.close()

#noSTART analysis:
f_start = open("/N/slate/pjohri/Paramecium/CNSGenomes/noSTART_analysis/" + species + "_noSTART_genes_af.char", 'r')

for line in f_start:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "gene" and line2[8] != "NA":
		if float(line2[8]) < 1.0:
			try:
				d_state[line2[0]].append("noSTART")
			except:
				d_state[line2[0]] = []
				d_state[line2[0]].append("noSTART")
f_start.close()

#frameshift analysis:
f_frame = open("/N/slate/pjohri/Paramecium/CNSGenomes/frameshift_analysis/" + species + "_frameshift_genes_af.char", 'r')

for line in f_frame:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "gene" and line2[9] != "NA":
		if float(line2[9]) < 1.0:
			try:
				d_state[line2[0]].append("frameshift")
			except:
				d_state[line2[0]] = []
				d_state[line2[0]].append("frameshift")
f_frame.close()

#CNV anaylsis; have to set a random cutoff. At this point it is either going to be 1000 bp or 2000 bp
f_cnv = open("/N/slate/pjohri/Paramecium/CNVnator/deletion_analysis/" + species + "_" + cutoff + "_genes.char", 'r')
for line in f_cnv:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0]!="gene":
		try:
			d_state[line2[0]].append("cnv_deletion")
		except:
			d_state[line2[0]] = []
			d_state[line2[0]].append("cnv_deletion")
f_cnv.close()

#get expression levels
d_FPKM, d_xp = {}, {}
if species != "multimicronucleatum":
	f_xp = open("/N/slate/pjohri/Paramecium/expression/" + species + "_genes_xp.tab", 'r')
	for line in f_xp:
		line1 = line.strip('\n')
		line2 = line1.split('\t')
		if species == "caudatum":
			gene = line2[0].replace("CAUDG", "CAUDC")
			d_FPKM[gene] = "NA"
			d_xp[gene] = line2[1]
		else:
			gene = line2[0].replace("GNG", "GNC")
			d_FPKM[gene] = line2[1]
			d_xp[gene] = line2[2]
	f_xp.close()

#get piNpiS
f_char = open("/N/slate/pjohri/Paramecium/piNpiS/cutoff_thetaS_5/" + species + ".charac", 'r')
d_NS = {}
for line in f_char:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[0] #.replace("EGNC", "P")
	#gene = gene0.replace("GNC", "P")
	d_NS[gene] = line2[8]
f_char.close()

#get blosum scores:
f_bl = open("/N/slate/pjohri/Paramecium/GFE_analysis/" + species + subtype + "/" + species + "_genes_SNPs_blosum.txt",'r')
d_bl62, d_bl80 = {}, {}
for line in f_bl:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "gene":
		if int(line2[6]) >= 5: #has 5 or more syn SNPs
			d_bl62[line2[0]] = line2[7]
			d_bl80[line2[0]] = line2[8]
f_bl.close()

#make a table with all genes:
f_all = open("/N/slate/pjohri/Paramecium/genomes/" + species + "/" + species + "_genes_CDS.char", 'r')
result = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_cnv_" + cutoff + ".char", 'w+') 

for line in f_all:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[0]
	if line2[0] == "gene":
		result.write("gene" + '\t' + "state" + '\t' + "length	GCcontent	status	ext_status	FPKM	xp	piNpiS	blosum62	blosum80" + '\n')
	else:
		result.write(gene + '\t')
		try:
			result.write(';'.join(d_state[gene]) + '\t')
		except:
			result.write("NA" + '\t')
		result.write('\t'.join(line2[1:]) + '\t' + d_FPKM.get(gene, "NA") + '\t' + d_xp.get(gene, "NA") + '\t' + d_NS.get(gene, "NA") + '\t' + d_bl62.get(gene, "NA") + '\t' + d_bl80.get(gene,"NA") + '\n')
result.close()
f_all.close()
print ("Finished")
















