import csv

name = 'article Heading'
maxCalories = 0
currCal = 0
elfcount = 0

for i in range(1):

    with open ('Book1.csv', 'r') as file:
        reader = csv.reader(file)
        for i in range(2266):
            try:
                csv_row = next(reader)
            except StopIteration:
                break
            
            if len(csv_row) > 0:
                val = csv_row[0]
                cal = int(csv_row[0])
                currCal = currCal + cal
                #print(cal)  
                
            else:
                
                print("Elf number:" , end="")
                elfcount = elfcount+1
                print(elfcount)
                print("total calories for this elf: ", end="")
                print(currCal)
                if currCal > maxCalories:
                    maxCalories = currCal
                currCal = 0         
            
print("The MaX CaLORIES IS!!!")
print(maxCalories)