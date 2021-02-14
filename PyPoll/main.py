#import modules
import os
import csv

#define csv import path
csvpath_in = os.path.join('Resources', 'election_data.csv')



with open(csvpath_in) as csvfile:

    # Specify delimiter
    csvfile = csv.reader(csvfile, delimiter=',') #csv holds contents of csv file

    csv_header = next(csvfile) #remove header row. This iterates to the next row

    
    cand =[]
    candzero = 1 #index at 1 to accoutn for first loop through if statement
    cand1 = 1
    cand2 = 1
    cand3 = 1

    for row in csvfile:
        if row[2] not in cand: #If candidate is not in list of cand
            cand.append(row[2])
        elif cand[0] in row:
            candzero += 1
        elif cand[1] in row:
            cand1 += 1
        elif cand[2] in row:
            cand2 += 1
        elif cand[3] in row:
            cand3 += 1
        else:
            print('Candidate list exceeds four')
        

   

    vote_total = csvfile.line_num-1 #subtract 1 because of header row

cand_list = [candzero,cand1,cand2,cand3]  
winner=cand_list.index(max(candzero,cand1,cand2,cand3))

#print to Gitbash
print(f'Winner {winner}')
print('Election Results')
print('----------------')
print(f'Total Votes: {vote_total}')
print('----------------')
print(f'{cand[0]}: {round(candzero/vote_total*100,2)}% ({candzero})')
print(f'{cand[1]}: {round(cand1/vote_total*100,2)}% ({cand1})')
print(f'{cand[2]}: {round(cand2/vote_total*100,2)}% ({cand2})')
print(f'{cand[3]}: {round(cand3/vote_total*100,2)}% ({cand3})')
print('----------------')
print(f'Winner: {cand[winner]}')
print('----------------')

#print to CSV

#output path
csv_out = os.path.join("analysis", "ElectionResults.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csv_out, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write rows
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['---------------'])
    csvwriter.writerow(['Total Votes' + str(vote_total)])
    csvwriter.writerow(['---------------'])
    csvwriter.writerow([str(cand[0]) +': ' + str(round(candzero/vote_total*100,2)) + '%' + ' (' + str(candzero) + ')'])
    csvwriter.writerow([str(cand[1]) +': ' + str(round(cand1/vote_total*100,2)) + '%' + ' (' + str(cand1) + ')'])
    csvwriter.writerow([str(cand[2]) +': ' + str(round(cand2/vote_total*100,2)) + '%' ' (' + str(cand2) + ')'])
    csvwriter.writerow([str(cand[3]) +': ' + str(round(cand3/vote_total*100,2)) + '%' + ' (' + str(cand3) + ')'])
    csvwriter.writerow(['---------------'])
    csvwriter.writerow(['Winner: ' + str(cand[winner])])
    csvwriter.writerow(['---------------'])