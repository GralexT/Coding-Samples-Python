''' 1st candidate vote counts as 1 vote.
If candidate of preference is removed, count next votes from candidates voters.
Assign each vote list to its current preffered candidate?
Assign counter at end of each vote list so next pref = counter+1?
No duplicate numbers!
length of candidates list = length of vote count.
'''
def main(candidatesfile,ballotsfile,optional=False):
    candidates = getcanddidates(candidatesfile)
    papers = getpapers(ballotsfile,len(candidates))
    countvotes(candidates,papers)
    winner,informalcount = conductelecction(candidates,formalvotes) #May need informal vote recount as a return value
    printresults(winner,informalcount)

'''Gets candidates list from text file.
Input filename as '<filename>.txt'.
Returns candidates as list.
'''
def getCandidates(f):
    try:
        candidatelist = open(f,'r').read().strip().split('\n') #Change read() to something more efficient
        for i in range(len(candidatelist)):
            candidatelist[i] = (candidatelist[i],[])
        return candidatelist
    except IOError:
        print('%s not found'%filename)
        return []
    
'''Prints the name of the winning candidate and the number of informal votes.
'''
def printresults(winner,informalVotesCount):
    print('\n'*2+'Candidate',winner,'is elected')
    print(informalCount,'papers excluded as informal')

'''Parses singular votes.
Returns 0 for empty votes.
Returns -1 for invalid votes.
Returns input for valid votes.
'''
def parseVote(s):
    s = s.strip()
    if s == "":
        return 0
    elif not s.isdigit():
        return -1
    else:
        return int(s)
'''Parses singular ballot papers.
Input s as string of integers to represent votes on ballot paper.
Input n as number of candidates.
If valid input, returns integer list of s and empty message.
If invalid input, returns empty list and error message
'''
def parsePaper(s,n):
    s = s.split(',')
    if len(s) > n:
        return [] #informal, "too long"
    for i in range(len(s)):
        s[i] = int(parseVote(s[i]))
        if s[i] < 0:
            return [] #informal, "non-digits"
    if sum(s) == 0 and s != []:
        return [] #informal, "blank"
    return s
'''Gets ballot paper list from text file and parses papers.
Input f as ’<filename>.txt.
Input n as number of candidates.
21947126-taylog14
Returns all parsed papers as list.
'''
def getPapers(f,n):
    try:
        paperlist = open(f,'r').read().strip().split('\n')
        i = 0
        for i in range(len(paperlist)):
            paperlist[i] = parsePaper(paperlist[i],n)
        return paperlist
    except IOError:
        print('%s not found'%f)
        return []

#if optional
def padvote(votes,numberOfCandidates):
    for vote in votes:
        while len(vote) < numberOfCandidates:
            vote.append(0)
    return votes

def countvote(vote,eliminated):
    return vote.index(min(i for i in vote if i not in eliminated))

def countvotes(candidates,voteslist,eliminated):
    for vote in voteslist:
        candidates[countvote(vote,eliminated)][1].append(vote)
        
def conductelection(candidates,formalvotes,eliminated=[]):
    if len(candidates) == 2 and len(candidates[0][1]) == len(candidates[1][1]):
        return candidates[1]
    for i in range(len(candidates)):
        if len(candidates[i][1]) > formalvotes // 2:
            return candidates[i]
    #function eliminatecandidate(candidates,eliminated)
    minlength = min(len(candidates[i][1]) for i in range(len(candidates)) if i not in eliminated)
    for i in range(len(candidates)):
        if i not in eliminated: # candidates[i][1] != []
            if len(candidates[i][1]) == minlength:
                eliminated.append(i)
                countvotes(candidates,candidates[i][1],eliminated)
                candidates[i][1] = []
                break
    return eliminated
            
        #min candidate votes recounted and assigned to next candidate in running
        #min candidate removed. If tied, randompick(c1,c2)//returns c2.
        #print "candidate removed",counts//add this to randompick function.
        #For optional, if next pref counter exceeds len(votelist), vote discarded and counted as informal.

