#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,vmem=50gb,walltime=20:00:00
#PBS -M pjohri@indiana.edu
#PBS -m abe
#PBS -N genes_from_vcf
#PBS -j oe

cd /N/dc2/scratch/pjohri/Paramecium/CNSGenomes/programs

python2.6 extract_genes_from_vcf6.py tetraurelia Sample_A30
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_291
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_98
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_99
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_169
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_M02
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_298
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_B
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_47
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_116
python2.6 extract_genes_from_vcf6.py tetraurelia Sample_51

python2.6 extract_genes_from_vcf6.py biaurelia Sample_379
python2.6 extract_genes_from_vcf6.py biaurelia Sample_45
python2.6 extract_genes_from_vcf6.py biaurelia Sample_562alpha
python2.6 extract_genes_from_vcf6.py biaurelia Sample_76
python2.6 extract_genes_from_vcf6.py biaurelia Sample_44
python2.6 extract_genes_from_vcf6.py biaurelia Sample_31
python2.6 extract_genes_from_vcf6.py biaurelia Sample_256-UB2
python2.6 extract_genes_from_vcf6.py biaurelia Sample_258-UB4
python2.6 extract_genes_from_vcf6.py biaurelia Sample_7K
python2.6 extract_genes_from_vcf6.py biaurelia Sample_USBL-36I1

python2.6 extract_genes_from_vcf6.py sexaurelia Sample_265
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_134
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_131
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_129
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_130
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_Indo1-7I
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_128
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_Moz13BIII
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_126
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_137
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_132
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_133
python2.6 extract_genes_from_vcf6.py sexaurelia Sample_127

python2.6 extract_genes_from_vcf6.py caudatum Sample_C033
python2.6 extract_genes_from_vcf6.py caudatum Sample_C131
python2.6 extract_genes_from_vcf6.py caudatum Sample_C023
python2.6 extract_genes_from_vcf6.py caudatum Sample_16I
python2.6 extract_genes_from_vcf6.py caudatum Sample_C147
python2.6 extract_genes_from_vcf6.py caudatum Sample_C119
python2.6 extract_genes_from_vcf6.py caudatum Sample_C104
python2.6 extract_genes_from_vcf6.py caudatum Sample_C065
python2.6 extract_genes_from_vcf6.py caudatum Sample_C026
python2.6 extract_genes_from_vcf6.py caudatum Sample_C083

python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M04
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M05
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M09
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M08
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M03
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M13
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M12
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_M15
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_Canal-1I
python2.6 extract_genes_from_vcf6.py multimicronucleatum Sample_Peniche3I
















