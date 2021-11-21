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




