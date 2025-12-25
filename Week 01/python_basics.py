# variables and data types

dna_sequence = "ATGCGATACGCTTGA"      # string
sequence_length = len(dna_sequence)   # integer
threshold = 0.5                       # float
is_valid_dna = True                   # boolean

print("DNA sequence:", dna_sequence)
print("Length:", sequence_length)

# lists & indexing
# A - Adenine, T - Thymine, C - Cytosine, G - Guanine

nucleotides = ["A", "T", "C", "G"]    # DNA base pairs list
print("First nucleotide:", dna_sequence[0])
print("Last nucleotide:", dna_sequence[-1])

# dictionaries - key value pairs
# used for mapping

nucleotide_counts = {"A": 0, "T": 0, "C": 0, "G": 0}

for nucleotide in dna_sequence:
    if nucleotide in nucleotide_counts:
        nucleotide_counts[nucleotide] += 1

print("Nucleotide counts:", nucleotide_counts)
