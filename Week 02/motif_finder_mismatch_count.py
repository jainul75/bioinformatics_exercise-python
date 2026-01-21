# calculate hamming distance - the total number of mismatches between two string  

def HammingDistance(P, Q):
    count = 0
    for i in range(len(P)):
        if P[i] != Q[i]:
            count = count + 1
    return count

# approximate pattern finding with mismatch (count total occurrences)

def ApproximatePatternCount(pattern, text, d):      # pattern: the k-mer to search, text: genome string, d: maximum mismatches allowed
    count = 0
    pattern_length = len(pattern)   # length of the pattern (k-mer)

    for i in range(len(text) - pattern_length + 1):
        substring = text[i:i + pattern_length]         # extract k-mer size substring from text
        if HammingDistance(pattern, substring) <= d:   # calculate mismatches using Hamming Distance
            count += 1
    return count

sample_pattern = 'GAGG'
sample_text = 'TTTAGAGCCTTCAGAGG'
d = 2

pattern_mismatch_count = ApproximatePatternCount(sample_pattern, sample_text, d)
print(f'The pattern was found {pattern_mismatch_count} times with at most {d} mismatches.')