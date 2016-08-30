# Input: A text and a number as value of k-mer
# Output: Most frequent k-mers of given value
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates
#-------------------------------------------------------------------------------

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Items):
    ItemsNoDuplicates = list(set(Items)) # output variable
    # your code here
    return ItemsNoDuplicates
#-------------------------------------------------------------------------------

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count
#-------------------------------------------------------------------------------
# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
#-------------------------------------------------------------------------------
# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i : i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions
#-------------------------------------------------------------------------------
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    list_gene = Skew(Genome)
    min_val = min(list_gene.values())
    for i in list_gene:
        if list_gene[i] == min_val:
            positions.append(i)
    return positions
#-------------------------------------------------------------------------------
# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {}
    skew[0] = 0
    #initializing the dictionary
    # your code here
    for i in range(1,len(Genome) + 1):
        if Genome[i-1] == 'C':
            skew[i] = skew[i - 1] - 1
        elif Genome[i-1] == 'G':
            skew[i] = skew[i - 1] + 1
        else:
            skew[i] = skew[i - 1]
    return skew
#-------------------------------------------------------------------------------
# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] == q[i]:
            continue
        else:
            count = count + 1
    return count
#-------------------------------------------------------------------------------
# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text) - len(Pattern) + 1):
        ham_dist = HammingDistance(Text[i:i + len(Pattern)] , Pattern)
        if ham_dist <= d:
            positions.append(i)
    return positions
#-------------------------------------------------------------------------------
# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    for i in range(len(Text) - len(Pattern) + 1):
        ham_dist = HammingDistance(Text[i:i + len(Pattern)] , Pattern)
        if ham_dist <= d:
            count = count + 1
    return count
#-------------------------------------------------------------------------------
