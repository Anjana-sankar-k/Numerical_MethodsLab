def add_matrices(mat1, mat2):
  rows, cols = len(mat1), len(mat1[0])
  result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
  return result
  
  
matrix1 = [[1, 2, 3], [4, 5, 6], [ 7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = add_matrices(matrix1, matrix2)
print("Resultant matrix: ")
for row in result: 
  print(row)
  
