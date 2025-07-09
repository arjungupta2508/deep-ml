def transpose_matrix(a: list[list[int|float]]) :
  rows = len(a)
  columns = len(a[0])
  b = [[0 for i in range(rows)] for j in range(columns)]

  for i in range(rows):
      for j in range(columns):
         b[j][i] = a[i][j]

  return b
