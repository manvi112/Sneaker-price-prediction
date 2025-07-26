import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sample_dataset.csv")

print("Shape of dataset:", df.shape)
print("\nColumn Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nStatistical Summary:\n", df.describe())

with open("eda_summary.txt", "w") as f:
    f.write(f"Shape of dataset: {df.shape}\n\n")
    f.write("Column Types:\n")
    f.write(str(df.dtypes))
    f.write("\n\nMissing Values:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\nStatistical Summary:\n")
    f.write(str(df.describe()))

plt.figure(figsize=(8,5))
sns.histplot(df['Sale Price'], kde=True)
plt.title('Sale Price Distribution')
plt.xlabel('Price')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('sale_price_distribution.png')
plt.close()

if 'Brand' in df.columns:
    top_brands = df['Brand'].value_counts().head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_brands.index, y=top_brands.values)
    plt.title('Top 10 Brands in Dataset')
    plt.xlabel('Brand')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_brands.png')
    plt.close()

print("EDA report and plots generated successfully")
