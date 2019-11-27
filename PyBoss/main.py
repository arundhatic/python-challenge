"""
Import the employee_data.csv file, which currently holds employee records like the below:

Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

Then convert and export the data to use the following format instead:

Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA

In summary, the required conversions are as follows:

The Name column should be split into separate First Name and Last Name columns.

The DOB data should be re-written into MM/DD/YYYY format.

The SSN data should be re-written such that the first five numbers are hidden from view.

The State data should be re-written as simple two-letter abbreviations.

"""

import os
import csv
from collections import Counter
from datetime import date

employeeDataPath = os.path.join("Resources", "employee_data.csv")

def pyBossAnalysis(filepath):
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
    empId = data['Emp ID']
    name = data['Name']
    date = data['DOB']
    ssn = data['SSN'] 
    state = data['State']
    
    # emp id list to the column
    empID = []
    for empIdKey in Counter(empId).keys():
        empID.append(empIdKey)
        
    # creating 1st name and last name as lists
    firstName = []
    lastName = []
    for nameKey in Counter(name).keys():
      firstName.append(nameKey.split(" ")[0])
      lastName.append(nameKey.split(" ")[1])
        
    # extracting DOB and change formating to 0M/0D/Y
    newDOB = []
    for dateKey in Counter(date).keys():
        yr, month, day = [str(f) for f in dateKey.split('-')]
        newDOB.append(f'{month}/{day}/{yr}') 
    
    # replacing first few digits of SSN with *
    newSSN = []
    for ssnKey in Counter(ssn).keys():
        newSSN.append( "***-**" + ssnKey[6:])
        
    #state  abbreviations lookup table/dictionary
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
} 
    stateAbbrev = []
    for stateKey in Counter(state).keys():
       stateAbbrev.append(us_state_abbrev[stateKey]) 
    
    rows = zip(empID,firstName,lastName,newDOB,newSSN, stateAbbrev)
    
    
    # writing the new set of data to a csv file  
    with open('output.csv', "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State" ])
        for row in rows:
            writer.writerow(row)
        
def main():
        pyBossAnalysis(employeeDataPath)


if __name__ == "__main__":
    main()   