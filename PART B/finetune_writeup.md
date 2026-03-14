# Finetuning Writeup

## Model Choice

For this task, the model **Qwen2.5-0.5B-Instruct** was selected. The model is relatively small compared to large language models, which allows it to run on the Google Colab free tier GPU (T4 with 16GB VRAM). Despite its small size, it supports instruction-following behavior and performs reasonably well for conversational tasks.

## LoRA Configuration

LoRA (Low Rank Adaptation) was used to finetune the model efficiently without updating all model parameters.

Configuration used:

* Rank (r): 8
* LoRA Alpha: 16
* Target modules: q_proj, v_proj
* LoRA Dropout: 0.1

These values were chosen to balance training stability and GPU memory usage. Using LoRA significantly reduces the number of trainable parameters while maintaining good adaptation capability.

## Training Setup

* Training data: Cleaned conversation dataset from Part A
* Epochs: 1
* Batch size: 2
* Maximum sequence length: 256

The goal was not to train a high-quality model but to demonstrate a working end-to-end finetuning pipeline.

## What Went Well

The LoRA training pipeline successfully ran on the Colab GPU and produced adapter weights. The model was able to generate responses related to EMI payment conversations after finetuning.

## Challenges

The dataset was relatively small and synthetic, which limited the model’s ability to generate diverse responses. Additionally, simple heuristic evaluation methods were used rather than advanced NLP metrics.

## Future Improvements

If more time and compute were available, the following improvements could be implemented:

1. Increase the dataset size with more realistic conversations.
2. Train for more epochs and experiment with different LoRA configurations.
3. Use automatic evaluation metrics such as BLEU, ROUGE, or semantic similarity.
4. Add conversation context rather than single-turn prompts.
