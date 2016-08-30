# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

#-------------------------------------------------------------------------------
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    profile = Count(Motifs)
    for symbol in 'ACGT':
        for j in range(k):
            profile[symbol][j] = profile[symbol][j]/float(t)
    return profile

#-------------------------------------------------------------------------------
# Input: A list of kmers Motifs
# Output: the consensus motif
def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

#-------------------------------------------------------------------------------
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    profile = Count(Motifs)
    consensus = Consensus(Motifs)
    t = len(Motifs)
    score = 0
    for i in range(len(Motifs[0])):
        score = score + (t - profile[consensus[i]][i])
    return score
#-------------------------------------------------------------------------------
# Input: A Dna string and profile
# Output: Probability of that Dna string
def Pr(Text, Profile):
    # insert your code here
    pr = 1
    for i in range(len(Text)):
        pr = pr*Profile[Text[i]][i]
    return pr

#-------------------------------------------------------------------------------
# Input: A Dna String and profile
# Output: mMost probable pattern of that string
def ProfileMostProbablePattern(Text, Profile):
    T = len(Text)
    K = len(Profile['A'])
    prob = 0
    x = Text[0:K]
    for i in range(T - K + 1):
        Subtext = Text[i:i+K]
        temp_prob = Pr(Subtext,Profile)
        if temp_prob > prob:
            prob = temp_prob
            x = Subtext
    return x

#-------------------------------------------------------------------------------
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

#-------------------------------------------------------------------------------
# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

#-------------------------------------------------------------------------------
# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    profile = CountWithPseudocounts(Motifs)
    for symbol in 'ACGT':
        for j in range(k):
            profile[symbol][j] = profile[symbol][j]/float(t+4)
    return profile

#-------------------------------------------------------------------------------
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
