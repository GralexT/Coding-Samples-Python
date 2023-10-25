#Author: 21947126-taylog

'''Gets candidates list from text file.
Input filename as '<filename>.txt'.
Returns candidates as list.
'''
def getCandidates(f):
    try:
        candidatelist = open(f,'r').read().strip().split('\n') #Change read() to something more efficient
        for i in range(len(candidatelist)):
            candidatelist[i] = [candidatelist[i],[]]
        return candidatelist
    except IOError:
        print('%s not found'%filename)
        return []

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
If valid input, returns integer list of s.
If invalid input, returns empty list.
Optional voting allows incomplete papers to be valid.
'''
def parsePaper(s,n,optional):
    s = s.split(',')
    if len(s) > n:
        return [] #informal, "too long"
    if optional:
        for i in range(len(s)):
            s[i] = int(parseVote(s[i]))
            if s[i] < 0:
                return [] #informal, "non-digits"
    else:
        for i in range(len(s)):
            s[i] = int(parseVote(s[i]))
            if s[i] < 1:
                return [] #informal, "non-digits", "digits less than 1"
    if sum(s) == 0:
        return [] #informal, "blank"
    return s
'''Gets ballot paper list from text file and parses papers.
Input f as ’<filename>.txt.
Input n as number of candidates.
Returns all parsed papers as list.
'''
def getPapers(f,n,optional):
    try:
        paperlist = open(f,'r').read().strip().split('\n')
        for i in range(len(paperlist)):
            paperlist[i] = parsePaper(paperlist[i],n,optional)
        return paperlist
    except IOError:
        print('%s not found'%f)
        return []

'''Pads incomplete votes with 0's.
'''
def padvotes(votes,numberOfCandidates):
    for vote in votes:
        while len(vote) < numberOfCandidates:
            vote.append(0)
    return votes

'''Counts individual votes, excludes 0 values (padded values).
'''
def countvote(vote):
    return vote.index(min(i for i in vote if vote != 0))

'''Clears all votes already assigned to candidates.
Removes empty votes and spent votes.
Counts votes and tallies vote counts for each candidate.
'''
def countvotes(candidates,voteslist,count=1):
    for i in range(len(candidates)):
        candidates[i][1] = []
    for vote in voteslist:
        if vote == [] or max(vote) == 0:
            voteslist.remove(vote)
            continue
        candidates[countvote(vote)][1].append(vote)
    printCount(candidates, count)

'''Prints count number and results for each candidate after each count.
'''
def printCount(candidates, count):
    print("Count",count)
    for i in range(len(candidates)):
        print(len(candidates[i][1]),"\t",candidates[i][0])
    
'''Finds the least voted candidate and removes them from the race.
Prints notification about eliminated candidate and recounts votes.
'''        
def eliminatecandidate(candidates,formalvotes,count):
    minlength = min(len(candidates[i][1]) for i in range(len(candidates)))
    for i in range(len(candidates)):
        if len(candidates[i][1]) == minlength:
            for vote in formalvotes: 
                del vote[i]
            print("\nCandidate",candidates[i][0],"has the smallest number of votes and is eliminated from the count\n")
            del candidates[i]           
            countvotes(candidates,formalvotes,count)
            break

'''Finds the winner from eliminated candidates by looping through elimination process.
If a tie occurs, the first candidate in line is removed.
If a candidate recieves over 50% of votes, they are elected immediately.
Counter counts number of loops before a candidate is elected.
'''
def conductElection(candidates,formalvotes,count=2):
    if len(candidates) == 2 and len(candidates[0][1]) == len(candidates[1][1]):
        return candidates[1][0],len(formalvotes)
    for i in range(len(candidates)):
        if len(candidates[i][1]) > (len(formalvotes)//2):
            return candidates[i][0],len(formalvotes)
    eliminatecandidate(candidates,formalvotes,count)
    count += 1
    return conductElection(candidates,formalvotes,count)#, len(formalvotes)
    
'''Prints the name of the winning candidate and the number of informal votes.
'''
def printResults(winner,informalcount):
    print("\n"*2+"Candidate",winner,"is elected")
    print(informalcount,"papers excluded as informal")
    
''' Conducts election and prints results of the winner.
Optional=False if full preferential voting.
Optional=True if optional preferential voting.
Prints number of informal votes, including spent votes.
'''
def main(candidatesfile,ballotsfile,optional=False):
    candidates = getCandidates(candidatesfile)
    papers = getPapers(ballotsfile,len(candidates),optional)
    formalvotes = formalisevotes(padvotes([paper for paper in papers if paper != []],len(candidates)))
    countvotes(candidates,formalvotes)
    winner,formalvotes = conductElection(candidates,formalvotes) #May need informal vote recount as a return value
    printResults(winner,len(papers)-formalvotes)

'''Finds informal votes then removes them from the count.
'''
def formalisevotes(votelist):
    templist = []
    for paper in votelist:
        for i in range(1,len(paper)):
            if not ((sorted(paper)[i-1] == 0 and sorted(paper)[i] == 0) or (sorted(paper)[i-1] == sorted(paper)[i]-1)):
                templist.append(votelist.index(paper))
                break
    for i in sorted(templist,reverse=True):
        votelist.remove(votelist[i])
    return votelist
    