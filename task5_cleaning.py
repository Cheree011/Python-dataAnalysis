import pandas as pd

# -----------------------------
# Step 1: Read the dataset
# -----------------------------
df = pd.read_csv("students_performance.csv", sep=",", header=0)

# -----------------------------
# Step 2: View dataset
# -----------------------------
print("\n🔹 First 5 rows of dataset:")
print(df.head())

print("\n🔹 Dataset information:")
print(df.info())

# -----------------------------
# Step 3: Check missing values
# -----------------------------
print("\n🔹 Missing values in each column:")
print(df.isnull().sum())

# -----------------------------
# Step 4: Handle missing values
# -----------------------------
df["MathScore"] = df["MathScore"].fillna(df["MathScore"].mean())
df["ReadingScore"] = df["ReadingScore"].fillna(df["ReadingScore"].mean())
df["WritingScore"] = df["WritingScore"].fillna(df["WritingScore"].mean())

print("\n🔹 Missing values after cleaning:")
print(df.isnull().sum())

# -----------------------------
# Step 5: Remove duplicates
# -----------------------------
print("\n🔹 Shape before removing duplicates:", df.shape)
df = df.drop_duplicates()
print("🔹 Shape after removing duplicates:", df.shape)

# -----------------------------
# Step 6: Convert datatype
# -----------------------------
df["Passed"] = df["Passed"].astype("category")

print("\n🔹 Dataset info after datatype conversion:")
print(df.info())

# -----------------------------
# Step 7: Create new column
# -----------------------------
df["AverageScore"] = (
    df["MathScore"] + df["ReadingScore"] + df["WritingScore"]
) / 3

print("\n🔹 Dataset with new column:")
print(df.head())

# -----------------------------
# Step 8: Save cleaned dataset
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Data cleaning is done successfully!")
print("📁 Cleaned file saved as cleaned_data.csv")
