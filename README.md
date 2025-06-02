# Email/SMS Spam-Ham Classification
<img width="1392" alt="Screenshot 2025-06-02 at 3 24 28 PM" src="https://github.com/user-attachments/assets/0347955e-8270-4838-896c-b9e6006ad1b1" />



A Data Science & Machine Learning-powered Flask Web Application that classifies Email/SMS messages as either **Spam** or **Ham** (Not Spam).

---

## 📌 Project Overview

This project demonstrates how **Natural Language Processing (NLP)** and **Machine Learning** can be used to classify text messages. It includes data cleaning, EDA, feature engineering, model building, and deployment in a real-time Web Application.

---

## 🧩 Problem Statement

With the ever-growing volume of digital communication, especially SMS and Email, distinguishing between legitimate messages and unwanted spam is critical. Spam messages often carry scams, phishing links, or irrelevant promotions that compromise user experience and safety.

---

## 💡 Why This Project Is Useful

This project provides an end-to-end solution for spam detection, from data preprocessing and feature engineering to deploying a real-time Flask Web Application. It helps automate message classification, enhancing communication security and saving users from spam clutter.

---

## 📦 Dataset & Preparation

- **Source**: [Kaggle SMS Spam Collection Dataset](https://www.kaggle.com/datasets/satyajeetbedi/email-hamspam-dataset)
- **Initial Shape**: 5572 rows × 5 columns
- **Preprocessing**:
  - Dropped irrelevant columns: `Unnamed: 2`, `Unnamed: 3`, `Unnamed: 4`
  - Renamed: `v1` → `label`, `v2` → `message`
  - Removed 403 duplicate rows

---

## 📊 Exploratory Data Analysis (EDA)

- **Class Distribution**:
  - **Ham**: 87.4%
  - **Spam**: 12.6%
- **Feature Creation**:
  - `num_of_char`: Total characters
  - `num_of_words`: Total words (`nltk.tokenize.word_tokenize`)
  - `num_of_sentences`: Sentence count
- **Visualizations**:
  - Pie chart of class distribution
  - Bar charts & histograms for custom features
  - Pairplot for feature relationships
  - Word frequency bar plots for both spam and ham
- Dropped temporary features after insights

---

## 🧹 Text Preprocessing

Implemented a custom text transformation pipeline:

- Lowercasing
- Tokenization with `nltk`
- Stopword removal (including HTML tags, emojis, punctuation, digits)
- Lemmatization & Stemming using `PorterStemmer`
- Dropped 87 duplicates after text transformation

---

## ⚙️ Feature Engineering

- Generated word clouds for:
  - **Spam** (e.g., "free", "win", "txt", "offer")
  - **Ham** (e.g., "love", "ok", "come", "home")
- Vectorized text using `CountVectorizer`
- Applied `StratifiedShuffleSplit` to ensure balanced train/test splits

---

## 🤖 Model Building & Evaluation

Tested the following classifiers:

- `MultinomialNB`
- `RandomForestClassifier`
- `SVC`
- `KNeighborsClassifier`

**Evaluation Metrics**: Accuracy, Precision, Confusion Matrix

### 📋 Results Summary:

```
| Algorithm | Training_Accuracy | Test_Accuracy | Training_Precision | Test_Precision |
|-----------|-------------------|---------------|---------------------|----------------|
| MNB       | 0.9909            | 0.9715        | 0.9676              | 0.8750         |
| RF        | 1.0000            | 0.9626        | 1.0000              | 1.0000         |
| SVC       | 0.9956            | 0.9607        | 1.0000              | 0.9885         |
| KNN       | 0.9262            | 0.9105        | 1.0000              | 1.0000         |
```

✅ **Best Model**: `RandomForestClassifier`

---

## 🚀 Deployment

- Saved final model and vectorizer using `pickle`
- Deployed using **Flask** for real-time predictions
- Users can input a message and receive immediate spam/ham classification

---

## 🛠️ Technologies Used

- **Programming**: Python
- **Libraries**: Pandas, Numpy, NLTK, Scikit-learn
- **Visualization**: Matplotlib, Seaborn, WordCloud
- **Web Framework**: Flask
