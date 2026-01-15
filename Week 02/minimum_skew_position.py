# find the skew array values

def SkewArray(Genome):
    skew = [0]      # initialize skew array with 0
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            skew.append(skew[-1]+1)     # if the nucleotide is 'G', increase skew by 1
        elif Genome[i] == 'C':
            skew.append(skew[-1]-1)     # if the nucleotide is 'C', decrease skew by 1
        else:
            skew.append(skew[-1])       # if the nucleotide is 'A' or 'T', skew remains unchanged
    return skew

sample_input = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print(SkewArray(sample_input))

# find the positions of minimum values in the skew array

def MinimumSkew(Genome):
    positions = []      # output list
    skew_ay = SkewArray(Genome)     # computes the skew array
    min_skew = min(skew_ay)         # finds the smallest value in the skew array
    for i in range(len(skew_ay)):   # finds all positions with minimum skew value
        if skew_ay[i] == min_skew:
            positions.append(i)
    return positions

sample_input_min = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
mp = MinimumSkew(sample_input_min)
print(f"The minimum skew value occurs at position: {mp}")