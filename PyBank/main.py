"""
 In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
 [budget_data.csv](PyBank/Resources/budget_data.csv). 
 The dataset is composed of two columns: `Date` and `Profit/Losses`. 

Your task is to create a Python script that analyzes the records to calculate each of the following:
       1.	The total number of months included in the dataset
       2.	The total net amount of "Profit/Losses" over the entire period
       3.	The average change in "Profit/Losses" between months over the entire period
       4.	The greatest increase in profits (date and amount) over the entire period
       5.	The greatest decrease in losses (date and amount) over the entire period
As an example, your analysis should look similar to the one below:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
 
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""
# import the modules
import os
import csv

# set the path for the csv file in pyBankPath
pyBankPath = os.path.join("Resources","budget_data.csv")

 
def profitLossAnalysis(filePath):
    with open(filePath,newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=",")
        # initialise variables
        monthCount = 0
        totalProfitLoss = 0
        prevValue = 0
        currentValue = 0
        average=0
        maxValue = 0
        minValue = 0 
        next(dataReader,None)
         
        for row in dataReader:
            monthCount+=1
            proftLossValue = int(row[-1])
            totalProfitLoss+= proftLossValue
             
            currentValue = proftLossValue
             
            if monthCount > 1:
                change = currentValue - prevValue
                average+= change
                if change > maxValue:
                    maxValue = change
                    maxMonth = row[0]
                if change < minValue:
                    minValue = change
                    minMonth = row[0]
             
            prevValue = currentValue
             
             
    output = ''
    output += 'Financial Analysis \n-------------------------\n'
    output += 'Total Months: ' + str(monthCount) + '\n'
    output += 'Total: $' + str(totalProfitLoss) + '\n'
    output += 'Average Change: $' + str((round(average/(monthCount-1), 2))) + '\n'
    output += 'Greatest Increase in Profits: ' + maxMonth + ' ($' + str(maxValue) + ')\n'
    output += 'Greatest Decrease in Profits: ' + minMonth + ' ($' + str(minValue) + ')'
        
    print(output)        
        
 
    textfile = open('PyBank.txt', 'w')
    textfile.write(output)
    textfile.close()
 
def main():
    profitLossAnalysis(pyBankPath)


if __name__ == "__main__":
    main()