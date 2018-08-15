import csv , os

path= os.path.join ('..' , 'PyPoll' , 'election_data.csv')

counta=0
candidate=[]
unique=[]
candidate=[]
count=0
votes=[]
percent=[]
output=[]

with open (path , "r" , newline='' , encoding="UTF-8" ) as vote_data:
    csv_reader= csv.reader(vote_data , delimiter= "," )

    header= next(csv_reader)
    
    for row in csv_reader:
        counta+=1
        candidate.append(row[2])   

    unique.append(candidate[0])
    for i in candidate:
        if i not in unique:
            unique.append(i)


    for i in range(len(unique)):

        for name in candidate:

            if name== unique[i]:
                count+=1  
        votes.append(count)
        count=0

for vote in votes:
    p= float(vote/counta)*100
    f=round(p,2)
    percent.append(str(f)+"%")
winner_max= max(votes)  
winner_index=votes.index(winner_max)
winner=unique[winner_index]

print("Election Results")
print("----------------------------")
print (f"Total Votes : {counta}")
print("----------------------------")

output=zip(unique , percent , votes)
for i in output:
    print(f"{i}")

print("----------------------------")
print(f"winner : {winner}")
print("----------------------------")

path= os.path.join ('..' , 'PyPoll' , 'pypoll.txt')
with open (path , "w" , newline='' , encoding="UTF-8" ) as pypoll_txt:
    pypoll_txt.write("Election Results")
    pypoll_txt.write("-----------------------------")
    pypoll_txt.write(f"Total Votes : {counta}")
    pypoll_txt.write("-----------------------------")
    
    ##pypoll_txt.write(i for i in zip)

    pypoll_txt.write("----------------------------")
    pypoll_txt.write(f"winner : {winner}")
    pypoll_txt.write("----------------------------")
    
    
