from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "emi_agent_lora_adapter"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

test_prompts = [
    "meri EMI due hai kya",
    "main next week payment karunga",
    "abhi paise nahi hai",
    "please mujhe reminder bhejo",
    "EMI kab pay karni hai",
    "sir mujhe thoda time chahiye",
    "payment kaise karu",
    "next month pay karunga",
    "EMI reminder bhejo",
    "payment delay ho gaya"
]

keywords = ["emi","payment","due","installment","pay"]

def check_language(text):
    hinglish_words = ["hai","kar","sir","payment","emi"]
    return any(w in text.lower() for w in hinglish_words)

def check_topic(text):
    return any(k in text.lower() for k in keywords)

def check_length(text):
    words = text.split()
    return len(words) > 0 and len(words) < 100


score = 0

for i,prompt in enumerate(test_prompts):

    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=50
    )

    response = tokenizer.decode(output[0])

    lang_ok = check_language(response)
    topic_ok = check_topic(response)
    len_ok = check_length(response)

    passed = lang_ok and topic_ok and len_ok

    print("\nPrompt:", prompt)
    print("Response:", response)

    if passed:
        print("Result: PASS")
        score += 1
    else:
        print("Result: FAIL")

print("\nFinal Score:", score, "/ 10")