number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])

# can't work below
# for i in range(len(number_grid)):
#     for j in range(number_grid[i]):
#         print(number_grid[i][j])

for row in number_grid:
    for col in row:
        print(col)