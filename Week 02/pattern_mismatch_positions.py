# calculate hamming distance - the total number of mismatches between two string  

def HammingDistance(P, Q):
    count = 0
    for i in range(len(P)):
        if P[i] != Q[i]:
            count = count + 1
    return count

# approximate pattern finding 

def ApproximatePatternMatching(pattern, text, d):      # pattern: the k-mer to search, text: genome string, d: maximum mismatches allowed
    positions = []
    pattern_length = len(pattern)   # length of the pattern (k-mer)

    for i in range(len(text) - pattern_length + 1):
        substring = text[i:i + pattern_length]         # extract k-mer size substring from text
        if HammingDistance(pattern, substring) <= d:   # calculate mismatches using Hamming Distance
            positions.append(i)
    return positions

sample_pattern = 'ATTCTGGA'
sample_text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
d = 3

pattern_mismatch_positions = ApproximatePatternMatching(sample_pattern, sample_text, d)
print(f'The pattern was found at positions: {pattern_mismatch_positions}')