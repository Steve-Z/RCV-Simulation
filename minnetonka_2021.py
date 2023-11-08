import csv
from rcv import RCV
from itertools import filterfalse

""" This is a script using the RCV class and its methods
to tabulate a ranked choice voting (instant runoff) election with the data
from Minnetonka, MN single-seat election for city council.

The data was obtained from
https://www.minnetonkamn.gov/home/showpublisheddocument/9848/637716260998730000.
Results obtained from running this script can be compared with the published
results at https://www.minnetonkamn.gov/home/showpublisheddocument/9902/637721487821600000
"""


r = RCV()
candidates = [
    "Stacy Cranbrook",
    "Jim Hadley",
    "Daniel Kral",
    "Ash Patel",
    "Kimberly Wilburn",
]

ballots = []
with open("Minnetonka2021.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        row = [c for c in row if c in candidates]
        if row:
            ballots.append(row)

originals = ballots[:]

round1 = r.count(ballots)

print("ROUND 1\n")

for k, v in round1[0].items():
    print("Candidate", k, "received", v, "first-choice votes")

print("Total:", sum(round1[0].values()))

d = r.runoff(
    first=round1[1], last=round1[2], d=round1[0], rnd=2, ballots=ballots, threshold=5096)
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
