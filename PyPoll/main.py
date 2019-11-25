"""
In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""

import os
import csv
from collections import Counter

electionDataPath = os.path.join("Resources", "election_data.csv")

def pollAnalysis(filepath):
   # read the file as a dictionary for each row ({header : value})
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                   data[header].append(value)
                except KeyError:
                   data[header] = [value]
    # extract the variables you want
    voterId = data['Voter ID']
    county = data['County']
    candidate = data['Candidate'] 

    # For debugging
    #print(Counter(candidate).keys()) #the keys of the dictionary, in this case each candidate in the list/set
    #print(Counter(candidate).values()) # counts the elements' frequency

    totalVotes = sum(Counter(candidate).values()) # sum the values of a dictionary

    output = ''
    output += '\n'
    output += 'Election results \n-------------------------\n'
    output += 'Total votes: ' + str(totalVotes) + '\n-------------------------\n'
    for key, value in Counter(candidate).items():
        output += str(key) + ': ' + str(round(value/totalVotes * 100,3)) + '% ' + '(' + str(value) + ')\n'
    output += '-------------------------\nWinner: ' + str(max(Counter(candidate), key=Counter(candidate).get)) + '\n'
    output += '-------------------------\n'
            
    print(output)

    textFile = open('electionResults.txt', 'w')
    textFile.write(output)
    textFile.close() 

def main():
    pollAnalysis(electionDataPath)


if __name__ == "__main__":
    main()