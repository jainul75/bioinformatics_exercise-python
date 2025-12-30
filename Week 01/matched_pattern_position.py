# function for finding matched pattern/substring position

def PatternMatching(pattern, genome):
    positions = []                                   # empty list       
    for i in range(len(genome) - len(pattern) + 1):  # defining the range for finding patterns
        if genome[i:i+len(pattern)] == pattern:      # start from position 0 and looking for exact pattern
            positions.append(i)                      # if we find the pattern, position of the pattern will add in the empty list
    return positions

p = 'ATAT'
g = 'GATATATGCATATACTT'
pattern_locations = PatternMatching(p, g)

print(f"Pattern 'ATAT' found at positions {pattern_locations} in the genome.")

p_locations = ", ".join(map(str, pattern_locations)) # convert the list of pattern positions into a comma separated string
print(f"Pattern 'ATAT' found at positions {p_locations} in the genome.")


# lets use our PatternMatching function to find a new pattern positions inside vibrio cholerae ori
# the vibrio cholerae ori sequence stored in a txt file - "Vibrio_cholerae.txt"
# open the file and read the genome sequence

with open("Vibrio_cholerae.txt", "r") as file:
    vibrio_cholerae_ori = file.read().strip()   # remove any extra whitespace or newlines

search_pattern = "CTTGATCAT"   # pattern we are looking for inside the Vibrio cholerae ori

positions = PatternMatching(search_pattern, vibrio_cholerae_ori)
print(f"Pattern '{search_pattern}' found at Vibrio cholerae ori positions: {positions}")