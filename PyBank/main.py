import csv , os

path= os.path.join ('..' , 'PyBank' , 'budget_data.csv')

counta=0
sum=0
x=0
sum_ave=0
list_data=[]
list_date=[]
tafavot_list=[]
change_sum=0


with open (path , "r" , newline='' , encoding="UTF-8" ) as budget_data:
    csv_reader= csv.reader(budget_data , delimiter= "," )

    header= next(csv_reader)

    for row in csv_reader:
        counta+=1
           
        sum = sum+ int(row[1])
        list_data.append(int(row[1]))
        list_date.append(str(row[0]))    
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {counta}")
print(f"Total: ${sum}")
#print (list_data)


for i in range(int(counta)-1):
    z=(list_data[i+1])-(list_data[i])
    tafavot_list.append(z)
#print(tafavot_list)


for nums in tafavot_list:

    change_sum+= nums
    average_change=round(change_sum/(counta-1) , 2)



max= max(tafavot_list)
max_index= tafavot_list.index(max)
max_increase= list_date[max_index+1]

min= min(tafavot_list)
min_index= tafavot_list.index(min)
max_decrease= list_date[min_index+1]


print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {max_increase} (${max})")
print(f"Greatest Decrease in Profits: {max_decrease} (${min}) ")

path= os.path.join ('..' , 'PyBank' , 'budget_data.txt')
with open (path , "w" , newline='' , encoding="UTF-8" ) as budget_data_txt:
    budget_data_txt.write("Financial Analysis" '\n')
    budget_data_txt.write("-----------------------------")
    budget_data_txt.write(f"Total Months: {counta} ")
    budget_data_txt.write(f"Total: ${sum}")
    budget_data_txt.write(f"Average Change: $ {average_change}")
    budget_data_txt.write(f"Greatest Increase in Profits: {max_increase} (${max})")
    budget_data_txt.write(f"Greatest Decrease in Profits: {max_decrease} (${min}) ")