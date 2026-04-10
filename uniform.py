# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats

# data = np.random.normal(0, 1, 1000)

# # histogram
# plt.hist(data, bins=30, density=True)

# # # fit normal
# # mu, std = stats.norm.fit(data)

# data = np.random.uniform(0,1, 10)
# print(data)


# plt.hist(data, bins= 10, density=True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Fix randomness for repeatability
np.random.seed(42)

# 1. Create NON-NORMAL population (Exponential distribution)
# population = np.random.exponential(scale=1, size=10000)
# population = np.random.exponential(scale=1, size=10000)
population = np.random.chisquare(df=1 ,size=10000)

# 2. Parameters
sample_size = 30        # size of each sample
num_frames = 1000        # how many steps (samples)

sample_means = []

# 3. Setup plot
fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
    # Take a new sample
    sample = np.random.choice(population, size=sample_size)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)
    
    # Plot histogram of sample means
    ax.hist(sample_means, bins=20)
    
    ax.set_title(f"CLT forming: {frame+1} sample means")
    ax.set_xlabel("Sample Mean")
    ax.set_ylabel("Frequency")

# 4. Create animation
ani = FuncAnimation(fig, update, frames=num_frames, repeat=False)

# 5. Save as GIF
ani.save("clt_animation.gif", writer=PillowWriter(fps=10))

print("Animation saved as clt_animation.gif")
