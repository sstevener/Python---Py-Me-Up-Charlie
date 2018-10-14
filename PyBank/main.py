import csv
import os

file = os.path.join('budget_data.csv')
TotalMonths = 0
ProfitLoss = 0
TotalProfitLoss = 0
PreviousProfitLoss = 0
GreatestIncreaseDate = []
GreatestIncrease = 0
GreatestDecreaseDate = []
GreatestDecrease = 0
RevenueChange = 0
RevenueChangeList = []
AverageRevenue = []


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:

        TotalMonths = TotalMonths + 1  

        TotalProfitLoss = int(row[1]) + TotalProfitLoss
   
        PreviousProfitLoss = int(row[1])

        TotalProfitLoss += int(row[1])
        RevenueChange = int(row[1]) - int(PreviousProfitLoss)

        if TotalProfitLoss > 0:

            if int(row[1]) >= GreatestIncrease:
                GreatestIncrease = int(row[1])
                GreatestIncreaseDate = row[0]

            if int(row[1]) <= GreatestDecrease:
                GreatestDecrease = int(row[1])
                GreatestDecreaseDate = row[0]

    AverageRevenue = round(TotalProfitLoss/TotalMonths, 2)

with open(output_dest, 'r') as readfile:
    print(readfile.read())

    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(TotalMonths))
    print("Total Revenue: " + "$" + str(TotalProfitLoss))
    print("Average Revenue: " + "$" + str(round(TotalProfitLoss/TotalMonths, 2)))
    print("Greatest Increase: " + str(GreatestIncreaseDate[0]) + " ($" + str(GreatestIncrease[1]) + ")")
    print("Greatest Decrease: " + str(GreatestDecreaseDate[0]) + " ($" + str(GreatestDecrease[1]) + ")")
    
with open('pybank_output.txt', "w") as txt_file:

    txt_file.write("TotalMonths: " + str(TotalMonths))
    txt_file.write("\n")
    txt_file.write('Total Revenue: $' + str(TotalProfitLoss) + '\n')
    txt_file.write("\n")
    txt_file.write('Average Revenue: $' + str(round(TotalProfitLoss/TotalMonths, 2)) + '\n')
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(GreatestIncreaseDate) + " ($" + str(GreatestIncrease)"+ '\n")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(GreatestDecreaseDate) + " ($" + str(GreatestDecrease) + ")")
