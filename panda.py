import pandas as pd

print("Soemthing")
df = pd.read_csv("sales.csv")

# print(df.head())
# print(df.tail())
# print(df.describe())
print(df.columns)
print(df.shape)
# print(df.info())



# df["quantity"].fillna(1, inplace=True)
df.dropna(inplace=True)
# print(df.isnull().sum())
# print(df.info())

print(df.dtypes)
df["date"] = pd.to_datetime(df["date"] )
print(df.dtypes)


df.rename(columns={
    "order_id":"OrderId",
    "payment_method":"paymentMethod",
}, inplace=True)

print(df.columns)

df.drop_duplicates(inplace=True)

df["city"] = df["city"].str.lower()
df["customer"] = df["customer"].str.lower()

df.info()
df.isnull().sum()



ahmd = df[df["city"] == "Ahmedabad"]
print(ahmd)

filt = df[(df["price"] > 500) | (df["category"] == "Electronics")]
print(filt)


df[~(df["city"] == "Ahmedabad")]


print(df[df["price"] > 20000])

df[(df["category"] == "Fashion") & (df["city"] == "Mumbai")]

print(df[df["city"].isin(["Ahmedabad", "Delhi"])])

print(df[df["customer"].str.contains("shah", case=False)])

print(df[df["city"] == "Ahmedabad"][["customer", "price"]])

print(df.loc[df["city"] == "Ahmedabad", ["customer", "price"]])


df["total_amount"] = df["price"] * df["quantity"]
print(df.columns)

df["total_amount"] = df.apply(lambda row: row["price"] * row["quantity"], axis=1)
df["total_items"] = df.apply(lambda row: row["price"] * row["quantity"], axis=1)

df["high_value"] = df["total_amount"].apply(lambda x: "Yes" if x > 20000 else "No")

# df["final_price"] = df["price"] - df["discount"]

df["price"] = df["price"] * 1.05

print(df.head())

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()
df["weekday"] = df["date"].dt.weekday

df[df["date"] > "2025-02-01"]
df[df["month"] == 1]

df.groupby("month")["total_amount"].sum()
print(df.groupby("category")["OrderId"].count())
print(df.groupby("category")["total_amount"].mean())

# print(df.groupby("category")["total_amount"].sum())
print(df.head())
print(df.groupby(["city", "category"])["total_amount"].sum())
print(df.groupby("category")["total_amount"].agg(["sum", "mean", "count"]))

df.groupby("category")["total_amount"].sum().reset_index()
