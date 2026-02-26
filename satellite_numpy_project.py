import numpy as np

# Create a 3D array
# list_3d = [
#     [[1,2], [3,4]]
# ]

# for i, value in enumerate(list_3d):
#     for j, data in enumerate(list_3d[i]):
#        for k, finaldata in enumerate (list_3d[i][j]):
#            print(finaldata)


# depth, rows, cols = 2, 3, 4

# list_3d = [[[0 for _ in range(cols)] for _ in range(rows)]for _ in range(cols)]
# print(list_3d)

arr_3d = np.array([
    [[1,2,3], [2,3,4]],
    [[7,8,9], [8,9,11]],
    [[7,8,9], [8,9,11]],
    [[7,8,9], [8,9,11]]
])



print(arr_3d)

print(f"shape of array is {arr_3d.shape}")