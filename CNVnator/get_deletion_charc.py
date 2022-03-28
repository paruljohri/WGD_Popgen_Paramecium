#This is to get properties of genes with PTCs.

import sys

species = sys.argv[1]
cutoff = sys.argv[2]
#read the samples
#f_list = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/" + species + ".list", 'r')
#l_samples = []
#for line in f_list:
#        line1 = line.strip('\n')
#        l_samples.append(line1)
#f_list.close()


#d_indv, d_num = {}, {}
#for sample in l_samples:
#	f_cnv = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_PTC_VCF/" + sample + "_homo.fasta", 'r')
#	for line in f_ptc:
#		line1 = line.strip('\n')
#		if line1[0] == ">":
#			gene = line1[1:]
#			try:
#				d_indv[gene].append(sample)
#				d_num[gene] = d_num[gene] + 1
#			except:
#				d_indv[gene] = []
#				d_indv[gene].append(sample)
#				d_num[gene] = 1
#	f_ptc.close()
#get list of genes that have cnvs
f_cnv = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/deletion_analysis/" + species + "_" +  cutoff + ".deletions", 'r')
d_samples = {}
l_genes = []
d_num = {}
for line in f_cnv:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0]!="gene":
		l_genes.append(line2[0])
		d_samples[line2[0]] = line2[1]
		d_num[line2[0]] = line2[1].count("Sample")
f_cnv.close()

f_char = open("/N/dc2/scratch/pjohri/Paramecium/piNpiS_protect/cutoff_thetaS_5/" + species + ".charac", 'r')
d_NS = {}
for line in f_char:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        gene = line2[0] #.replace("EGNC", "P")
        #gene = gene0.replace("GNC", "P")
        d_NS[gene] = line2[8]
f_char.close()
print d_NS


#get expression levels
d_FPKM, d_xp = {}, {}
if species != "multimicronucleatum":
        f_xp = open("/N/dc2/scratch/pjohri/Paramecium/expression/" + species + "_genes_xp.tab", 'r')
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


f_char = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/" + species + "/" + species + "_genes_CDS.char", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/deletion_analysis/" + species + "_" + cutoff + "_genes.char", 'w+')

d_char = {}
for line in f_char:
	#print line
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[0]
	if gene == "gene":
		result.write(line1 + '\t' +"piNpiS" + '\t' + "xp" + '\t' +  "num_indv" + '\t' + "samples" + '\n') 
	else:
		d_char[gene] = line1
f_char.close()

for gene in l_genes:
	print gene
	#print d_NS[gene]
	result.write(d_char[gene] + '\t' + d_NS.get(gene, "NA") + '\t' + d_xp.get(gene, "NA") + '\t' + str(d_num[gene]) + '\t' + d_samples[gene] + '\n')
result.close()
print "Finished"





















