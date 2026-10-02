data_2d_array = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
];

for i in range(0, len(data_2d_array)):
    for j in range(0, len(data_2d_array[i])):
        print(data_2d_array[i][j], end=" ")
    print()
        