import csv

name = 'article Heading'
maxCalories = 0
secondMax = 0
thirdMax = 0
currCal = 0
elfcount = 1
total3 = 0

for i in range(1):

    with open ('elves.csv', 'r') as file:
        reader = csv.reader(file)
        for i in range(2266):
            try:
                csv_row = next(reader)
            except StopIteration:
                break
            
            if len(csv_row) > 0:
                
                cal = int(csv_row[0])
                currCal = currCal + cal 
                
            else:
                
                print("Elf number:" , end="")
                elfcount = elfcount+1
                print(elfcount)
                print("total calories for this elf: ", end="")
                print(currCal)
                if currCal > maxCalories:
                    maxCalories = currCal
                elif currCal > secondMax:
                    secondMax = currCal
                elif currCal > thirdMax:
                    thirdMax = currCal
                currCal = 0         
            
total3 = maxCalories+secondMax+thirdMax
print("Highest")
print(maxCalories)
print("second")
print(secondMax)
print("third")
print(thirdMax)
print("total")
print(total3)