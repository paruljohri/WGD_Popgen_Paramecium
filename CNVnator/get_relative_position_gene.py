#This is to get the relative position in the gene where the deletion occurred:
#The bins will be as follows: [0.0,0.1), [0.1,0.2) etc
import sys
species = sys.argv[1]
cutoff = int(sys.argv[2])
l_positions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] 
d_position = {}
for x in l_positions:
	d_position[x] = 0
s_tot = 0

#get duplicate/ singlecopy status:
f_char = open("/N/dc2/scratch/pjohri/Paramecium/genomes_protect/" + species + "/" + species + "_genes_CDS.char", 'r')
d_status, d_ext_status = {}, {}
for line in f_char:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	d_status[line2[0]] = line2[3]
	d_ext_status[line2[0]] = line2[4]
f_char.close()

f_pos = open("//N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + species + ".genes.position.cnv", 'r')
for line in f_pos:
	line1 = line.strip('\n')
	line2 = line1.split('\t')
	if line2[0] != "Sample":
		if int(line2[3]) <= cutoff:
			if line2[1] == "deletion":
				for x in line2[10:]:
					span = x.split(";")[2]
					##This is to exclude genes that are deleted entirely
					#if span != "0.0-1.0":
					##This is to only look at genes that are duplicates or singlecopy:
					gene = x.split(";")[0]
					if d_status[gene] == "duplicate" and d_ext_status[gene] == "retained":
						start = float(span.split("-")[0])
						end = float(span.split("-")[1])
						for posn in l_positions:
							if posn <= end and posn > start:
								d_position[posn] += 1
								s_tot += 1
f_pos.close()

print d_position
print s_tot
print "Finished"











