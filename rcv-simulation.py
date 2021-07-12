from rcv import RCV
from itertools import filterfalse

""" This is a sample script using the RCV class and its methods
to simulate a ranked choice voting election.

This example uses the default arguments of the ballots method:
fieldsize = 7 (number of candidates)
ranksize = 5  (number of choices a voter can rank)
turnout = 10000  (number of voters/ballots)

You can easily change any or all of these by using keyword arguments
in the ballots method, e.g., r.ballots(turnout=20000). """


r = RCV()

ballots = r.ballots()
originals = ballots[:]

round1 = r.count(ballots)

print("ROUND 1\n")

for k, v in round1[0].items():
    print("Candidate", k, "received", v, "first-choice votes")

print("Total:", sum(round1[0].values()))

d = r.runoff(
    first=round1[1], last=round1[2], d=round1[0], rnd=2, ballots=ballots)
print(d)
print(', '.join(list(d)), "were the finalists.")
print(len(originals), "first-round ballots cast.")


def uncounted(alist):
    tests = []
    for k in d.keys():
        test = k in alist
        tests.append(test)
    return any(tests)


wasted = list(filterfalse(uncounted, originals))

print(len(wasted), "voters cast ballots without any finalists.")
