MASTER NUMPY PROJECT
Build a Satellite Data Processing System (Using Only NumPy)

📦 DATA DESCRIPTION

You receive:

365 days of data

24 hours per day

5 sensors

So shape should be:

(365, 24, 5)

Each value = temperature reading.

📦 DATA DESCRIPTION

You receive:

365 days of data

24 hours per day

5 sensors

So shape should be:

(365, 24, 5)

Each value = temperature reading.



🔥 STEP 1 — Create Dataset

Create a 3D array:

Use np.random.normal

Mean = 25

Std = 5

Shape = (365, 24, 5)

Concepts:

ndarray

dtype

shape

ndim

size

🔥 STEP 2 — Indexing & Slicing

Tasks:

Extract:

All data for day 100

All days at hour 12

Sensor 3 data for whole year

Get:

First 10 days

Last 7 days

Every alternate hour

Reverse data

Concepts:

Basic slicing

Step slicing

Negative indexing

Ellipsis (...)

🔥 STEP 3 — Data Cleaning

Simulate errors:

Randomly insert 500 NaN values

Insert 50 extreme outliers (value = 999)

Now:

Detect NaN values

Replace NaN with column mean

Detect outliers (> 3 std)

Replace outliers with median

Concepts:

np.isnan

np.where

np.mean(axis=)

np.std

Boolean masking

Broadcasting

🔥 STEP 4 — Reshaping & Transformations

Convert:

From:

(365, 24, 5)

To:

(365, 120)

Then:

Flatten entire dataset

Reshape back

Swap axes

Transpose

Concepts:

reshape

flatten

ravel

swapaxes

transpose

🔥 STEP 5 — Aggregations

Compute:

Daily average temperature

Hourly average temperature

Sensor-wise yearly average

Global max/min

Day with highest average temperature

Concepts:

axis

argmax

argmin

sum

mean

max

min

🔥 STEP 6 — Sorting & Ranking

Sort temperatures for day 200

Get indices of top 10 hottest readings

Rank sensors by average temperature

Concepts:

np.sort

np.argsort

Fancy indexing

🔥 STEP 7 — Broadcasting Practice

Subtract sensor-wise mean from entire dataset

Normalize each sensor independently

Add correction factor array shape (5,) to dataset

Concepts:

Broadcasting rules

Dimension expansion

np.newaxis

🔥 STEP 8 — Stacking & Splitting

Split year into:

Q1

Q2

Q3

Q4

Stack first two quarters together

Concatenate along different axes

Concepts:

np.split

np.vstack

np.hstack

np.concatenate

🔥 STEP 9 — Linear Algebra

For a selected day:

Compute covariance matrix between sensors

Compute correlation matrix

Find eigenvalues & eigenvectors

Concepts:

np.cov

np.corrcoef

np.linalg.eig

Matrix multiplication

🔥 STEP 10 — Performance Test

Create a large array (10 million elements).

Compute:

Square using Python loop

Square using NumPy vectorization

Compare execution time.

You’ll understand why NumPy is powerful.

🔥 STEP 11 — Memory Understanding (Very Important)

Test:

a = np.arange(10)
b = a[2:7]

Modify b.

Check if a changes.

Then try with .copy()

Understand:

Views vs Copies

Memory efficiency

🎯 FINAL OUTPUT

At the end you should produce a script:

satellite_numpy_project.py

That:

Generates

Cleans

Analyzes

Prints insights

Shows performance results