# 🧹 Data-Cleaning-Tool-for-SLM-Models  
### *A High-Performance Text Preprocessing Pipeline for Small Language Models*

The **Data Cleaning Pipeline for SLM Models** is a powerful Python-based system designed to transform raw, noisy text data into **clean, structured, and model-ready datasets**. Built with a focus on **NLP and AI workflows**, this pipeline ensures that your data is optimized for training **Small Language Models (SLMs)**, chatbots, and other intelligent systems.

Raw text from sources like web scraping often contains inconsistencies such as HTML tags, special characters, and irrelevant noise. This project eliminates those issues and delivers **high-quality, normalized text** ready for machine learning.

---

<p align="center">
  <strong>⚡ CleanText Pipeline</strong><br/>
  <em>From Raw Noise → Intelligent Data</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/NLP-Preprocessing-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Regex-Cleaning-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lightweight-Fast-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square"/>
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Pipeline Architecture](#-pipeline-architecture)
- [Core Processing Steps](#-core-processing-steps)
- [Workflow](#-workflow)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Use Cases](#-use-cases)
- [Future Enhancements](#-future-enhancements)

---

## 🌟 Overview

This project focuses on building a **robust and reusable text preprocessing pipeline** tailored for AI and NLP applications.

It solves a critical problem in machine learning:

> ❗ *“Garbage in → Garbage out”*

By cleaning and normalizing raw datasets, this system ensures:

- High-quality training data  
- Reduced noise and redundancy  
- Improved model accuracy  
- Consistent and structured input  

---

## 🎯 Objectives

- 🧹 Remove unwanted noise and symbols  
- 🔤 Normalize and standardize text  
- 🧠 Improve dataset quality for NLP models  
- 🔁 Build a reusable preprocessing pipeline  
- ⚡ Optimize data for SLM training  

---

## ✨ Key Features

| Feature | Description |
|--------|------------|
| 🧹 **Advanced Cleaning** | Removes HTML tags, URLs, emails, and unwanted characters |
| 🔤 **Text Normalization** | Converts text to lowercase and standardizes encoding |
| 🧠 **Smart Filtering** | Eliminates short, repetitive, and low-quality text |
| ⚡ **Efficient Processing** | Lightweight and fast pipeline using Python |
| 🤖 **Model-Ready Output** | Clean text suitable for NLP, chatbots, and SLM training |

---

## 🛠 Technology Stack

| Component | Technology | Purpose |
|----------|-----------|--------|
| **Language** | Python 3.x | Core processing logic |
| **Regex Engine** | `re` | Pattern-based text cleaning |
| **Unicode Handling** | `unicodedata` | Text normalization |
| **Utilities** | `string` | Character filtering |
| **Optional NLP** | `nltk` | Tokenization & advanced preprocessing |

---

## 🏗 Pipeline Architecture

```
Raw Data → Cleaning → Normalization → Filtering → Clean Dataset
```

### Processing Layers

1. **Input Layer** → Raw text ingestion  
2. **Cleaning Layer** → Noise & unwanted data removal  
3. **Normalization Layer** → Standardization of text  
4. **Filtering Layer** → Quality-based data filtering  
5. **Output Layer** → Clean dataset ready for ML  

---

## 📜 Core Processing Steps

### 🧹 Remove HTML Tags
- Strips `<tags>` and markup content  

### 🌐 Remove URLs & Emails
- Eliminates hyperlinks and email patterns  

### 🔤 Normalize Text
- Unicode → ASCII conversion  
- Lowercase transformation  

### ⚙ Regex-Based Cleaning
- Removes special characters and symbols  

### 🧠 Smart Filtering
- Removes:
  - Very short sentences  
  - Repetitive/noisy text  
  - Low-quality content  

---

## 🔄 Workflow

```
1. Load raw text dataset
2. Remove HTML tags
3. Remove URLs and emails
4. Normalize unicode characters
5. Clean special characters
6. Convert text to lowercase
7. Remove extra whitespace
8. Filter low-quality text
9. Save cleaned dataset
```

---

## 📁 Project Structure

```
Data-Cleaning-SLM/
│
├── cleaning_script.py        # Core preprocessing pipeline
├── input_data.txt            # Raw input dataset
├── cleaned_output.txt        # Final cleaned output
```

---

## ⚡ How to Run

### Prerequisites
- Python 3.x installed  

---

### 1️⃣ Install Dependencies (Optional)
```bash
pip install nltk
```

### 2️⃣ Run the Script
```bash
python cleaning_script.py
```

### 3️⃣ Output File
```
cleaned_output.txt
```

---

## 🎯 Use Cases

- 🧠 Training Small Language Models (SLMs)  
- 🤖 Chatbot dataset preparation  
- 📄 NLP preprocessing pipelines  
- 🔍 Research data cleaning  
- 🌐 Web scraped data processing  

---

## 🌟 Highlights

✔ Lightweight and fast pipeline  
✔ Designed for real-world noisy datasets  
✔ Easy to extend and customize  
✔ Focused on AI/NLP workflows  
✔ Clean, modular implementation  

---

## 🔮 Future Enhancements

- 🧠 Stopword removal integration  
- 📊 Tokenization & lemmatization  
- 🌐 Integration with web scraping tools  
- ⚡ Batch processing for large datasets  
- 🤖 Direct ML pipeline integration  

---

## 👨‍💻 Author

**Vaibhav Sharma**  
*AI Developer | Data Pipeline Engineer*

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

> **High-quality data is the foundation of powerful AI systems.**

This project ensures your dataset is **clean, consistent, and optimized** for training intelligent models 🚀

---

<p align="center">
  Built with ❤️ using Python & NLP techniques<br/>
  <strong>CleanText Pipeline</strong> — Powering Smarter AI Models
</p>
