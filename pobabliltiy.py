import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)


n = 1000

click = np.random.binomial(1, 0.4, n)
# print(click)

purchase = []

for c in click:
    if c == 0:
        purchase.append(np.random.binomial(1,0.1))
    if c == 1:
        purchase.append(np.random.binomial(1, 0.1))


print(len(purchase))
print(len(click))

# print(purchase)

df = pd.DataFrame({
    "click": click,
    "purchase": purchase
})


print(df.head())

p_click = df["click"].mean()
print(p_click, "p_click")

p_purchase = df["purchase"].mean()
print(p_purchase, "p_purchase")

p_joint = len(df[(df.click == 1) & (df.purchase == 1)]) / n

print(p_joint, "p_joint")

# p(purchase/ click) 

p_purchace_given_click =  len(df [ (df["click"] == 1) & (df["purchase"] == 1)]) / len(df[df["click"] == 1])
print(p_purchace_given_click, "p_purchace_given_click")


# Now find p(click/ purchase)

p_click_given_purchase = p_joint / p_purchase
print(p_click_given_purchase, "p_click_given_purchase")


mean_purchase = df['purchase'].mean()
print(mean_purchase, "mean_purchase")

mean_click = df['click'].mean()
print(mean_click, "mean_click")


var_purchase = df["purchase"].var()
print(var_purchase, "var_purchase")


# df['purchase'].value_counts().plot(kind='bar')
# plt.title("Purchase Distribution")
# plt.show()

sample_means = []


for i in range(1000):
    sampels = df["purchase"].sample(50)
    sample_means.append(sampels.mean())

plt.hist(sample_means, bins=30)
print(sample_means)
plt.title("CLT")
# plt.show() 


def predict(click):
    if click == 1:
        return p_purchace_given_click
    else:
        return 0.1  # baseline
    
print(predict(1))
print(predict(0))


import statsmodels.api as sm

clicks = 200
n = 1000

ci_low, ci_high = sm.stats.proportion_confint(clicks, n, alpha=0.05)
print(ci_low, ci_high)


from statsmodels.stats.proportion import proportions_ztest

clicks = [200, 240]
n = [1000, 1000]

stat, p = proportions_ztest(clicks, n)
print(p)