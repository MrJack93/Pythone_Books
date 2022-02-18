
# import csv
#
# file = open('Books.csv', 'r')
# search_start = int(input('Enter starting year: '))
# search_finish = int(input('Enter end year : '))
# reader = csv.reader(file)
#
# book_list = []
# for row in file:
#     for year in range(search_start, search_finish):
#         if str(year) in str(row):
#             book_list.append(row)
# print(book_list)

import csv
start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
x = 0
for row in tmp:
    if start <= int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x + 1
