# reversing all the letters of a pattern/string

# def Reverse(Pattern):
#     rev = ""
#     for char in Pattern:
#         rev = char + rev   # add each character to the front
#     return rev

def Reverse(Pattern):
    return Pattern[::-1]

sample_input_r = 'AAAACCCGGT'
print(Reverse(sample_input_r))

# complement of dna nucleotide
# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement)

def Complement(Pattern):
    complement_nucleotide = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}    # mapping each nucleotide to its complementary base
    comp = ""
    for char in Pattern:
        comp += complement_nucleotide[char]     # add complementary nucleotide to the result string
    return comp

sample_input_c = 'AAAACCCGGT'
print(Complement(sample_input_c))


# here we will utilize the both function 'Complement' & 'Reverse' and create a new function 'ReverseComplement'
# the function will complement & reverse the input pattern

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

sample_input = 'AAAACCCGGT'
print(ReverseComplement(sample_input))
