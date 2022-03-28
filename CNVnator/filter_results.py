#This is to start filtering the results we get from CNVnator:
#The first filter is to throw out regions near scaffold ends

import sys

species = sys.argv[1]


#read sample names:
f_list = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + ".list", 'r')
l_samples = []
for line in f_list:
	line1 = line.strip('\n')
	l_samples.append(line1)
f_list.close()

#get scaffold ends for each sample separately (based on mpileup files):
print "getting scaffold lengths"
d_len = {}
d_begin = {}
for sample in l_samples:
	print sample
	d_len[sample] = {}
	d_begin[sample] = {}
	f_mp = open("/N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped_protect/" + species + "/MPILEUP3/" + sample + ".mpileup", 'r')
	for line in f_mp:
		line1 = line.strip('\n')
		line2 = line1.split('\t')
		scaffold = line2[0]
		if d_begin[sample].get(scaffold, "NA") == "NA":
			d_begin[sample][scaffold] = line2[1]
		d_len[sample][scaffold] = line2[1]
	f_mp.close()
#print d_len

#filter:
print "Going through CNV file"
result = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + species + ".filter1.cnv", 'w+')
result.write("Sample" + '\t' + "CNV_type" + '\t' + "coordinates" + '\t' + "CNV_size" + '\t' + "normalized_RD" + '\t' + "e-val1" + '\t' + "e-val2" + '\t' + "e-val3" + '\t' + "e-val4" + '\t' + "q0" + '\n')
for sample in l_samples:
	print sample
	f_cnv = open("/N/dc2/scratch/pjohri/Paramecium/CNVnator/" + species + "/" + sample + ".result", 'r')
	for line in f_cnv:
		line1 = line.strip('\n')
		line2 = line1.split('\t')
		scaffold = line2[1].split(":")[0]
		temp = line2[1].split(":")[1]
		start = temp.split("-")[0]
		end = temp.split("-")[1]
		if d_len[sample].get(scaffold, "NA") != "NA":
			if int(start)-int(d_begin[sample][scaffold]) > 200 and int(d_len[sample][scaffold])-int(end) > 200:
				result.write(sample + '\t' + line1 + '\n')
	f_cnv.close()

result.close()
print "Finished"








