# RCV-Simulation
A module and sample script for simulating a Ranked Choice Voting, a.k.a, Instant Runoff election

In June 2021 around the time of the New York Democratic Mayoral Primary, I saw some posts and comments in social media about Ranked Choice Voting (RCV), used in New York City for the first time, being responsible for the anticipated delay in obtaining results. Having been an RCV advocate for a long while, that did not sound correct to me.

This module `rcv.py` and its associated example script `rcv-simulation.py` is my attempt to show that, even in the hands of a relative beginner like myself, an instant-runoff/RCV election is not a time consuming task.

The example script is easy to implement and customize:
```
This is a sample script using the RCV class and its methods
to simulate a ranked choice voting election.

This example uses the default arguments of the ballots method:
fieldsize = 7 (number of candidates)
ranksize = 5  (number of choices a voter can rank)
turnout = 10000  (number of voters/ballots)

You can easily change any or all of these by using keyword arguments
in the ballots method, e.g., r.ballots(turnout=20000).
```

Running the script with defaults will yield the following to your `stdout`:

```
ROUND 1

Candidate F received 1505 first-choice votes
Candidate G received 1452 first-choice votes
Candidate A received 1441 first-choice votes
Candidate D received 1419 first-choice votes
Candidate C received 1409 first-choice votes
Candidate B received 1400 first-choice votes
Candidate E received 1382 first-choice votes
Total: 10008

Candidate E got the least votes.


ROUND 2 

Candidate F received 1744 votes.
Candidate G received 1703 votes.
Candidate D received 1659 votes.
Candidate A received 1637 votes.
Candidate B received 1637 votes.
Candidate C received 1627 votes.
Total: 10007

Candidate C got the least votes.


ROUND 3 

Candidate F received 2086 votes.
Candidate G received 2029 votes.
Candidate D received 1979 votes.
Candidate B received 1967 votes.
Candidate A received 1945 votes.
Total: 10006

Candidate A got the least votes.


ROUND 4 

Candidate F received 2595 votes.
Candidate G received 2514 votes.
Candidate D received 2458 votes.
Candidate B received 2438 votes.
Total: 10005

Candidate B got the least votes.


ROUND 5 

Candidate F received 3375 votes.
Candidate G received 3321 votes.
Candidate D received 3308 votes.
Total: 10004

Candidate D got the least votes.


ROUND 6 

Candidate G received 4766 votes.
Candidate F received 4756 votes.
Total: 9522
Candidate G has won with a majority: 50.05250997689561 %.

F, G were the finalists.
10008 first-round ballots cast.
486 voters cast ballots without any finalists.
```
