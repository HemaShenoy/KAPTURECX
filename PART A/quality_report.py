import json
from collections import Counter

RAW_FILE = "raw_conversations.jsonl"
CLEAN_FILE = "cleaned_conversations.jsonl"
REJECT_FILE = "rejected_conversations.jsonl"


def load_jsonl(file_path):
    """
    Load JSONL file into list of dictionaries
    """
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def language_distribution(data):
    """
    Count languages
    """
    languages = [d.get("language", "unknown") for d in data]
    return Counter(languages)


def outcome_distribution(data):
    """
    Count outcomes
    """
    outcomes = []

    for d in data:
        metadata = d.get("metadata", {})
        outcome = metadata.get("outcome")
        if outcome:
            outcomes.append(outcome)

    return Counter(outcomes)


def rejection_reason_distribution(data):
    """
    Count rejection reasons
    """
    reasons = [d.get("rejection_reason", "unknown") for d in data]
    return Counter(reasons)


def average_turns(data):
    """
    Calculate average number of turns per conversation
    """
    if len(data) == 0:
        return 0

    total_turns = sum(len(d.get("turns", [])) for d in data)

    return round(total_turns / len(data), 2)


def print_counter(title, counter):
    """
    Print formatted distribution
    """
    print("\n" + title)
    print("-" * len(title))

    for key, value in counter.items():
        print(f"{key}: {value}")


def main():

    raw_data = load_jsonl(RAW_FILE)
    clean_data = load_jsonl(CLEAN_FILE)
    rejected_data = load_jsonl(REJECT_FILE)

    print("\nDATASET SUMMARY")
    print("=================")

    print(f"Total raw conversations: {len(raw_data)}")
    print(f"Total cleaned conversations: {len(clean_data)}")
    print(f"Total rejected conversations: {len(rejected_data)}")

    # Rejection reasons
    rejection_stats = rejection_reason_distribution(rejected_data)
    print_counter("Rejection Reasons", rejection_stats)

    # Language distributions
    raw_lang = language_distribution(raw_data)
    clean_lang = language_distribution(clean_data)

    print_counter("Language Distribution BEFORE Cleaning", raw_lang)
    print_counter("Language Distribution AFTER Cleaning", clean_lang)

    # Outcome distributions
    raw_outcome = outcome_distribution(raw_data)
    clean_outcome = outcome_distribution(clean_data)

    print_counter("Outcome Distribution BEFORE Cleaning", raw_outcome)
    print_counter("Outcome Distribution AFTER Cleaning", clean_outcome)

    # Average turns
    print("\nAverage Turns Per Conversation")
    print("--------------------------------")
    print(f"Before cleaning: {average_turns(raw_data)}")
    print(f"After cleaning: {average_turns(clean_data)}")


if __name__ == "__main__":
    main()