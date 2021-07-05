from rcv import RCV

r = RCV()

ballots = r.ballots(turnout=10000)

round1 = r.count(ballots)

print("ROUND 1\n")

for k, v in round1[0].items():
    print("Candidate", k, "received", v, "first-choice votes")

print("Total:", sum(round1[0].values()))

r.runoff(first=round1[1], last=round1[2], d=round1[0], rnd=2, ballots=ballots)
