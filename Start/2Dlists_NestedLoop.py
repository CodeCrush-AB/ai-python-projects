
number_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_lists[0][0])
# the first '[]' is row, second '[]' is colum

for row in number_lists:
    for col in row:
        print(col)