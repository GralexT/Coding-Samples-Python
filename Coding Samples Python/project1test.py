"""
Short test file for Project 1, Election Night. 

We do not claim that this file is a complete testing scheme: 
its primary purpose is to check the spelling of the function names. 
You should supplement the tests in this file with your own tests. 
The correctness of your program is your responsibility. 

Author: Lyndon While 
Date: 3/4/14
Version 1.15 
Recoded: Michael Wise
Date: 17/4/17
"""


import project1
import os.path


#a non-existent file
nonfile = "nofile.txt"

tupletype = type(())
listtype = type([])

# A recursive function to turn lists or tuples involving tuples into the equivalent lists
def untuple(x) :
  if type(x) == tupletype  or type(x) == listtype :
    newlist = []
    for item in x :
      newlist.append(untuple(item))
    return(newlist)
  return(x)



def test_getCandidates():
    f = "candidates.txt"
    flist = ["Major Clanger", "Soup Dragon", "Froglet", "Iron Chicken", "The Cloud"]
    tests = [[f, flist], [nonfile, []]]
    results = []
    for x, y in  tests :
       results.append([untuple(project1.getCandidates(x)), y])
    return results

def test_parseVote():
    tests = [["", 0], ["no", -1], ["27", 27]]
    results = []
    for x, y in  tests :
        results.append([untuple(project1.parseVote(x)), y])
    return results

def test_parsePaper():
    tests = [[",,, ",      4, [[],         "blank"]]
            ,["  3,4,5  ", 2, [[],         "too long"]]
            ,["4,-4,4",    3, [[],         "non-digits"]]
            ,["4,5, 16",   6, [[4, 5, 16], ""]]
            ,["9876",      8, [[9876],     ""]]]
    results = []
    for x, y, z in  tests :
        results.append([untuple(project1.parsePaper(x, y)), z])
    return results

def test_getPapers():
    f = "smallfile.txt"
    tests = [[f, [[[1,2,3,4], ""], 
                  [[], "blank"],
                  [[0,23,0], ""],
                  [[], "non-digits"], 
                  [[], "non-digits"],
                  [[4,0,4,4], ""],
                  [[], "too long"]]],
              [nonfile, []]]
    results = []
    for x, y in tests:
        results.append([untuple(project1.getPapers(x, 4)), y])
    return results

def test_normalisePaper():
    tests = [[[2,1,5], 3, [0.25, 0.125, 0.625]]
            ,[[8,2],   4, [0.8,  0.2,   0,    0]]
            ,[[7],     4, [1,    0,     0,    0]]]
    results = []
    for x, y, z in tests:
        results.append([untuple(project1.normalisePaper(x, y)), z])
    return results

def test_normalisePapers():
    tests = [[[[2,1,5], [8,2]], 3, [[0.25,0.125,0.625], [0.8,0.2,0]]]]
    results = []
    for x, y, z in tests:
        results.append([untuple(project1.normalisePapers(x, y)), z])
    return results

def test_countVotes():
    tests = [(["A", "B", "C"], [[0,0,1], [0,1,0], [0,0,1]], [[2,   "C"], [1,   "B"], [0,   "A"]])
            ,(["A", "B", "C"], [[0.7, 0.2, 0.1]],           [[0.7, "A"], [0.2, "B"], [0.1, "C"]])]
    results = []
    for cs, ps, x in tests :
        results.append([untuple(project1.countVotes(cs, ps)), x])
    return results

# Interested in which tests failed, but just count of those passed
def msg(f, z) :
    tests_failed = [] 
    count_passed = 0
    for i  in range(len(z)) :
      x, y = z[i]
      if x == y:
        count_passed += 1
      else:
        tests_failed.append(i) 
    if count_passed == 0 and tests_failed == [] :
      s = "untested"
    elif count_passed == len(z) :
      s = "all " + str(count_passed) + " test(s) correct"
    else:
      s = "Test tests incorrect: " + str(tests_failed)
    print("%20s" % (f + ":"), s)
      

def main() :
  tests = [("getCandidates", "test_getCandidates()"),
	   ("parseVote", "test_parseVote()"),
           ("parsePaper", "test_parsePaper()"),
           ("getPapers", "test_getPapers()"),
           ("normalisePaper", "test_normalisePaper()"),
           ("normalisePapers", "test_normalisePapers()"),
           ("countVotes", "test_countVotes()")]
  for m, f in tests:
    try:
      z = eval(f)
      msg(m, z)
    except  BaseException as err:
      print("\nException thrown when testing {0:s}: {1:s}\n".format(m, str(err)))
  print()

if __name__ == "__main__" :
  main()

