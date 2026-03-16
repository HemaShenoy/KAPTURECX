import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Base model used during training
base_model = "Qwen/Qwen2-0.5B"

# LoRA adapter folder
adapter_path = "emi_agent_lora_adapter"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(base_model)

print("Loading base model...")
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    torch_dtype=torch.float32
)

print("Loading LoRA adapter...")
model = PeftModel.from_pretrained(model, adapter_path)

model.eval()

# Test prompts
test_prompts = [
    "meri EMI due hai kya",
    "main next week payment karunga",
    "abhi paise nahi hai",
    "payment kaise karu",
    "EMI kab pay karni hai",
]

print("\n----- EMI Agent Evaluation -----\n")

for prompt in test_prompts:

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=50
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("Prompt:", prompt)
    print("Response:", response)
    print()