# function to count how many times a pattern occurs in a given text
def PatternCount(Text, Pattern):
    count = 0   # initialize count of pattern occurrences
    for i in range(len(Text) - len(Pattern) + 1): 
        if Text[i:i+len(Pattern)] == Pattern:  # check if substring matches the pattern
            count += 1                         # increment count if a match is found
    return count


# function to compute the nucleotide (symbol) in a circular genome
def SymbolArray(Genome, symbol):
    array = {}       # empty dictionary to store counts at each position
    n = len(Genome)  # length of the genome

    # extend genome by adding the first half to the end to handle circularity, ex - AAAAGGGG
    ExtendedGenome = Genome + Genome[0:n//2]    # after adding first half - AAAAGGGGAAAA

    for i in range(n):
        window = ExtendedGenome[i:i + (n//2)]   # take a window of length n/2 starting at position i
        array[i] = PatternCount(window, symbol) # count how many times the symbol appears in that window
    return array

input_1 = "AAAAGGGG"
symbol_1 = "A"
input_2 = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
symbol_2 = "CC"

print(SymbolArray(input_1, symbol_1))
print('Output for input_2:')
print(SymbolArray(input_2, symbol_2))
