# Data-Cleaning-Tool-for-SLM-Models

# 🧹 Data Cleaning Pipeline for Training SLM (Small Language Model)

### Advanced Text Preprocessing & Noise Removal System in Python

---

## 📌 Overview

This project focuses on building a **robust text cleaning and preprocessing pipeline** designed specifically for preparing high-quality datasets for training **Small Language Models (SLMs)**.

Raw text collected from sources like web scraping often contains:

* ❌ Noise
* ❌ Special characters
* ❌ HTML tags
* ❌ Irrelevant symbols

This system transforms such raw data into **clean, structured, and model-ready text**.

---

## 🎯 Objectives

* Remove unwanted characters and noise from text
* Normalize and standardize textual data
* Improve dataset quality for ML/NLP training
* Build a reusable preprocessing pipeline

---

## 🚀 Key Features

### 🧹 Advanced Text Cleaning

* Removes:

  * Special characters
  * HTML tags
  * URLs
  * Emails
* Filters unwanted symbols using regex

---

### 🔤 Text Normalization

* Converts text to lowercase
* Removes extra whitespace
* Standardizes encoding (ASCII normalization)

---

### 🧠 Smart Filtering

* Removes:

  * Very short sentences
  * Repetitive/noisy text
  * Low-quality data

---

### ⚡ Model-Ready Output

* Produces clean text suitable for:

  * NLP models
  * SLM training
  * Chatbots

---

## 🏗️ Project Structure

```id="cleanstruct"
Data-Cleaning-SLM/
│
├── cleaning_script.py        # Core cleaning logic
├── input_data.txt            # Raw dataset
├── cleaned_output.txt        # Processed dataset
```

---

## 🖥️ Tech Stack

### 🐍 Language

* Python

### 📦 Libraries Used

* `re` → Regular expressions for cleaning
* `unicodedata` → Text normalization
* `string` → Character handling
* (Optional) `nltk` → Tokenization

---

## 🔄 Working Pipeline

```id="cleanflow"
1. Load raw text data
2. Remove HTML tags
3. Remove URLs and emails
4. Normalize unicode characters
5. Remove special symbols
6. Convert to lowercase
7. Remove extra spaces
8. Filter low-quality text
9. Save cleaned output
```

---

## 📜 Core Logic Explained

### 📌 Step 1: Remove HTML Tags

* Strips `<tags>` from raw text

---

### 📌 Step 2: Remove URLs & Emails

* Cleans hyperlinks and email patterns

---

### 📌 Step 3: Normalize Text

* Converts Unicode → ASCII
* Ensures consistent encoding

---

### 📌 Step 4: Regex Cleaning

* Removes unwanted characters using patterns

---

### 📌 Step 5: Filtering

* Keeps only meaningful sentences
* Removes noise and junk data

---

## ⚡ How to Run

### 1️⃣ Install Dependencies (if any)

```bash id="instclean"
pip install nltk
```

---

### 2️⃣ Run Script

```bash id="runclean"
python cleaning_script.py
```

---

### 3️⃣ Output

* Cleaned text will be saved in:

```id="outclean"
cleaned_output.txt
```

---

## 📊 Use Cases

* 🧠 Training Small Language Models (SLM)
* 🤖 Chatbot dataset preparation
* 📄 NLP preprocessing pipelines
* 🔍 Data cleaning for research
* 🌐 Web scraped data processing

---

## 🌟 Highlights

✔ Clean and reusable pipeline
✔ Focused on NLP/AI use cases
✔ Handles real-world noisy data
✔ Easy to extend and customize
✔ Lightweight and efficient

---

## 🧩 Future Enhancements

* 🧠 Add stopword removal
* 📊 Add tokenization & lemmatization
* 🌐 Integrate with web crawlers
* ⚡ Batch processing for large datasets
* 🤖 Direct pipeline for model training

---

## 👨‍💻 Author

**Vaibhav Sharma**

* AI & Data Enthusiast
* Focused on building intelligent data pipelines

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

High-quality data is the backbone of any AI model.
This project ensures your dataset is **clean, consistent, and ready for training powerful language models 🚀**

---
