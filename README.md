# RCV-Simulation
A module and sample script for simulating a Ranked Choice Voting, a.k.a, Instant Runoff election

In June 2021 around the time of the New York Democratic Mayoral Primary, I saw some posts and comments in social media about Ranked Choice Voting (RCV), used in New York City for the first time, being responsible for the anticipated delay in obtaining results. Having been an RCV advocate for a long while, that did not sound correct to me.

This module `rcv.py` and its associated example script `rcv-simulation.py` is my attempt to show that, even in the hands of a relative beginner like myself, an instant-runoff/RCV election is not a time consuming task.

The example script is easy to implement and customize:
```
This is a sample script using the RCV class and its methods
to simulate a ranked choice voting election.

This example uses the default arguments of the ballots method:
fieldsize = 5 (number of candidates)
ranksize = 5  (number of choices a voter can rank)
turnout = 10000  (number of voters/ballots)

You can easily change any or all of these by using keyword arguments
in the ballots method, e.g., r.ballots(turnout=20000).
```

Running the script with defaults will yield the following to your `stdout`:

```
ROUND 1

Candidate E received 2085 first-choice votes
Candidate C received 2025 first-choice votes
Candidate B received 2005 first-choice votes
Candidate A received 1997 first-choice votes
Candidate D received 1893 first-choice votes
Total: 10005

Candidate D got the least votes.


ROUND 2 

Candidate E received 2538 votes.
Candidate C received 2512 votes.
Candidate A received 2494 votes.
Candidate B received 2460 votes.
Total: 10004

Candidate B got the least votes.


ROUND 3 

Candidate E received 3376 votes.
Candidate A received 3343 votes.
Candidate C received 3284 votes.
Total: 10003

Candidate C got the least votes.


ROUND 4 

Candidate E received 5002 votes.
Candidate A received 5000 votes.
Total: 10002
Candidate E has won with a majority: 50.00999800039992 %.

E, A were the finalists.
10005 first-round ballots cast.
3 voters cast ballots without any finalists.
```
