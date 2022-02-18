
import csv

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
x = 0
for row in tmp:
    print(f' {x + 1} - {tmp[x]}')
    x = x + 1

# import csv
#
# file = open("Books.csv", "r")
# x = 0
# for row in file:
#     display = "Row: " + str(x) + " - " + row
#     print(display)
#     x = x + 1
