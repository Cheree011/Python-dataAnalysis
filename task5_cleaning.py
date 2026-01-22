import pandas as pd

df = pd.read_csv("students_performance.csv", sep=",", header=0)

print("\n First 5 rows of dataset:")
print(df.head())

print("\n Dataset information:")
print(df.info())

print("\n Missing values in each column:")
print(df.isnull().sum())

df["MathScore"] = df["MathScore"].fillna(df["MathScore"].mean())
df["ReadingScore"] = df["ReadingScore"].fillna(df["ReadingScore"].mean())
df["WritingScore"] = df["WritingScore"].fillna(df["WritingScore"].mean())

print("\n Missing values after cleaning:")
print(df.isnull().sum())

print("\n Shape before removing duplicates:", df.shape)
df = df.drop_duplicates()
print(" Shape after removing duplicates:", df.shape)

df["Passed"] = df["Passed"].astype("category")

print("\n Dataset info after datatype conversion:")
print(df.info())

df["AverageScore"] = (
    df["MathScore"] + df["ReadingScore"] + df["WritingScore"]
) / 3

print("\n Dataset with new column:")
print(df.head())

df.to_csv("cleaned_data.csv", index=False)

print("\n Data cleaning is done successfully!")
print(" Cleaned file saved as cleaned_data.csv")

