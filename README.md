---
tags:
- chatbot
- evaluation
- first-aid
license: mit
language:
- en
metrics:
- faithfulness
- answer_relevancy
- context_recall
- answer_correctness
- semantic_similarity
---

# 🏥 First Aid Tutor

![First Aid Tutor](https://github.com/SYEDFAIZAN1987/First-Aid-Tutor/blob/main/RAGGPT%20UI.png)

## 📘 About the Project
First Aid Tutor is an **AI-powered chatbot** designed to evaluate the efficacy of **Retrieval-Augmented Generation (RAG)** in medical education for paramedical and medical students. It provides **first-aid guidance** based on medical literature to assess learning outcomes and response accuracy.

This repository contains the **codebase** for the **First Aid Assistant** chatbot, tested on **10 first-aid-related questions**.

## 📢 **Ownership and Attribution**
> **⚠️ Disclaimer:**  
> - The **First Aid Assistant chatbot** is the property of **Mysore Medical College and Research Institute**.  
> - The uploaded **FIRST AID PDF** that forms the basis of the **Retrieval-Augmented Generation (RAG)** process is an **official course material** and the property of **Mysore Medical College and Research Institute**.

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

---
tags:
- chatbot
- evaluation
- first-aid
license: mit
language:
- en
metrics:
- faithfulness
- answer_relevancy
- context_recall
- answer_correctness
- semantic_similarity
---



# 🩺 First Aid Assistant - Model Evaluation Report

This repository also presents the evaluation results of the **First Aid Assistant** chatbot, which provides first aid guidance based on common emergency conditions. The model has been evaluated using the **RAGAS** framework with metrics that assess the quality of the generated answers.

## 📊 **Evaluation Metrics**

The chatbot was evaluated based on the following RAGAS metrics:

- **Answer Relevancy:** Measures how relevant the response is to the user's question.
- **Answer Correctness:** Compares the generated response to the ground truth to assess factual correctness.
- **Semantic Similarity:** Evaluates how semantically similar the generated answer is to the reference answer.

---

## 🚀 **Performance Summary**

| **Metric**               | **Average Score** |
|:--------------------------|:-----------------:|
| **Answer Relevancy**      | **0.94**          |
| **Answer Correctness**    | **0.91**          |
| **Semantic Similarity**   | **0.97**          |

---

## 📈 **Detailed Results**

Here’s a snapshot of the evaluation for some sample questions:

| **Question**                                            | **Answer Relevancy** | **Answer Correctness** | **Semantic Similarity** |
|---------------------------------------------------------|----------------------|------------------------|-------------------------|
| What are the first aid measures for high fever in infants? | 0.93                 | 0.85                   | 0.98                    |
| What are the signs and symptoms of low blood sugar?       | 0.85                 | 0.98                   | 0.94                    |
| What does RICE stand for in first aid treatment?          | 0.99                 | 1.00                   | 0.98                    |
| What is the treatment of snake bite?                      | 0.96                 | 1.00                   | 0.98                    |
| How do you provide first aid for choking?                 | 0.96                 | 0.97                   | 0.98                    |

---

## 📋 **Key Insights**

- The chatbot performed exceptionally well in **semantic similarity** (average score of **0.97**), indicating that responses are closely aligned with the ground truth.
- **Answer correctness** is strong overall but showed slight variability, suggesting room for improvement in handling complex queries.
- The **relevancy** of responses remained consistently high, reflecting the model's ability to address user questions effectively.

---

## 📝 **Evaluation Artifacts**

- **RAGAS Evaluation Report:** [View Full Report](https://huggingface.co/spaces/DrSyedFaizan/FirstAidTutor_RAGAS_Evaluation)

---

## 🌟 **Conclusion**

The **First Aid Assistant** demonstrates reliable performance in answering first aid-related queries with high semantic accuracy and relevancy. Continuous improvement in factual correctness will further enhance its capability to provide life-saving information in emergency situations.

---


## 📥 Download & Re-Evaluate
You can **re-evaluate the chatbot** by running the following:

```
git clone https://huggingface.co/DrSyedFaizan/First_Aid_Assistant_Evaluation
cd First_Aid_Assistant_Evaluation
python eval.py
```

---

## 📌 Author
👨‍⚕ **Dr. Syed Faizan** | 🏥 **Healthcare AI & Data Science**  
🔗 **Hugging Face Repo**: [First_Aid_Assistant_Evaluation](https://huggingface.co/DrSyedFaizan/First_Aid_Assistant_Evaluation)

📩 **For collaborations, inquiries, or improvements, feel free to contribute or reach out!**




