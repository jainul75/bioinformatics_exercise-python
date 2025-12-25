# finding patterns in dna sequence

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

print(PatternCount('GCGCGCG', 'GCG'))


# find out how many times a pattern occurs in Vibrio cholerae ori

vibrio_cholerae_ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
search_pattern = "TGATCA"   # pattern we are looking for inside the Vibrio cholerae ori

# using PatternCount function
num = PatternCount(vibrio_cholerae_ori, search_pattern)
# print("The TGATCA pattern was found", num, "times in the Vibrio cholerae ori.")
print(f'The {search_pattern} pattern was found {num} times in the Vibrio cholerae ori.')