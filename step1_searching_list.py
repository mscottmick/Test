import csv

portfolio = csv.reader(open("password.csv", "r"))
portfolio_list = []
portfolio_list.extend(portfolio)
names = []
for data in portfolio_list:
    names.append(data[1])



value= input("What is your password? ") 
if value in names:
        print ("list contains " + value)
        for row in portfolio_list:
            print (row[0])
            #print (row[1])
            #print (row[2])
            #print (row[3])

else:
    print("no "+ value)
   


#print (names)
