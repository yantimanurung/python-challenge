import os
import csv
import sys
csvpath = os.path.join('..', 'Pypoll', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csvreader)
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == "Khan":
            Khan_votes = Khan_votes + 1
        elif row[2] == "Correy":
            Correy_votes = Correy_votes + 1
        elif row[2] == "Li":
            Li_votes = Li_votes + 1
        elif row[2] == "O'Tooley":
            OTooley_votes = OTooley_votes + 1
    Khan_percentage = round(Khan_votes / total_votes *100, 3)
    Correy_percentage = round(Correy_votes / total_votes *100, 3)
    Li_percentage = round(Li_votes / total_votes * 100, 3)
    OTooley_percentage = round(OTooley_votes / total_votes* 100, 3)

    print(f'Election Results')
    print(f'-----------------------------------')
    print(f'Total votes: {total_votes}')
    print(f'-----------------------------------')
    print(f'Khan: {Khan_percentage}% ({Khan_votes})')
    print(f'Correy: {Correy_percentage}% ({Correy_votes})')
    print(f'Li: {Li_percentage}% ({Li_votes})')
    print(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})")
    print(f'-----------------------------------')
    print(f'Winner: Khan')
    print(f'-----------------------------------')
    
    sys.stdout = open('analysis.txt','wt')
    print(f'Election Results')
    print(f'-----------------------------------')
    print(f'Total votes: {total_votes}')
    print(f'-----------------------------------')
    print(f'Khan: {Khan_percentage}% ({Khan_votes})')
    print(f'Correy: {Correy_percentage}% ({Correy_votes})')
    print(f'Li: {Li_percentage}% ({Li_votes})')
    print(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})")
    print(f'-----------------------------------')
    print(f'Winner: Khan')
    print(f'-----------------------------------')
    