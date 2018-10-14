import os
import csv

file = os.path.join('election_data.csv')

Poll = {}

TotalVotes = 0

with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:

        TotalVotes += 1

        if row[2] in Poll.keys():
            Poll[row[2]] = Poll[row[2]] + 1

        else:
            Poll[row[2]] = 1

Candidates = []
NumberVotes = []

for key, value in Poll.items():
    Candidates.append(key)
    NumberVotes.append(value)

VotePercent = []

for n in NumberVotes:
    VotePercent.append(round(n/TotalVotes*100, 1))

VoteResults = list(zip(Candidates, NumberVotes, VotePercent))

PopularWinner = []

for name in VoteResults:

    if max(NumberVotes) == name[1]:
        PopularWinner.append(name[0])

Winner = PopularWinner[0]

output_file = os.path.join('Output.txt')

with open(output_file, 'w') as txtfile:

    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(TotalVotes) + 
      '\n-------------------------\n')

    for entry in VoteResults:

        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + Winner + '\n-------------------------')

with open(output_file, 'r') as readfile:

    print(readfile.read())