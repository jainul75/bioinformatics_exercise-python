# skew array measures the imbalance between two nucleotides along a genome
# cumulative difference between the number of 'G' and 'C'
# starts with 0, add +1 for 'G', subtract -1 for 'C', and no change for 'A' or 'T'
# minimum skew value often indicates the origin of replication

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

sample_input = "CATGGGCATCGGCCATACGCC"

print(SkewArray(sample_input))