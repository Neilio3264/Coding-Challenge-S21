from Bio import SeqIO

for seq_record in SeqIO.parse("./Genome.gb", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    print(seq_record.features)