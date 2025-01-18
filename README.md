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
# 🏥 First Aid Tutor

![First Aid Tutor](https://github.com/SYEDFAIZAN1987/First-Aid-Tutor/blob/main/RAGGPT%20UI.png)

## 📘 About the Project
First Aid Tutor is an AI-powered chatbot designed to evaluate the efficacy of Retrieval-Augmented Generation (RAG) in medical education for paramedical and medical students. It provides first-aid guidance based on medical literature to assess learning outcomes and response accuracy.



This repository contains the **codebase** for the `First Aid Assistant` chatbot, tested on **10 first-aid-related questions**.

## 📢 **Ownership and Attribution**
> **⚠️ Disclaimer:**  
> - The **First Aid Assistant chatbot** is the property of **Mysore Medical College and Research Institute**.  
> - The uploaded **FIRST AID PDF** that forms the basis of the Retrieval-Augmented Generation (RAG) process is an **official course material** and the property of **Mysore Medical College and Research Institute**.

---
# 🚑 First Aid Tutor - RAG Chatbot

The **First Aid Tutor** is a **Retrieval-Augmented Generation (RAG)** chatbot designed to assist **medical and paramedical students** in learning **first-aid protocols**. It is strictly trained on a **verified first-aid guide** and only provides information present in the **First Aid PDF**.

## 🎯 Features
✅ **Evidence-Based Responses** - The chatbot only retrieves and generates answers based on the **First Aid PDF**.  
✅ **User-Friendly Interface** - Developed using **Gradio**, featuring a modern and intuitive UI.  
✅ **Medical Education Research** - Used for evaluating **RAG efficacy in medical education**.  

## 🔬 How It Works
- Uses **TF-IDF + Cosine Similarity** for retrieving contextually relevant information.  
- Queries are answered based strictly on **verified medical content**.  
- Integrated with **Gradio UI** for an easy-to-use chatbot experience.  

## 📌 Live Demo
🚀 **[Try the First Aid Tutor Chatbot](https://huggingface.co/spaces/DrSyedFaizan/First_Aid_Assistant)**

## 📥 How to Run Locally
You can run the chatbot locally using the following commands:

```bash
git clone https://github.com/SYEDFAIZAN1987/First-Aid-Tutor
cd First-Aid-Tutor
pip install -r requirements.txt
python raggpt.py  # Runs the chatbot

## 📊 Evaluation Metrics
The chatbot's responses were evaluated using **Precision, Recall, F1 Score, and Cosine Similarity**.

| Metric    | Score  |
|-----------|--------|
| Precision | **1.00** |
| Recall    | **1.00** |
| F1 Score  | **1.00** |

> 🔍 Full evaluation results are available in **[`evaluation_results.txt`](https://github.com/SYEDFAIZAN1987/First-Aid-Tutor/blob/main/evaluation_results.txt)**.

## 📈 Evaluation Visualization
Below is a graphical representation of the chatbot’s performance.

![Evaluation Graph](https://github.com/SYEDFAIZAN1987/First-Aid-Tutor/blob/main/evaluation_plot.png)

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
