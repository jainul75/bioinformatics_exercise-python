# function for counting pattern/symbol 
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

# SymbolArray function optimization
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute symbol in first window/array
    array[0] = PatternCount(Genome[0:n//2], symbol)
    
    # slide the window across genome
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        # if the symbol leaving the window matches, decrease the count
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1

        # if the symbol entering the window matches, increase the count
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

input_1 = "AAAAGGGG"
symbol_1 = "A"

print(FasterSymbolArray(input_1, symbol_1))

# import time
# start = time.time()
# FasterSymbolArray(Genome, symbol)
# print("FasterSymbolArray time:", time.time() - start)