#import modules
import os
import csv

#define csv import path
csvpath_in = os.path.join('Resources', 'budget_data.csv')

with open(csvpath_in) as csvfile:

    # Specify delimiter
    csv1 = csv.reader(csvfile, delimiter=',') #csv holds contents of csv file

    csv_header = next(csv1) #remove header row. This iterates to the next row

    change=[]
    month=[]
    last = 0

    for r in csv1:
        if last == 0: #start counting different on second row
            last = r[1]
            total = int(r[1]) #intitiate total on row 0
        else:
            change.append(int(r[1]) - int(last))
            month.append(r[0])
            total += int(r[1])
            last = int(r[1])

    
    month_count = csv1.line_num-1 #Bullet 1: determine the number of months included in the dataset. -1 to subtract for header
    average_change = round(sum(change)/len(change),2) #Bullet 3: Calculate change in P/L and average of changes
    
    in_max = max(change)
    in_index = change.index(in_max)
    
    dec_min = min(change)
    dec_index = change.index(dec_min)


    #print to terminal
    print(f'Financial Analyis \n-----------------------')
    print(f'Month Count {month_count}')
    print(f'Net Sum ${total}')
    print(f'Average Change ${average_change}')
    print(f'Greatest Increase {month[in_index]} ${in_max}')
    print(f'Greatest Descrease {month[dec_index]} ${dec_min}')

#output path
csv_out = os.path.join("analysis", "FinancialAnalysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csv_out, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write rows
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])    
    csvwriter.writerow(['Month Count',str(month_count)])
    csvwriter.writerow(['Net Sum','$' + str(total)])
    csvwriter.writerow(['Average Change', '$' + str(average_change)])
    csvwriter.writerow(['Greatest Increase', month[in_index], '$' + str(in_max)])
    csvwriter.writerow(['Greatest Descrease', month[dec_index], '$' + str(dec_min)])
