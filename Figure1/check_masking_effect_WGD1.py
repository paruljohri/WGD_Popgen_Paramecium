#This is to get at masking effect by presence of multiple copies:

import sys
s_category ="lost in sister species"
#s_category = "all"
#s_category = "paralogs retained in sister species"
#s_category = "conserved duplicates and singlecopy"

print s_category

l_species = ["tetraurelia", "biaurelia", "sexaurelia", "caudatum"]
#get the characteristics:
print "readinng the characteristics of each species:"
d_state = {}
for species in l_species:
        print species
        f_char = open("/N/slate/pjohri/Paramecium/CNSGenomes/" + species + "/all_genes_filtered.char", 'r')
        for line in f_char:
                line1 = line.strip('\n')
                line2 = line1.split('\t')
                if line2[0] != "gene":
                        gene0 = line2[0].replace("EGNC", "P")
                        gene1 = gene0.replace("GNC", "P")
                        gene2 = gene1.replace("CAUDC", "CAUD")
			#if "cnv" in line2[1]:
                        d_state[gene2] = line2[1]
        f_char.close()

#read the orthoparalog file to get the set of genes that you want to survey:
f_ortho = open("/N/slate/pjohri/Paramecium/genomes/tet_bi_sex_caud_orthoparalogons_WGD1_truncated.txt", 'r')
l_copies = [1, 2]
l_aurelia = ["tet","bi", "sex"]
l_out = ["caud"] 
d_genes = {}
for aurelia in l_aurelia:
	d_genes[aurelia] = {}
	for copy in l_copies:
		d_genes[aurelia][copy] = []
for outgroup in l_out:
	d_genes[outgroup] = {}
	for aurelia in l_aurelia:
		d_genes[outgroup][aurelia] = {}
		for copy in l_copies:
			d_genes[outgroup][aurelia][copy] = []
#print d_genes

for line in f_ortho:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	tet_copy, bi_copy, sex_copy = 0,0,0
	if line2[0] != "PTET1":
		if line2[6] != ".":#outgroup is present
			print line2[0]
			##This is for putting the condition that the gene is lost in all other species:
			if s_category=="lost in sister species":
				if line2[2] =="." or line2[3]==".":#one of the bi pairs is lost
					if line2[4]=="." or line2[5]==".":#one of the sex pairs is lost
						tet_copy = line1.count("TET")
				if line2[0] =="." or line2[1]==".":#one of tets is lost
					if line2[4]=="." or line2[5]==".":#one of sex is lost
						bi_copy = line1.count("BI")
				if line2[0] =="." or line2[1]==".":#one of tets is lost
					if line2[2]=="." or line2[3]==".":#one of bi is lost
						sex_copy = line1.count("SEX")
			##This is for putting the condition that the gene is retained in all species:
			if s_category == "paralogs retained in sister species":
				if line2[2]!="." and line2[3]!="." and line2[4]!="." and line2[5]!=".":#both retained in bi and sex
					tet_copy = line1.count("TET")
				if line2[0]!="." and line2[1]!="." and line2[4]!="." and line2[5]!=".":#both retained in tet and sex
					bi_copy = line1.count("BI")
				if line2[0]!="." and line2[1]!="." and line2[2]!="." and line2[3]!=".":#both retained in tet and bi
					sex_copy = line1.count("SEX")
			##This is for simply all genes:
			if s_category == "all":
				tet_copy = line1.count("TET")
				bi_copy = line1.count("BI")
				sex_copy = line1.count("SEX")
			##This is for the case where duplicates are preserved in all, and single-copy are lost in all:
			if s_category== "conserved duplicates and singlecopy":
				if (line1.count("TET")==2 and line1.count("BI")==2 and line1.count("SEX")==2) or (line1.count("TET")==1 and line1.count("BI")==1 and line1.count("SEX")==1):
					tet_copy = line1.count("TET")
					bi_copy = line1.count("BI")
					sex_copy = line1.count("SEX")
			#print str(tet_copy) + '\t' + str(bi_copy) + '\t' + str(sex_copy)
			for x in line2:
				if "TET" in x:
					if d_state[x] != "NA":
						if tet_copy > 0:
								d_genes["tet"][tet_copy].append(x)
				elif "BI" in x:
					if d_state[x] != "NA":
						if bi_copy > 0:
							d_genes["bi"][bi_copy].append(x)
				elif "SEX" in x:
					if d_state[x] != "NA":
						if sex_copy > 0:
							d_genes["sex"][sex_copy].append(x)
				elif "CAUD" in x:
					if d_state[x] != "NA":
						if tet_copy > 0:
							d_genes["caud"]["tet"][tet_copy].append(x)
						if bi_copy > 0:
							d_genes["caud"]["bi"][bi_copy].append(x)
						if sex_copy > 0:
							d_genes["caud"]["sex"][sex_copy].append(x)

f_ortho.close()
print s_category
for aurelia in l_aurelia:
	for copy in l_copies:
		print "species and number of copies:"
		print aurelia + '\t' + str(copy)
		print "total number of genes evaluated:"
		print len(d_genes[aurelia][copy])
		s_ptc = 0
		for x in d_genes[aurelia][copy]:
			if d_state.get(x, "NA")!="NA" and d_state.get(x, "NA")!="intact":
				s_ptc += 1
		print "number of genes with ptcs:"
		print s_ptc
		print "caud" + '\t' + str(copy)
		print "total number of genes evaluated in caud:"
		print len(d_genes["caud"][aurelia][copy])
		s_ptc = 0
		for y in d_genes["caud"][aurelia][copy]:
			if d_state.get(y, "NA") != "NA" and d_state.get(y, "NA") != "intact":
				s_ptc += 1
		print "number of genes with ptcs in caud:"
		print s_ptc

print "Finished"







