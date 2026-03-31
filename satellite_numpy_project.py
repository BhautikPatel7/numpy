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
outlier_count = 0

indices_to_nan = np.random.choice(data.size, nan_count, replace=False)
indicase_to_outlier = np.random.choice(data.size, outlier_count, replace=False)

data.ravel()[indices_to_nan] = np.nan
data.ravel()[indicase_to_outlier] = 999


# print(data)


nan_check = np.isnan(data)

# print(nan_check)
print(nan_check.shape)


# count = np.count_nonzero(nan_check)

# layers, rows, cols = np.where(nan_check)

nan_index = np.argwhere(nan_check)
print(nan_index, "Nan index")
# print(len(layers))
# print(len(rows))
# print(len(cols))

print(nan_index[0][0])
# print(rows)
# print(cols)
# print(f"The number of True values is: {count}")

print(data[nan_index[0][0]][nan_index[0][1]][nan_index[0][2]])

data[nan_index[0][0]][nan_index[0][1]][nan_index[0][2]] = 15

print(data[nan_index[0][0]][nan_index[0][1]][nan_index[0][2]])
# for i, data in enumerate(nan_index):
#     # print(f"{i} {data}")
#     for j , indata in enumerate(data):
#         print(f"{j} + {indata}")
#     # print(data)

col_mean = np.nanmean(data, axis=0)
col_std = np.nanstd(data, axis=0)
# print(col_std) 
print(col_std.shape) 
# print(col_mean)
print(col_mean.shape)
# 

# for h in range(data.shape[1]):        # 24 hours
#     for f in range(data.shape[2]):    # 5 features
        
#         column = data[:, h, f]       # all 365 days
        
#         mean_val = np.nanmean(column)
        
#         for d in range(data.shape[0]):   # 365 days
#             if np.isnan(data[d][h][f]):
#                 data[d][h][f] = mean_val
                
                

nan_indices = np.where(np.isnan(data))
# 

indices = np.where(col_std > 5)
print(data.shape[1])
print(data.shape[2])
print(data.shape[0])
# print(indices)
for h in range(data.shape[1]):        # 24 hours
    for f in range(data.shape[2]):    # 5 features
        
        col = data[:, h, f]
        # print(col)
        median_val = np.nanmedian(col)
        
        # Replace NaN
        for d in range(data.shape[0]):
            if np.isnan(data[d][h][f]):
                data[d][h][f] = median_val
# print(nan_indices.count())

data[nan_indices] = col_mean[nan_indices[1], nan_indices[2]]


# Step 4

# Convert to (360, 120)c

data_2d = data.reshape(data.shape[0], -1)
print(data_2d[0])

flatten = data.flatten()
print(flatten.shape)
# print(flatten)

data = data.reshape(365,24,5)
print(data.shape)

swapped_arr = np.swapaxes(data, 1, 2)
print("\nSwapped array shape:", swapped_arr.shape)
# print(swapped_arr)


transposed_arr = data.T
print(transposed_arr.shape)



# step 5
mean_value = np.mean(data)
# print(mean_value)


daily_avg = np.mean(data[:, :, 0], axis=1)
# print(daily_avg)
hourly_avg = np.nanmean(data[:, :, 0], axis=0)
# print(hourly_avg)


sensor_yearly_avg = np.nanmean(data, axis=(0, 1))
# print(sensor_yearly_avg)


global_min_func = np.min(data)
global_max_func = np.max(data)

print(global_max_func)
print(global_min_func)

dat_with_max_temp = np.where(data == global_max_func)
print(dat_with_max_temp)


# step 6

day_200 = data[199]
sort_200 = np.sort(day_200)
print(sort_200)


temp = data[:, :, 0] 
print(temp.shape)

flat_indices = np.argsort(temp, axis=None)[-10:]
print(flat_indices)
top_indices = np.unravel_index(flat_indices, temp.shape)
print(top_indices)
for d, h in zip(top_indices[0], top_indices[1]):
    print(f"Day {d}, Hour {h}, Temp = {temp[d, h]}")
    
    
sensor_avg = np.nanmean(data, axis=(0, 1))
print(sensor_avg)

rank_indices = np.argsort(sensor_avg)[::-1]

for rank, sensor_id in enumerate(rank_indices, start=1):
    print(f"Rank {rank}: Sensor {sensor_id}, Avg Temp = {sensor_avg[sensor_id]:.2f}")
    
    
    
# Step 7


sensor_data = data[:,:,0]
print(sensor_data)


for i in range(5):
    sensor_wise_mean = np.mean(sensor_data[i])
    print(sensor_wise_mean)
# sensor_wise_mean = np.mean(sensor_data[0])


normalized_col = (data - data.min(axis=(0,1))) / (data.max(axis=(0,1)) - data.min(axis=(0,1)))
print(normalized_col)

correction_factor = np.ones((5))
print(correction_factor)


corrected_data = data + correction_factor
# print(corrected_data)




# q1 = data[:92]
# # q2 = data[93:184]
# q3 = data[185:276]
# q4 = data[276:]


quarters = np.array_split(data, 4)
q1, q2, q3, q4 = quarters


q1_q2 = np.concatenate((q1, q2), axis=0)
print(q1_q2.shape)


# result = np.concatenate((q1, q2), axis=2)
# print(result.shape)

one_day = data[0][0]
cov_matrix = np.cov(one_day)
print(cov_matrix)

correlation_matrix = np.corrcoef(one_day)
print(corrected_data)


# eigenvalues, eigenvectors = np.linalg.eig(data[0])

# print(Da)

cov_matrix = np.cov(data_2d, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print(eigenvalues)
print(eigenvectors)