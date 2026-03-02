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

# arr_3d = np.array([
#     [[1,2,3], [2,3,4]],
#     [[7,8,9], [8,9,11]],
#     [[7,8,9], [8,9,11]],
#     [[7,8,9], [8,9,11]]
# ])



# print(arr_3d)

# print(f"shape of array is {arr_3d.shape}")

Mean = 25

Std = 5

Shape = (365, 24, 5)


data = np.random.normal(size=Shape, loc=Mean, scale=Std)
# print(data.shape)
# print(data)

nan_count = 500
outlier_count = 50

indices_to_nan = np.random.choice(data.size, nan_count, replace=False)
indicase_to_outlier = np.random.choice(data.size, outlier_count, replace=False)

data.ravel()[indices_to_nan] = np.nan
data.ravel()[indicase_to_outlier] = 999


# print(data)


nan_check = np.isnan(data)

# print(nan_check)
print(nan_check.shape)


# count = np.count_nonzero(nan_check)

layers, rows, cols = np.where(nan_check)

print(len(layers))
print(len(rows))
print(len(cols))

print(layers)
print(rows)
print(cols)
# print(f"The number of True values is: {count}")