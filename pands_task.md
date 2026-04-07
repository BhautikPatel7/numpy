Project: E-commerce Sales Data Analysis

You are analyzing an online store dataset.

📁 Dataset columns (you can create CSV manually or I can generate it for you):
order_id, date, customer, city, product, category, price, quantity, payment_method

🧠 TASK 1 — Load & Inspect Data
Concepts:
read_csv()
head(), tail()
info(), describe()
Goal:
df = pd.read_csv("sales.csv")

✔ Understand structure of data

🧹 TASK 2 — Data Cleaning
Concepts:
Handling missing values (isnull, fillna, dropna)
Type conversion (astype)
Rename columns
Goal:

✔ Clean inconsistent data

🔍 TASK 3 — Filtering Data
Concepts:
Boolean indexing
Multiple conditions (&, |)
Example:
df[df["city"] == "Ahmedabad"]
df[(df["price"] > 500) & (df["category"] == "Electronics")]
📊 TASK 4 — Create New Columns
Concepts:
Column operations
apply(), lambda
Goal:
df["total_amount"] = df["price"] * df["quantity"]
📅 TASK 5 — Date Handling
Concepts:
to_datetime()
Extract month, year
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
📈 TASK 6 — Grouping & Aggregation
Concepts:
groupby()
sum(), mean(), count()
Example:
df.groupby("category")["total_amount"].sum()

🔄 TASK 7 — Sorting & Ranking
Concepts:
sort_values()
nlargest()
Goal:

✔ Top 5 selling products

🔗 TASK 8 — Merge & Join
Concepts:
merge()
Add:

Create another dataset:

product, supplier, cost_price

✔ Merge with main dataset




📉 TASK 9 — Pivot Tables
Concepts:
pivot_table()
pd.pivot_table(df, values="total_amount", index="city", columns="category", aggfunc="sum")

✔ Multi-dimensional analysis

📊 TASK 10 — Visualization
Concepts:
plot()
Bar chart, line chart
df.groupby("month")["total_amount"].sum().plot(kind="line")
🧩 FINAL PROJECT OUTPUT

At the end, you should be able to answer:

✔ Which city has highest sales?
✔ Which category performs best?
✔ Monthly revenue trend
✔ Top customers
✔ Most used payment method

🔥 Bonus (Advanced)
loc vs iloc
value_counts()
drop_duplicates()
Performance optimization