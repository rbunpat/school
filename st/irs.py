#get input1 from user
input1 = input("Enter a number: ")
#add 7 percent vat and 30 percent profit to input1
saleprice = float(input1) * 1.07 + float(input1) * 0.3
#add 30 percent profit to input1
ogandprofit = float(input1) * 0.3 + float(input1)

#print out the result

print("The sale price is " + str(saleprice))
print("The original price with profit is " + str(ogandprofit))
