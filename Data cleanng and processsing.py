import pandas as pd

# 1. Load the CSV
df = pd.read_csv("complex_dirty_dataset.csv")

# 2. Show original shape and preview
print("Original shape:", df.shape)
print(df.head())

# 3. Drop completely empty rows
df.dropna(how='all', inplace=True)

# 4. Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# 5. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 6. Standardize column names: lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 7. Fill missing values and strip extra spaces in object columns
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())

# 8. Convert date columns if any (example shown, uncomment if applicable)
# df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# 9. Show cleaned shape and preview
print("\nCleaned shape:", df.shape)
print(df.head())

# 10. Save cleaned CSV
df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.csv'")
