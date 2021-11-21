# This is the pipeline used to get genes with PTCs
#directly gets genes and indels from the vcf files:

qsub run_extract_genes_from_vcf.pbs # output in my_consensus_CDS_VCF

python2.6 translate_my_CDS.py

python2.6 count_PTCs.py
>>NK list (which is basically genes that are missing 1/3rd of their sequence)

python2.6 count_noSTART.py

python2.6 get_large_indels_CDS.py tetraurelia ""
python2.6 get_large_indels_CDS.py caudatum _subset

#get genes that have a single 1 bp or 2 bp indel- there will have to be a frameshift
python get_single_frameshift_genes.py tetraurelia
#>>lists the genes that have an odd number of indels in my_consensus_frameshift. So this list includes genes that have PTC and do not.

#get genes that are mistranslated as a result of indels:
python

#get the genes with deletions, CNVnator:
#This is in the folder CNVnator


get_PTC_charc.py

get_noSTART_charc.py

get_large_indels_props.py

get_noSTOP_charc.py

get_frameshift_charc.py

#get_cnv_charac.py. This is the CNVnator folder.

python2.6 get_allele_freq_PTCs.py

get_all_genes_char.py caudatum 3_subset

python get_all_genes_char_cnv.py caudatum 3_subset 2000

python check_coverage_nonfunc_genes.py caudatum 3_subset

python get_all_genes_char_filtered.py caudatum
python get_all_genes_char_filtered.py caudatum #do the same thing after changing the script to _cnv

python get_all_genes_char_filtered_exclude_noSTOP.py caudatum #to exclude genes that have noSTOP polymorphism

python get_all_genes_samples.py caudatum 3_subset

get_ortho_para_states.py

#add the information of single genes that are only present in that particular species. Absent everywhere else.

cd VCF_analysis/programs/
python get_sfs_from_vcf_corrected.py biaurelia




