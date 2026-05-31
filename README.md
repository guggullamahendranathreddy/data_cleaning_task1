# Customer Personality Analysis: Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing the Customer Personality Analysis dataset obtained from Kaggle. The objective was to transform raw data into a clean, structured, and analysis-ready dataset using Python and Pandas.

The dataset contained missing values, inconsistent formats, and required preprocessing before analysis.

---

## Objective

The main objective of this project is to:

* Identify missing values
* Handle missing values appropriately
* Remove duplicate records
* Standardize column names
* Convert date columns into proper datetime format
* Validate data types
* Prepare the dataset for further analysis

---

## Dataset Information

Dataset: Customer Personality Analysis

Source: Kaggle

The dataset contains customer demographic information, purchasing behavior, and campaign response data.

Key Columns:

* ID
* Year_Birth
* Education
* Marital_Status
* Income
* Kidhome
* Teenhome
* Dt_Customer
* Recency
* Product Spending Features

---

## Tools Used

* Python
* Pandas
* NumPy
* VS Code

---

## Data Cleaning Steps Performed

### 1. Missing Value Analysis

Missing values were identified using:

```python
df.isnull().sum()
```

The Income column contained missing values.

### 2. Missing Value Treatment

Missing values in numerical columns were replaced using the median value.

Missing values in categorical columns were replaced using the mode value.

### 3. Duplicate Record Removal

Duplicate records were identified and removed using:

```python
df.drop_duplicates()
```

### 4. Column Name Standardization

Column names were converted to:

* Lowercase
* Underscore format
* Consistent naming convention

### 5. Date Conversion

The Dt_Customer column was converted into datetime format using Pandas.

### 6. Data Type Validation

Data types were checked and verified to ensure consistency.

### 7. Dataset Export

The cleaned dataset was exported as:

```text
cleaned_data.csv
```

---

## Results

Successfully completed:

* Missing value handling
* Duplicate removal
* Column standardization
* Date conversion
* Data type verification
* Dataset preparation for analysis

---

## Project Structure

Data-cleaning-task-1/

├── raw_data.csv

├── cleaned_data.csv

├── Data_cleaning.py

├── README.md

├── report.pdf

├── requirements.txt

└── screenshots/

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python Data_cleaning.py
```

Output:

```text
cleaned_data.csv
```

---

## Conclusion

The Customer Personality Analysis dataset was successfully cleaned and transformed into an analysis-ready dataset. Data quality issues such as missing values, duplicates, and formatting inconsistencies were resolved using Python and Pandas.
