#This is to create fasta files for different species with caudatum as the outgroup (always kept last)
#place the nonfunctional one first
#currently only doing this for tetraurelia:

import sys
import os

def read_fasta(file):
        sequence = ""
        data = {}
        for line in file:

                if line[0] != '>':
                        line0 = line.strip('\n')
                        #linem = linew.strip('\r')
                        line1 = line0.strip('\r')
                        sequence = sequence + line1

                else:

                        if sequence != "":
                                data[name[1:]] = sequence
                                sequence = ""
                        name = line.strip('\n').split()[0]

        data[name[1:]] = sequence
        return data

#read hte fasta files for their gene or protein sequences
l_species = ["pprim", "pbi", "ptet", "ppent", "psex", "psept", "poct", "pnov", "pdec", "pdodec", "ptre", "pquad", "pson", "pjen", "pcaud", "pmultimic"]
d_fasta = {}
for species in l_species:  
	f_cds = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/genomes_new_ann/" + species + "/" + species + "_genes_CDS_prot.fasta", 'r')
	d_fasta[species] = read_fasta(f_cds)
	f_cds.close()

#get the list of nonfunc genes from tet
#f_ptc = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/CNSGenomes_new_annotation/tetraurelia/all_genes.char", 'r')
#d_state = {}
#for line in f_ptc:
#	line1 = line.strip('\n')
#	line2 = line1.split('\t')
#	if line2[0]!="gene":
#		d_state[line2[0]] = line2[1]
#f_ptc.close()

#exclude these potentially ambiguous gene families:
#f_doubles = open("/N/dc2/scratch/pjohri/Paramecium_all_sp/calling_orthologs/all_aurelias_doubles.flipped.outgroup", 'r')
#d_exclude = {}
#for line in f_doubles:
#        line1 = line.strip('\n')
#        line2 = line1.split('\t')
#        l_fam = line2[0].split(";")
#        for x in l_fam:
#                d_exclude[x] = "T"
#f_doubles.close()

#get the ortholog file and write the sequences
f_ortho = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/calling_orthologs/all_aurelias.flipped", 'r')
#l_species = ["pprim", "pbi", "ptet", "ppent", "psex", "psept", "poct", "pnov", "pdec", "pdodec", "ptre", "pquad", "pson", "pjen", "pcaud", "pmultimic"]
print "removing and creating new directories"
l_aurelias = ["pprim", "pbi", "ptet", "ppent", "psex", "psept", "poct", "pnov", "pdec", "pdodec", "ptre", "pquad", "pson", "pjen"]
for sp in l_aurelias:
	print sp
	os.system("rm -r /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + sp)
	os.system("mkdir /N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + sp)
l_out = ["pcaud", "pmultimic"]
d_col = {}
print "reading through ortholog file"
for line in f_ortho:
        line1 = line.strip('\n')
        line2 = line1.split('\t')
        if line2[0] == "WGD":
                i = 0
                for x in line2:
                        #if "caud" in x:
                        #        d_col["pcaud"] = i
                        #elif "multi" in x:
                        #        d_col["pmultimic"] = i
                        #else:
                        d_col[x] = i
                        i = i + 1
        else:
                if line2[d_col["allScored"]] == "TRUE":#line is good
                        #if d_exclude.get(line2[0], "NA") == "NA":#this line in not ambiguous:
			if "CAUD" in line2[d_col["pcaud"]] or "MMN" in line2[d_col["pmultimic"]]:
				fam = line2[0]
				for taxa in l_aurelias:
					pair  = line2[d_col[taxa]]
					if "," in pair:
						dup1_1 = pair.split(",")[0].replace(".P", ".C")
						dup2_1 = pair.split(",")[1].replace(".P", ".C")
						dup1 = dup1_1.replace("PRIMP", "PRIMC")
						dup2 = dup2_1.replace("PRIMP", "PRIMC")
						if dup1!="." and dup2!="." and dup1!="NA" and dup2!="NA":
							print fam
							result = open("/N/dc2/scratch/pjohri/Paramecium_all_sp_protect/tajima_rate_test/" + taxa + "/" + fam + ".fasta", 'w+')
							result.write(">" + dup1 + '\n')
							result.write(d_fasta[taxa][dup1] + '\n')
							result.write(">" + dup2 + '\n')
							result.write(d_fasta[taxa][dup2] + '\n')
							if "MMN" in line2[d_col["pmultimic"]]:
								out1 = line2[d_col["pmultimic"]].split("_")[0]
								out2 = out1.replace(";", "")
								out = out2.replace("MMNT", "MMNC")
								result.write(">" + out + '\n')
								result.write(d_fasta["pmultimic"][out] + '\n')
							else:
								out1 = line2[d_col["pcaud"]].split("_")[0]
								out2 = out1.replace(";", "")
								out = out2.replace("CAUDP", "CAUDC")
								result.write(">" + out + '\n')
								result.write(d_fasta["pcaud"][out] + '\n')
							#result.write(">" + dup1 + '\n')
							#result.write(d_fasta[taxa][dup1] + '\n')
							#result.write(">" + dup2 + '\n')
							#result.write(d_fasta[taxa][dup2] + '\n')
							result.close()
	

f_ortho.close()

print "Finished"





