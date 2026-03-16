# Conversational AI Fine-Tuning Project

## Overview

This project demonstrates the full pipeline for building a domain-specific conversational AI assistant. The system is trained to answer **EMI-related customer support queries** using a cleaned conversation dataset and parameter-efficient fine-tuning.

The project is divided into two parts:

* **Part A – Data Cleaning and Quality Filtering**
* **Part B – Model Fine-Tuning and Evaluation**

The model is fine-tuned using **LoRA (Low-Rank Adaptation)** to reduce computational cost while maintaining performance.

---

# Repository Structure

```
repo/
│
├── part_a/
│   ├── raw_conversations.jsonl
│   ├── clean_data.py
│   ├── quality_report.py
│   ├── cleaned_conversations.jsonl
│   ├── rejected_conversations.jsonl
│   └── writeup.md
│
├── part_b/
│   ├── finetune.ipynb
│   ├── eval.py
│   ├── finetune_writeup.md
│   ├── evaluation_results.json
│   └── emi_agent_lora_adapter/
│
├── requirements.txt
└── README.md
```

---

# Part A – Data Cleaning

## Objective

Raw conversational datasets often contain noise, incomplete messages, or formatting issues.
The goal of this stage is to filter and prepare **high-quality training conversations**.

## Steps Performed

1. Load conversations from `raw_conversations.jsonl`
2. Validate conversation structure
3. Remove conversations that:

   * contain empty messages
   * have missing roles
   * have extremely short responses
4. Save valid conversations to `cleaned_conversations.jsonl`
5. Save rejected conversations to `rejected_conversations.jsonl`

## Running Part A

Navigate to the folder:

```
cd part_a
```

Run:

```
python clean_data.py
```

Generate dataset statistics:

```
python quality_report.py
```

---

# Part B – Model Fine-Tuning

## Objective

Fine-tune a conversational language model to respond to **EMI payment related queries** such as:

* EMI due information
* payment reminders
* payment methods
* delayed payments

The model is fine-tuned using **LoRA**, which allows efficient training by updating only a small number of parameters.

## Training Pipeline

1. Load cleaned dataset
2. Format conversations into prompt–response pairs
3. Load base language model
4. Apply LoRA configuration
5. Train using Hugging Face Trainer
6. Save the trained adapter

The complete training process is implemented in:

```
part_b/finetune.ipynb
```

---

# Training Environment

Fine-tuning was performed using **Google Colab GPU** because the local system had limited hardware resources.

Local machine configuration:

* CPU-only environment
* 8 GB RAM

Large language models require GPU acceleration, so training was executed in **Google Colab** to ensure efficient model training.

---

# Saved Model

The trained LoRA adapter is stored in:

```
part_b/emi_agent_lora_adapter/
```

This folder contains the adapter weights and configuration required to load the fine-tuned model.

---

# Model Evaluation

Evaluation was performed using a set of EMI-related prompts.

Example prompts:

* "meri EMI due hai kya"
* "payment kaise karu"
* "abhi paise nahi hai"
* "next week payment karunga"

The evaluation outputs were saved to:

```
part_b/evaluation_results.json
```

Example response:

```
Prompt: meri EMI due hai kya
Response: Aapki EMI payment pending hai. Kripya jaldi payment karein.
```

---

# Running Evaluation

Navigate to Part B:

```
cd part_b
```

Run:

```
python eval.py
```

This script loads evaluation results and displays the generated responses.

---

# Requirements

Install dependencies:

```
pip install -r requirements.txt
```

Main libraries used:

* transformers
* datasets
* peft
* accelerate
* torch

---

# Key Concepts Used

* Conversational Dataset Cleaning
* Prompt-Response Formatting
* Parameter Efficient Fine-Tuning
* LoRA (Low Rank Adaptation)
* Model Evaluation

---

# Conclusion

This project demonstrates an end-to-end workflow for building a domain-specific conversational AI system:

1. Cleaning raw conversation datasets
2. Preparing structured training data
3. Fine-tuning a language model using LoRA
4. Evaluating responses on real-world prompts

The resulting model acts as a **basic EMI support conversational assistant** capable of answering customer queries about payments and due dates.


