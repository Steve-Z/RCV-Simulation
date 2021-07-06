from rcv import RCV
from itertools import filterfalse

r = RCV()

ballots = r.ballots(fieldsize=7, turnout=1001)
originals = ballots[:]

round1 = r.count(ballots)

print("ROUND 1\n")

for k, v in round1[0].items():
    print("Candidate", k, "received", v, "first-choice votes")

print("Total:", sum(round1[0].values()))

d = r.runoff(first=round1[1], last=round1[2], d=round1[0], rnd=2, ballots=ballots)
print(d.keys())
print(len(originals))


def uncounted(alist):
    tests = []
    for k in d.keys():
        test = k in alist
        tests.append(test)
    return any(tests)


wasted = list(filterfalse(uncounted, originals))
print(wasted)
print(len(wasted))
