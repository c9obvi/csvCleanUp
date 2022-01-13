import csv
import re

with open('newcsv.csv', 'w+') as fp:
  with open('ID_only_.csv', 'r') as f:
        reader = csv.reader(f)

        for row in reader:
          # print (row)
          splitted = row[0].split('=:')
          user = splitted[0]
          # print(splitted[1])
          time = splitted[1].split('+')[0]
          userData = user + ", " + time
          fp.write(userData + "\n")
          #print(userData)
          # print (time)
          # print(user)
