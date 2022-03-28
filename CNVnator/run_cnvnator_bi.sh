#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,vmem=100gb,walltime=5:00:00
#PBS -M pjohri@indiana.edu
#PBS -m abe
#PBS -N cnvnator_bi
#PBS -j oe

cd /N/dc2/scratch/pjohri/Paramecium/CNVnator/biaurelia
#For biaurelia use bin size: 100 (check pipeline to see why)

declare -a TLIST
TLIST=("Sample_31" "Sample_45" "Sample_7K" "Sample_256-UB2" "Sample_379" "Sample_562alpha" "Sample_258-UB4" "Sample_44" "Sample_76" "Sample_USBL-36I1")
#TLIST=("Sample_1038")
for sample in "${TLIST[@]}";
do
	#1.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/assembly_protect/biaurelia/biaurelia_V1-4_assembly_v1.fa -root ${sample}.root -unique -tree /N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped_protect/biaurelia/BAM_SORTED/${sample}.sorted.bam
	#2.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/assembly_protect/biaurelia/biaurelia_V1-4_assembly_v1.fa -root ${sample}.root -his 100
	#3.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -stat 100
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -eval 100 > ${sample}.eval
	#4.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -partition 100
	#5.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -call 100 > ${sample}.result
done







