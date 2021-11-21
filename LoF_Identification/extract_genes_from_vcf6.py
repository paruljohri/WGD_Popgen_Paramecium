# This is to directly extract CDSs from vcf files; this is only for genes that do not have multiple heterozygous indels.
#version 5, this uses _allfilt.vcf file, which has less filtering steps before it.
#adding the feature that if there is an indel that goes beyond the gene's end, stop including the additional sequence 
import sys
species = sys.argv[1]
sample = sys.argv[2]

def get_ambiguity_code(s_ntds):
        s = ""
        #s_ntds = s1 + ',' + s2
        if "A" in s_ntds and "G" in s_ntds and "C" in s_ntds and "T" in s_ntds:
                s = "N"
        elif "A" in s_ntds and "G" in s_ntds and "C" in s_ntds:
                s = "V"
        elif "A" in s_ntds and "T" in s_ntds and "C" in s_ntds:
                s = "H"
        elif "A" in s_ntds and "G" in s_ntds and "T" in s_ntds:
                s = "D"
        elif "T" in s_ntds and "G" in s_ntds and "C" in s_ntds:
                s = "B"
        elif "A" in s_ntds and "C" in s_ntds:
                s = "M"
        elif "A" in s_ntds and "G" in s_ntds:
                s = "R"
        elif "A" in s_ntds and "T" in s_ntds:
                s = "W"
        elif "C" in s_ntds and "G" in s_ntds:
                s = "S"
        elif "C" in s_ntds and "T" in s_ntds:
                s = "Y"
        elif "T" in s_ntds and "G" in s_ntds:
                s = "K"
        elif "A" in s_ntds:
                s = "A"
        elif "T" in s_ntds:
                s = "T"
        elif "C" in s_ntds:
                s = "C"
        elif "G" in s_ntds:
                s = "G"
        else:
                print "Something is weird about the reference or alternate allele"
                print site
                #print s2
                #print line2[1]
        return s

def reverse(sequence):
        Comp_seq = []
        for x in sequence:
                if x not in "AaTtGgCcMmRrWwSsYyKkVvHhDdBbNn":
                        print "Failed to recognize the ambiguity code for DNA!"
                        print x
                if x == "A" or x == 'a':
                        y = "T"
                if x == "T" or x == 't':
                        y = "A"
                if x == "G" or x == 'g':
                        y = "C"
                if x == "C" or x == 'c':
                        y = "G"
                if x == "M" or x == 'm': # A / C
                        y = "K"
                if x == "R" or x == 'r': #A/G
                        y = "Y"
                if x == "W" or x == 'w':  #A/T
                        y = "W"
                if x == "S" or x == 's':  #C/G
                        y = "S"
                if x == "Y" or x == 'y':  #C/T
                        y = "R"
                if x == "K" or x == 'k':  #G/T
                        y = "M"
                if x == "V" or x == 'v':  #A/C/G
                        y = "B"
                if x == "H" or x == 'h':  #A/C/T
                        y = "D"
                if x == "D" or x == 'd':  #A/G/T
                        y = "H"
                if x == "B" or x == 'b':  #C/G/T
                        y = "V"
                if x == "N" or x == 'n':
                        y = "N"
                if x.istitle():
                        Comp_seq.append(y)
                else:
                        Comp_seq.append(y.lower())
        Comp_seq.reverse()
        Comp_sequence = "".join(Comp_seq)
        return Comp_sequence


print "going through indel summary file to get homozygous genes"
#get the list of genes that have single heterozygous indel (l_sin_het) or any number of heterozygous indels (l_hetero)
f_sum = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis/" + species + "3/" + species + "_indelsfiltQfinal_genes.summary", 'r')
l_hetero, l_sin_het = [], []
d_het = {}
for line in f_sum:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	gene = line2[7]
	if ',' in line2[3]:
		if gene not in l_hetero:
			l_hetero.append(gene)
	if line2[0] != "scaffold":
		#for y in line2[4].split('_'):
			#y = x.split('_')
		if "0/1" in line2[4]:
			try:
				d_het[gene] = d_het[gene] + 1
			except:
				d_het[gene] = 0
				d_het[gene] = d_het[gene] + 1
f_sum.close()

for gene in d_het.keys():
	if int(d_het[gene]) > 1: #if any indel is heterozygous
		l_hetero.append(gene)
	if int(d_het[gene]) == 1:
		l_sin_het.append(gene)

print l_sin_het			
#get gene cooredinates:

#read the annotation file:
f_list = open("/N/dc2/scratch/pjohri/Paramecium/genomes/annotation.list", 'r')
for line in f_list:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if species == line2[0]:
		f_ann = open("/N/dc2/scratch/pjohri/Paramecium/genomes/" + species + "/" + line2[1], 'r')
f_list.close()

print "reading the annotation file to read the coordinates of the genes"
#read the annotation file:
d_genes, d_strand, d_end, d_start = {}, {}, {}, {}
l_genes, l_start_sites = [], []
gene0 = ""
for line in f_ann:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[2] == "CDS":
		gene = line2[8].split(':')[0][3:]
		l_CDS = []
		if gene not in l_hetero:
			start = int(line2[3])
			end = int(line2[4])
			d_strand[gene] = line2[6]
			d_end[gene] = line2[0] + '_' + line2[4]
			if gene != gene0:
				d_start[line2[0] + '_' + line2[3]] = gene #this will remember the start positions of all genes
			while start <= end:
				site = line2[0] + '_' + str(start)
				l_CDS.append(site)
				start = start + 1
			try:
				d_genes[gene].append(l_CDS)
			except:
				d_genes[gene] = []
				l_genes.append(gene)
				d_genes[gene].append(l_CDS)
				
		gene0 = gene[:]
f_ann.close()
#print d_genes
#get all snps:
print "storing snp sites"
f_snp = open("/N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped/" + species + "/POPN3/" + species + "_snpsfiltQfinal.vcf", 'r')
d_snp = {}
l_snp = []
for line in f_snp:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	#identify column number of the sample:
        if line2[0] == "#CHROM":
                i = 0
                for x in line2:
                        if sample in x:
                                col_num = i
                        i = i + 1
	else:
		if line[0] != "#":
			site = line2[0] + '_' + line2[1]
			l_snp.append(site)
			#allele = line2[4]
			geno = line2[col_num].split(':')[0]
			if geno == "0/0":
				allele = line2[3]
			elif geno == "1/1":
				allele = get_ambiguity_code(line2[4])
			elif geno == "0/1" or geno == "1/0":
				allele = get_ambiguity_code(line2[3] + line2[4])
			elif geno == "./.":
				allele = "N"
			else:
				print "Error: There is no genotype."
			d_snp[site] = allele
f_snp.close()

#read all indels
print "storing indel sites"
f_ind = open("/N/dc2/scratch/pjohri/Paramecium/VCF_analysis/" + species + "3/" + species + "_indelsfiltQfinal_genes.vcf", 'r')
d_ind, d_ind_len, d_type, d_ref_len = {}, {}, {}, {}
l_ind = []
for line in f_ind:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        #identify column number of the sample:
        if line2[0] == "CHROM":
                i = 0
                for x in line2:
                        if sample in x:
                                col_num = i
                        i = i + 1
        else:
                if line2.pop() != "NA":
                        site = line2[0] + '_' + line2[1]
			#l_ind.append(site)
                        geno = line2[col_num].split(':')[0]
			#geno = line2[col_num].split(':')[0]
                        #if geno == "0/0":
                        #        allele = line2[3]
			#	length = len(line2[3])
                        if geno == "1/1":
                                allele = line2[4]
				length = len(line2[3])
                        elif geno == "0/1" or geno == "1/0":
                                allele = line2[3] + '_' + line2[4]
				length = len(line2[3])
                        elif geno == "./.":
                                allele = "N"
				length = "NA"
                        elif geno != "0/0":
                                print "Error: There is no genotype."
			if geno != "0/0":
				l_ind.append(site)
                        	d_ind[site] = allele
				d_ind_len[site] = length
				d_ref_len[site] = len(line2[3])
				if len(line2[3]) > len(line2[4]):
					d_type[site] = "deletion"
				else:
					d_type[site] = "insertion"
                        
f_ind.close()

#get all bases:
print "storing all sites"
f_all = open("/N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped/" + species + "/POPN3/" + species + "_allfilt.vcf", 'r')
d_all = {}
for line in f_all:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        #identify column number of the sample:
        if line2[0] == "#CHROM":
                i = 0
                for x in line2:
                        if sample in x:
                                col_num = i
                        i = i + 1
        else:
                if line[0] != "#" and "INDEL" not in line2[7]:
                        site = line2[0] + '_' + line2[1]
                        #l_snp.append(site)
                        #allele = line2[4]
                        GT = line2[col_num].split(':')[0]
			DP = line2[col_num].split(':')[2]
			GQ = line2[col_num].split(':')[3]
			if int(DP) >= 4 and int(GQ) >= 30:
				allele = line2[3]
			else:
				allele = "N"
                        d_all[site] = allele
f_all.close()




#read the file with all bases:
#f_all = open("/N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped/" + species + "/POPN3/" + species + "_allfiltQ.recode.vcf", 'r')
result = open("/N/dc2/scratch/pjohri/Paramecium/CNSGenomes/my_consensus_CDS_VCF/" + sample + "_homo.fasta", 'w+')
print "going through gene sequences"
#dealing first with only homozygous indel cases:
d_sequences = {}
l_exclude = []
for gene in l_genes:
	if gene not in l_sin_het and gene not in l_exclude:
		print gene
		#result.write(">" + gene + '\n')
		seq = ""
		for CDS in d_genes[gene]:
			mark = 0
			CDS_len = len(CDS)
			CDS_end = CDS[CDS_len-1].split('_')[2]
			print CDS_end
			for site in CDS:
				if mark == 0:
					try:
						if d_ind[site] != "N": #it is an indel with some clear genotype (not ./.)
							coord = site.split("_")[2]
							
							if (int(coord) + int(d_ref_len[site])) <= int(CDS_end): 
								seq = seq + d_ind[site]
								mark = int(d_ind_len[site])
							elif d_type[site] == "insertion":
								try:
									seq = seq + d_all[site]
								except:
									seq = seq + "N"
							elif d_type[site] == "deletion":
								l_exclude.append(gene)
								break
							if "_" in d_ind[site]:
                                                        	print d_ind[site]
                                                        	print site
							#l_ind.remove(site)
						else:  #there is probably no indel at that site. We do not know what is at the site.
							try:   #check if there is a SNP
								seq = seq + d_snp[site]
								if "_" in d_snp[site]:
                                                        		print d_snp[site]
                                                        		print site
							except:  #it's either the ref allel or not known
								try:
									seq = seq + d_all[site]
									if "_" in d_all[site]:
										print d_all[site]
										print site
								except:
									seq = seq + "N"
					except:  #there is no indel detected at that site
						try:
							#elif site in l_snp:
							seq = seq + d_snp[site]
							if "_" in d_snp[site]:
                                                        	print d_snp[site]
                                        	        	print site
							#l_snp.remove(site)
						except:
							#else:   #now the site is neither an indel or snp, so it's either not known or is the refernces allele
							try:
								seq = seq + d_all[site]
								if "_" in d_all[site]:
									print d_all[site]
									print site
							except:
								seq = seq + "N"
				if mark != 0:  #This is so that we don't read the sites just after an indel
					mark = mark - 1
		if d_strand[gene] == "+":
			d_sequences[gene] = seq
			#result.write(seq + '\n')
			#print seq
		else:
			d_sequences[gene] = reverse(seq)
			#result.write(reverse(seq) + '\n')
			#print reverse(seq)
		#if gene == "PTETEGNC13841":
		#	print seq

for gene in l_genes:
	if gene not in l_sin_het and gene not in l_exclude:
		result.write(">" + gene + '\n' + d_sequences[gene] + '\n')
result.close()
print "Finished"


					
					
					





















