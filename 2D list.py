matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
#rows
print(len(matrix))
#columns
print(len(matrix[0]))
print(matrix[1][2])

for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print("\n")