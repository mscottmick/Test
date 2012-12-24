import csv

passwordreader = csv.reader(open('password.csv', 'r'), delimiter=',', quotechar='"')
a = []
for row in passwordreader:
  a += [", ".join(row)]

  print(a)

password =input ("What is your password? ")

  

if password == row:
  print ("Yes")

else:
  print ("no")
    
    
