#!/usr/bin/env python
# coding: utf-8

from Bio import SeqIO

project_folder = '/home/ismael/palaeoproteomics/briquettes/'
contams_db_fasta = project_folder + 'databases/contams.fasta'
db1_dairy_fasta = project_folder + 'databases/DB1_all_annotated_dairy_BLG_variants_ArchaecRAP3.2_nodups_norevs.fasta'
bovin_dairy_fasta = project_folder + 'databases/DB1_bovin_ArchaeocRAP3.2.fasta'


contams_db = SeqIO.to_dict(SeqIO.parse(contams_db_fasta, 'fasta'))
db1_dairy_db = SeqIO.to_dict(SeqIO.parse(db1_dairy_fasta, 'fasta'))


bovin_dairy = []
excluded = 0
skip = 0
for id, r in db1_dairy_db.items():
    if 'BOVIN' in id or id in contams_db:
        bovin_dairy.append(r)
    elif 'BOVIN' not in id and id not in contams_db:
        print(f'Excluded: {r.description}')
        excluded += 1

print(f'Kept {len(bovin_dairy)} sequences')
print(f'Excluded {excluded} sequences')
print(f'Skipped {skip} sequences')

SeqIO.write(bovin_dairy, bovin_dairy_fasta, "fasta")

