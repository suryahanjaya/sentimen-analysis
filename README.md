Berikut versi **README GitHub (lebih visual, profesional, dan fokus hasil)** dalam bahasa Inggris. Siap langsung paste ke repo.

---

# 🚀 Indonesian Sentiment Analysis System

A high-performance sentiment analysis pipeline for Indonesian text using **Machine Learning and Deep Learning**.
Built with a multi-model approach to achieve **>92% accuracy**.

---

## 📌 Overview

This project classifies user-generated text into:

* Negative
* Neutral
* Positive

It combines:

* Traditional ML (SVM, Logistic Regression)
* Deep Learning (BiLSTM)
* Transformer (IndoBERT)

---

## 🧠 Key Features

* Large-scale dataset (>10,000 samples)
* Hybrid labeling + noise filtering
* Multiple training strategies
* Modular pipeline (train or load models independently)
* High accuracy across all models

---

## 🗂️ Dataset

* Source: Self-scraped (Google Play Store reviews)
* Size: 10,000+ samples
* Classes: Balanced (Negative, Neutral, Positive)

### Labeling Strategy

* Ratings used as base labels
* Noise filtering applied:

  * High rating + negative words → removed
  * Low rating + positive words → removed

---

## ⚙️ Preprocessing Pipeline

* Lowercasing
* Text cleaning (URL, emoji, symbols)
* Slang normalization
* Stopword removal
* Stemming (Indonesian)

---

## 🧪 Feature Engineering

### 🔹 Word-Level TF-IDF

* n-grams: (1,2)
* Captures semantic meaning

### 🔹 Character-Level TF-IDF

* n-grams: (3,7)
* Captures:

  * Typos
  * Slang
  * Informal language

---

## 🤖 Models

### 🔹 1. BiLSTM (Deep Learning)

* Embedding + Bidirectional LSTM
* Gradient clipping + dropout
* Strong contextual understanding

---

### 🔹 2. SVM + TF-IDF

* LinearSVC
* Optimized hyperparameters
* Strong baseline performance

---

### 🔹 3. Char N-gram + Logistic Regression

* Handles noisy and informal text
* High-dimensional sparse features

---

### 🔹 4. IndoBERT (Transformer)

* Model: `indobenchmark/indobert-base-p1`
* Fine-tuned for sentiment classification
* Context-aware representations

---

## 📊 Results

| Model      | Features      | Accuracy |
| ---------- | ------------- | -------- |
| BiLSTM     | Embedding     | **93%+** |
| SVM        | TF-IDF (word) | **92%+** |
| Char Model | TF-IDF (char) | ~91–92%  |
| IndoBERT   | Transformer   | ~90–92%  |

---

Pretrained model not included due to size limitations.
You can download IndoBERT from:
https://huggingface.co/suryahanjaya/sentimen-analysis/tree/main


## 📈 Performance Highlights

* Stable accuracy above **92%**
* Strong generalization across models
* Robust to noisy and informal text
* Efficient inference pipeline

---

## 🔍 Example Predictions

```text
Input  : "This app is very helpful and easy to use"
Output : POSITIVE

Input  : "Frequent errors and very slow"
Output : NEGATIVE

Input  : "It's okay, nothing special"
Output : NEUTRAL
```

---

## 🧩 Project Structure

```text
├── data/
├── models/
│   ├── lstm_full.pth
│   ├── svm_full.pkl
│   ├── indobert_model/
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## ⚡ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Train models

```python
LOAD_ONLY = False
```

---

### 3. Load trained models (skip training)

```python
LOAD_ONLY = True
```

---

## 🧠 Design Decisions

* SVM used as strong baseline
* LSTM for sequential understanding
* IndoBERT for contextual semantics
* Char-level features to handle noisy text

---

## 📌 Conclusion

This system demonstrates that combining:

* Classical ML
* Deep Learning
* Transformer models

can achieve **high accuracy and robustness** for Indonesian sentiment analysis.

---

## 📬 Future Improvements

* Ensemble learning (SVM + LSTM + BERT)
* Hyperparameter optimization (AutoML)
* Deployment as API / web app

---

## 👨‍💻 Author
2026
Surya Hanjaya
Informatics Engineering Student
