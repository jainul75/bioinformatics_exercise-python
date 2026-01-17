# the total number of mismatches between two strings is called the Hamming distance between these strings
# calculate the hamming distance - if the symbols at position i of the two strings are not the same

def HammingDistance(P, Q):
    count = 0
    for i in range(len(P)):
        if P[i] != Q[i]:
            count = count + 1
    return count

string_1 = 'GGGCCGTTGGT'
string_2 = 'GGACCGTTGAC'

hd = HammingDistance(string_1, string_2)
print(f'Total number of mismatch between two string is {hd}.')