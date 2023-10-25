"""
Submission for Project 1, Election Night. 

Program conducts the Nerdvanian Election of 2017.
Requires two text file inputs; one candidates list and one list of submitted ballot papers.

Author: Grant Alexander Taylor, 21947126.
Date: 22/09/2017
Version 1.0
"""



'''Gets candidates list from text file.
Input f as '<filename>.txt.
Returns candidates as list.
'''
def getCandidates(f):
    try:
        candidatelist = open(f,'r').read().strip().split('\n')
        return candidatelist
    except IOError:
        print('%s not found'%f)
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
If valid input, returns integer list of s and empty message.
If invalid input, returns empty list and error message
'''
def parsePaper(s,n):
    message = ''
    s = s.split(',')
    if len(s) > n:
        return [],"too long"
    for i in range(len(s)):
        s[i] = int(parseVote(s[i]))
        if s[i] < 0:
            return [],"non-digits"
    if sum(s) == 0 and s != []:
        return [],"blank"
    return s,message


'''Gets ballot paper list from text file and parses papers.
Input f as '<filename>.txt.
Input n as number of candidates.
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


'''Normalises individual papers and pads votes to contain equal number of votes to candidates.
Input p as list of integers.
Input n as number of candidates.
Returns normalised paper as list.
'''
def normalisePaper(p,n):
    sump = sum(p)
    for i in range(len(p)):
        p[i] /= sump
    while len(p) < n:
        p.append(0)
    return p


'''Normalises list of papers using normalisePaper(p,n) for each paper.
Input ps as list of paper lists.
Input n as number of candidates.
Returns normalised papers as list.
'''
def normalisePapers(ps,n):
    for i in range(len(ps)):
        ps[i] = normalisePaper(ps[i],n)
    return ps


'''Sums normalised papers for each candidate.
Input cs as list of candidates.
Input ps as list normalised papers.
Returns list of summed votes attached to their candidates in descending order.
'''
def countVotes(cs,ps):
    candidatecount = []
    for i in range(len(cs)):
        candidatecount.append([sum(paper[i] for paper in ps),cs[i]])
    candidatecount.sort(reverse=True)
    return candidatecount


'''Prints single space indented election results for each candidate.
Input c as countVotes(cs,ps).
'''
def printCount(c):
    for i in range(len(c)):
        c[i][0] = "%.2f"%c[i][0]
    for i in c:
        results = ' '.join(str(x) for x in i)
        print(" "+results)
    return


'''Prints election results with formal and informal vote counts included.
'''
def main():
    candidates = getCandidates(input('Enter candidate list file as <filename.txt>: '))
    papers = getPapers(input('Enter vote list file as <filename.txt>: '), len(candidates))
    papervotes = []
    informal = []
    for vote in papers:
        if vote[0] != []:
            papervotes.append(vote[0])
        else:
            informal.append(vote[0])
    print("\nNerdvanian election 2017\n")
    print("There were", str(len(informal)),"informal votes")
    print("There were", str(len(papers) - len(informal)),"formal votes \n")
    printCount(countVotes(candidates, normalisePapers(papervotes, len(candidates))))