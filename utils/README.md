# Preprocessing Scripts

These Python scripts prepare the Online Retail dataset for Hadoop MapReduce processing.

## 🧹 `cleaning.py`

Cleans the original `Online_Retail.xlsx` dataset by:
- Removing rows with missing or invalid fields
- Converting encoding to UTF-8
- Filling missing `CustomerID` with `0` and empty `Country` with `"Unknown"`
- Exporting to a clean CSV file for HDFS input

### Output:
`Online_Retail_Clean.csv`

> ⚠️ This step is essential before uploading to HDFS. The raw file may cause job failure.

---

## 📈 `big_data.py`

Generates a larger dataset by repeating the cleaned data multiple times (default: 10×).

### Input:
`Online_Retail_Clean.csv`

### Output:
`OnlineRetail_Large.csv`

Use this version for testing performance under larger data volume in your Hadoop cluster.

---

## How to Run

```bash
python cleaning.py
python big_data.py  # Optional for stress testing
