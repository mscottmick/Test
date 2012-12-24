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

else:
    print("no "+ value)


#print (names)
