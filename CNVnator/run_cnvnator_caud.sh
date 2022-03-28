#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,vmem=100gb,walltime=11:00:00
#PBS -M pjohri@indiana.edu
#PBS -m abe
#PBS -N cnvnator_caud
#PBS -j oe

cd /N/dc2/scratch/pjohri/Paramecium/CNVnator/caudatum
#For caudatum use bin size: 400 (check pipeline to see why)

declare -a TLIST
TLIST=("Sample_C033" "Sample_C131" "Sample_C023" "Sample_C147" "Sample_C119" "Sample_C104" "Sample_C065" "Sample_C083")
for sample in "${TLIST[@]}";
do
	#1.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/Paramecium/genomes_protect/caudatum/caudatum_43c3d_assembly_v1.fasta -root ${sample}.root -unique -tree /N/dc2/scratch/pjohri/Paramecium/kelley_data_mapped_protect/caudatum/BAM_SORTED/${sample}.sorted.bam
	#2.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/Paramecium/genomes_protect/caudatum/caudatum_43c3d_assembly_v1.fasta -root ${sample}.root -his 400
	#3.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -stat 400
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -eval 400 > ${sample}.eval
	#4.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -partition 400
	#5.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -call 400 > ${sample}.result
done







