PyBank
*  In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
*  Your task is to create a Python script that analyzes the records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period
*  As an example, your analysis should look similar to the one below:
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
*  In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll
*  In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
*  You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.
*  As an example, your analysis should look similar to the one below:
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
*  In addition, your final script should both print the analysis to the terminal and export a text file with the results

PyBoss

Import the employee_data.csv file, which currently holds employee records like the below:
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
* Then convert and export the data to use the following format instead:
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
* In summary, the required conversions are as follows:
o The Name column should be split into separate First Name and Last Name columns.
o The DOB data should be re-written into MM/DD/YYYY format.
o The SSN data should be re-written such that the first five numbers are hidden from view.
o The State data should be re-written as simple two-letter abbreviations.

PyParagraph
* Import a text file filled with a paragraph of your choosing.
* Assess the passage for each of the following:
o Approximate word count
o Approximate sentence count
o Approximate letter count (per word)
o Average sentence length (in words)
* As an example, this passage:
“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”
...would yield these results:
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0




