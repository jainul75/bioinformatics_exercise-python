# In bioinformatics, k-mers are substrings of length k contained within a biological sequence. (wikipedia)
# find the frequency of a word or k-mer from a given text
# values of k can be any numerical value - length of the word/k-mer

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


input_text = "CGATATATCCATAG"
k = 3
print(FrequencyMap(input_text, k))