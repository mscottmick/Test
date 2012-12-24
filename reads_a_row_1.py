import csv
with open("password.csv", 'r') as file:
  reader = csv.reader(file)
  third_where_pineapple = [line[0]+ ", " +line [1] + ", " + line[2]+ " " + line[3]+", " + line[4]+ ", " + line[5]+ ", " + line[6] for line in reader if line[1] == 'alan123']
  print (third_where_pineapple)
