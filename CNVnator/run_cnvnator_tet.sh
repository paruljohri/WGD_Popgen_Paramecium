#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,vmem=100gb,walltime=11:00:00
#PBS -M pjohri@indiana.edu
#PBS -m abe
#PBS -N cnvnator_tet
#PBS -j oe

cd /N/dc2/scratch/pjohri/Paramecium_protect/CNVnator/tetraurelia
#For tetraurelia use bin size: 100 (check pipeline to see why)

declare -a TLIST
TLIST=("Sample_116" "Sample_169" "Sample_291" "Sample_298" "Sample_47" "Sample_51" "Sample_98" "Sample_99" "Sample_A30" "Sample_B" "Sample_M02")
for sample in "${TLIST[@]}";
do
	#1.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/Paramecium_protect/genomes/tetraurelia/tetraurelia_mac_51_edit.fasta -root ${sample}.root -unique -tree /N/dc2/scratch/pjohri/Paramecium_protect/kelley_data_mapped/tetraurelia/BAM_SORTED/${sample}.sorted.bam
	#2.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -genome /N/dc2/scratch/pjohri/Paramecium_protect/genomes/tetraurelia/tetraurelia_mac_51_edit.fasta -root ${sample}.root -his 100
	#3.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -stat 100
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -eval 100 > ${sample}.eval
	#4.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -partition 100
	#5.
	/N/dc2/scratch/pjohri/Tools/CNVnator_v0.3.3/src/./cnvnator -root ${sample}.root -call 100 > ${sample}.result
done







