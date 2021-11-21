# This is the pipeline used to get genes with PTCs
#directly gets genes and indels from the vcf files:

Step1:
>> qsub run_extract_genes_from_vcf.pbs # output in my_consensus_CDS_VCF
#which runs:
>> extract_genes_from_vcf6.py //output: CNSGenomes/my_consensus_CDS_VCF/ + sample + _homo.fasta

Step2:
>> python2.6 translate_my_CDS.py
#output: Paramecium/CNSGenomes/my_consensus_prot_VCF
#output: Paramecium/CNSGenomes/my_consensus_noSTART_VCF

Step3:
>> python2.6 count_PTCs.py
#output: Paramecium/CNSGenomes/my_consensus_PTC_VCF
#output: Paramecium/CNSGenomes/my_consensus_noSTOP_VCF
#output: Paramecium/CNSGenomes/my_consensus_NK_VCF
#NK list (which is basically genes that are missing 1/3rd of their sequence)

Step4:
>> python2.6 count_noSTART.py
#output: Paramecium/CNSGenomes/my_consensus_noSTART_VCF

Step5:
>> python2.6 get_large_indels_CDS.py tetraurelia ""
>> python2.6 get_large_indels_CDS.py biaurelia ""
>> python2.6 get_large_indels_CDS.py sexaurelia ""
>> python2.6 get_large_indels_CDS.py caudatum _subset
#output: Paramecium/CNSGenomes_protect/large_indels_VCF/ + species + _large_indels_CDS.vcf

Step6:
#get genes that have a single 1 bp or 2 bp indel- there will have to be a frameshift
>> python get_single_frameshift_genes.py tetraurelia 3
>> python get_single_frameshift_genes.py biaurelia 3
>> python get_single_frameshift_genes.py sexaurelia 3
>> python get_single_frameshift_genes.py caudatum 3_subset
#lists the genes that have an odd number of indels in my_consensus_frameshift. So this list includes genes that have PTC and do not.
#output: Paramecium/CNSGenomes_protect/my_consensus_frameshift/${species}_frameshift_posn.txt
#output: Paramecium/CNSGenomes_protect/my_consensus_frameshift/${strain}.list


#get genes that are mistranslated as a result of indels:
#python

Step7:
#get the genes with deletions, CNVnator:
#This is in the folder CNVnator

Step8: get characteristics of genes that have Lof variants:
>> get_PTC_charc.py
#output: Paramecium/CNSGenomes/PTC_analysis/${species}_PTC_genes.char
>> get_noSTART_charc.py
#output: Paramecium/CNSGenomes/noSTART_analysis/${species}_noSTART_genes.char
>> get_large_indels_charac.py
#output: Paramecium/CNSGenomes/large_indels_analysis/${species}_large_indels_CDS.char
>> get_noSTOP_charc.py
#output: Paramecium/CNSGenomes/noSTOP_analysis/${species}_noSTOP_genes.char
>> get_frameshift_charc.py
#output: Paramecium/CNSGenomes_protect/frameshift_analysis/${species}_frameshift_genes.char
>>CNVnator/get_cnv_charac.py. #This is the CNVnator folder.

Step9: calculate allele frequency of the LoF haplotype accounting for samples with no coverage for some genes
>> python2.6 get_allele_freq_PTCs.py 
#output: Paramecium/CNSGenomes/PTC_analysis/${species}_PTC_genes_af.char
#output: Paramecium/CNSGenomes/noSTART_analysis/" + species + "_noSTART_genes_af.char
#output: Paramecium/CNSGenomes/noSTOP_analysis/" + species + "_noSTOP_genes_af.char
#output: Paramecium/CNSGenomes/frameshift_analysis/" + species + "_frameshift_genes_af.char
#output: Paramecium/CNSGenomes/intact_analysis/" + species + "_intact_genes_af.char

Step10: Get the list of all genes in every species and the corresponding LoF status
>> get_all_genes_char.py caudatum 3_subset
#output: Paramecium/CNSGenomes/${species}/all_genes.char
>> python get_all_genes_char_cnv.py caudatum 3_subset 2000
#includes CNV genes with large deletions
#output: Paramecium/CNSGenomes/${species}/all_genes_cnv_2000.char

Step11: to test 2 things- if the coverage of such genes is higher or if they are over-represented in strin-specific dulications:
>> python check_coverage_nonfunc_genes.py caudatum 3_subset
#output: Paramecium/CNSGenomes/${species}/all_genes_depth.char

Step12:This is to filter the all_genes_char file to exclude genes
#1. with too low or too high coverage
#2. present as tandem duplicates
#3. present as duplicates in CNVnator
>> python get_all_genes_char_filtered.py caudatum
#output: Paramecium/CNSGenomes/${species}/all_genes_filtered.char
>> python get_all_genes_char_filtered.py caudatum #run the same script after internally changing the input file to _cnv_2000
#output: Paramecium/CNSGenomes/${species}/all_genes_cnv_2000_filtered.char

Step13: to exclude genes that have noSTOP polymorphism
>> python get_all_genes_char_filtered_exclude_noSTOP.py caudatum 
#output: Paramecium/CNSGenomes/${species}/all_genes_filtered_exclude_noSTOP.char

Step14: Aligh orthologs and paralogs
>> python get_ortho_para_states_filtered.py
#output: tet_bi_sex_caud_filtered.state


