# 🛒 Online Retail Data Analysis using Hadoop MapReduce

This project performs large-scale data analysis on the [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail) using a custom-built Hadoop cluster and Python MapReduce programs. The goal is to preprocess the raw sales data and compute:

- Total number of transactions per country
- Minimum, maximum, and average **Quantity** of items bought per country
- Then we made the dataset 10x bigger and evaluate the performance on it

<br>

## 🚀 Technologies Used

- **Hadoop 3.3.4**
- **Python 3**
- **Hadoop Streaming**
- **HDFS & YARN**
- **Linux (Ubuntu)**

<br>

<br>

## 🧪 Dataset

- **Original Source:** UCI Machine Learning Repository  
- **Original Format:** Excel (.xlsx)  
- **Preprocessed Format:** Cleaned CSV with ~500,000 records

Preprocessing steps:
- Removed missing or corrupted rows
- Converted encoding to UTF-8
- Filled empty `CustomerID` with `0`, and `Country` with `"Unknown"`

<br>

## ⚙️ Hadoop Cluster Setup

- Built a **3-node cluster** (1 master, 2 workers)
- Configured environment variables and XML files in `/usr/local/hadoop/etc/hadoop/`
- Started HDFS and YARN services

See `setup/` folder for configuration files and commands.

<br>

## 🛠 MapReduce Jobs

### 1- Count Transactions per Country

- `mapper.py`: emits `(Country, 1)`
- `reducer.py`: sums counts per country

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapper.py,reducer.py \
    -input /input_clean/Online_Retail_Clean.csv \
    -output /output_country_count \
    -mapper mapper.py \
    -reducer reducer.py
```

### 2- Count Transactions per Country

- `quantity_mapper.py`: emits `(Country, quantity)`
- `quantity_reducer.py`: performs min, max, avg

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files quantity_mapper.py,quantity_reducer.py \
  -input /input_clean/Online_Retail_Clean.csv \
  -output /output_quantity_stats \
  -mapper quantity_mapper.py \
  -reducer quantity_reducer.py
```

