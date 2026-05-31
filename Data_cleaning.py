import pandas as pd

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("data/raw_data.csv")

print("=" * 60)
print("DATA CLEANING AND PREPROCESSING")
print("=" * 60)

print("\nOriginal Shape:", df.shape)

# =====================================
# DATASET OVERVIEW
# =====================================

print("\nDataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# =====================================
# MISSING VALUES BEFORE CLEANING
# =====================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# =====================================
# HANDLE INCOME COLUMN
# =====================================

df["Income"] = pd.to_numeric(
    df["Income"],
    errors="coerce"
)

df["Income"] = df["Income"].fillna(
    df["Income"].median()
)

# =====================================
# HANDLE OTHER MISSING VALUES
# =====================================

for col in df.columns:

    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(
            df[col].median()
        )

    else:
        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

# =====================================
# REMOVE DUPLICATES
# =====================================

duplicates = df.duplicated().sum()

print("\nDuplicate Records Found:", duplicates)

df = df.drop_duplicates()

# =====================================
# STANDARDIZE COLUMN NAMES
# =====================================

df.columns = (
    df.columns
      .str.lower()
      .str.strip()
      .str.replace(" ", "_")
)

# =====================================
# CONVERT DATE COLUMN
# =====================================

df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    dayfirst=True,
    errors="coerce"
)

# Fill missing dates if any

if df["dt_customer"].isnull().sum() > 0:
    df["dt_customer"] = df["dt_customer"].fillna(
        df["dt_customer"].mode()[0]
    )

# =====================================
# CLEAN TEXT COLUMNS
# =====================================

for col in df.select_dtypes(include="object"):
    df[col] = df[col].astype(str).str.strip()

# =====================================
# DATA TYPES CHECK
# =====================================

print("\nData Types:")
print(df.dtypes)

# =====================================
# MISSING VALUES AFTER CLEANING
# =====================================

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# =====================================
# SAVE CLEAN DATASET
# =====================================

df.to_csv(
    "data/cleaned_data.csv",
    index=False
)

# =====================================
# FINAL SUMMARY
# =====================================

print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

print(f"Original Rows : {2240}")
print(f"Final Rows    : {df.shape[0]}")
print(f"Columns       : {df.shape[1]}")

print("\nCleaning Steps Performed:")
print("✓ Missing values handled")
print("✓ Income column cleaned")
print("✓ Duplicate records removed")
print("✓ Column names standardized")
print("✓ Date column converted")
print("✓ Text values cleaned")
print("✓ Data types verified")
print("✓ Clean dataset exported")

print("\nPreview of Cleaned Dataset:")
print(df.head())

print("\nCleaning Completed Successfully!")