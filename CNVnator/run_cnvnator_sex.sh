#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,vmem=100gb,walltime=11:00:00
#PBS -M pjohri@indiana.edu
#PBS -m abe
#PBS -N cnvnator_sex
#PBS -j oe

cd /N/dc2/scratch/pjohri/Paramecium_protect/CNVnator/sexaurelia
#For sexaurelia use bin size: 100 (check pipeline to see why)

declare -a TLIST
TLIST=("Sample_126" "Sample_129" "Sample_132" "Sample_137" "Sample_Moz13BIII" "Sample_127" "Sample_130" "Sample_133" "Sample_265" "Sample_128" "Sample_131" "Sample_134" "Sample_Indo1-7I")
for sample in "${TLIST[@]}";
do
	#1.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/assembly_protect/sexaurelia/sexaurelia_AZ8-4_assembly_v1.fasta -root ${sample}.root -unique -tree /N/dc2/scratch/pjohri/Paramecium_protect/kelley_data_mapped/sexaurelia/BAM_SORTED/${sample}.sorted.bam
	#2.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/assembly_protect/sexaurelia/sexaurelia_AZ8-4_assembly_v1.fasta -root ${sample}.root -his 100
	#3.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -stat 100
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -eval 100 > ${sample}.eval
	#4.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -partition 100
	#5.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -call 100 > ${sample}.result
	
done







