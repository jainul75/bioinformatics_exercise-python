# function for mapping substrings and their occurrence
def FrequencyMap(Text, k):
    freq = {}      # empty dictionary to store k-mer frequencies
    n = len(Text)

    # first loop: initialize all possible k-mers with count 0
    for i in range(n-k+1):
        pattern = Text[i:i+k]   # extract substring length of k
        freq[pattern] = 0       # initialize the k-mer count to 0

    # second loop: count the occurrences of each k-mer    
    for i in range(n-k+1):
        pattern = Text[i:i+k]   # extract the same substring again
        freq[pattern] = freq[pattern] + 1   # increment the count of the substring (k-mer)
    return freq

# function for finding maximum frequent words
def FrequentWord(Text, k):
    word = []
    freq_w = FrequencyMap(Text, k)   # using the previously defined function to generate a frequency map of all substrings (k-mers) in the text
    max_val = max(freq_w.values())   # maximum frequency value among all k-mers
    for i in freq_w:
        if freq_w[i] == max_val:
            word.append(i)
    return word


input_text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
print(FrequentWord(input_text, k))

# use the FrequentWord function for different input text where k=10 
vibrio_cholerae_ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
new_k = 10
print(FrequentWord(vibrio_cholerae_ori, new_k))