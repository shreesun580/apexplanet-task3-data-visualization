
import plotly.express as px 
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("../dataset/Cleaned_Superstore.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# Category-wise Sales for Plotly

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Interactive Category-wise Sales",
    color="Category"
)

fig.show()

fig.write_html("../python/interactive_category_sales.html")

# Scatter Plot - Sales vs Profit

plt.figure(figsize=(8,6))

plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()

# Interactive Scatter Plot

fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Category",
    hover_data=["Product Name", "Customer Name"],
    title="Interactive Sales vs Profit"
)

fig.show()

fig.write_html("../python/interactive_sales_profit.html")

# Histogram - Sales Distribution

plt.figure(figsize=(8,6))

plt.hist(df["Sales"], bins=30)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

import seaborn as sns
# Box Plot - Profit by Category

plt.figure(figsize=(8,6))

sns.boxplot(x="Category", y="Profit", data=df)

plt.title("Profit Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()

# Heatmap - Correlation Matrix

plt.figure(figsize=(8,6))

correlation = df[["Sales", "Profit", "Quantity", "Discount"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# Pair Plot

import seaborn as sns

pairplot_data = df[["Sales", "Profit", "Quantity", "Discount"]]

sns.pairplot(pairplot_data)

plt.show()

# Monthly Sales for Plotly

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Interactive Monthly Sales Trend"
)

fig.show()

fig.write_html("../python/interactive_monthly_sales_trend.html")