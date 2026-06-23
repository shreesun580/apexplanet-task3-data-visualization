# ApexPlanet Data Analytics Internship - Task 3

## Data Visualization and Dashboard

### Project Overview

This project is a part of the **Data Analytics Internship** offered by **ApexPlanet Software Pvt. Ltd.**

The objective of this task is to analyze the Superstore dataset and present meaningful business insights using Python visualization libraries and Microsoft Power BI.

---

## Objectives

- Create visualizations using Python
- Analyze sales and profit trends
- Build an interactive Power BI dashboard
- Create DAX measures for business KPIs
- Present business insights through charts and filters

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Microsoft Power BI

---

## Dataset

- Superstore Dataset (Cleaned)
- Rows: 9994
- Columns: 21

---

## Python Visualizations

The following visualizations were created using Python:

- Monthly Sales Trend (Line Chart)
- Category-wise Sales (Bar Chart)
- Sales vs Profit (Scatter Plot)
- Sales Distribution (Histogram)
- Profit Distribution by Category (Box Plot)
- Correlation Heatmap
- Pair Plot
- Interactive Plotly Line Chart
- Interactive Plotly Bar Chart
- Interactive Plotly Scatter Plot

---

## Power BI Dashboard

The interactive dashboard includes:

- Total Sales KPI
- Total Profit KPI
- Total Quantity KPI
- Profit Margin KPI
- Monthly Sales Trend
- Category-wise Sales
- Sales by Region (Donut Chart)
- Sales by State (Map)
- Top 10 Products by Sales
- Interactive Slicers
  - Region
  - Category
  - Segment

---

## DAX Measures

```DAX
Total Sales = SUM('Cleaned_Superstore'[Sales])

Total Profit = SUM('Cleaned_Superstore'[Profit])

Profit Margin % =
DIVIDE(
    SUM('Cleaned_Superstore'[Profit]),
    SUM('Cleaned_Superstore'[Sales])
)
```

---

## Business Insights

- Technology generated the highest sales.
- The West region contributed the highest revenue.
- Sales and Profit show a positive relationship.
- Discounts significantly impact profitability.
- The dashboard enables interactive analysis using slicers.

---

## Folder Structure

```
apexplanet-task3/
│
├── dataset/
├── python/
├── powerbi/
├── screenshots/
├── README.md
└── requirements.txt
```

---

## Learning Outcomes

Through this task, I learned:

- Data visualization using Python
- Creating interactive charts with Plotly
- Building dashboards in Microsoft Power BI
- Creating DAX measures
- Designing interactive business dashboards
- Presenting business insights visually

---

## Author

**Shree Vathy**

Data Analytics Intern

ApexPlanet Software Pvt. Ltd.
