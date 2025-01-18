---
tags:
- chatbot
- evaluation
- first-aid
license: mit
language:
- en
metrics:
- precision
- recall
- f1
---

# 🏥 First Aid Assistant - Evaluation Results

This repository contains the **evaluation results** for the `First Aid Assistant` chatbot, tested on **10 first-aid-related questions**.

## 📢 **Ownership and Attribution**
> **⚠️ Disclaimer:**  
> - The **First Aid Assistant chatbot** is the property of **Mysore Medical College and Research Institute**.  
> - The uploaded **FIRST AID PDF** that forms the basis of the Retrieval-Augmented Generation (RAG) process is an **official course material** and the property of **Mysore Medical College and Research Institute**.

---

## 📊 Evaluation Metrics
The chatbot's responses were evaluated using **Precision, Recall, F1 Score, and Cosine Similarity**.

| Metric    | Score  |
|-----------|--------|
| Precision | **1.00** |
| Recall    | **1.00** |
| F1 Score  | **1.00** |

> 🔍 Full evaluation results are available in **[`evaluation_results.txt`](./evaluation_results.txt)**.

## 📈 Evaluation Visualization
Below is a graphical representation of the chatbot’s performance.

![Evaluation Graph](./evaluation_plot.png)

---

## 📖 **Evaluation Method**
- Used **TF-IDF + Cosine Similarity** to compare chatbot responses with expected answers.
- Evaluated on **10 first-aid-related questions** covering:
  - High fever in infants
  - Low blood sugar treatment
  - First-aid steps for burns, seizures, choking, etc.
- **Expected answers** were sourced from medical literature.

---

## 📥 **Download & Re-Evaluate**
You can **re-evaluate the chatbot** by running the following:

```
git clone https://huggingface.co/DrSyedFaizan/First_Aid_Assistant_Evaluation
cd First_Aid_Assistant_Evaluation
python eval.py  # Runs evaluation on the chatbot
```

## 📌 **Author**
👨‍⚕ **Dr. Syed Faizan** | 🏥 Healthcare AI & Data Science  
🔗 **Hugging Face Repo**: [First_Aid_Assistant_Evaluation](https://huggingface.co/DrSyedFaizan/First_Aid_Assistant_Evaluation)
