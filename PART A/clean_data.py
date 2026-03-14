import json

RAW_FILE = "raw_conversations.jsonl"
CLEAN_FILE = "cleaned_conversations.jsonl"
REJECT_FILE = "rejected_conversations.jsonl"

VALID_LANGUAGES = {"english", "hindi", "hinglish"}
VALID_OUTCOMES = {
    "payment_committed",
    "callback_scheduled",
    "escalated",
    "no_resolution"
}


def has_empty_turn(turns):
    """
    Detect turns with empty or whitespace text
    """
    for turn in turns:
        if "text" not in turn:
            return True
        if turn["text"].strip() == "":
            return True
    return False


def has_duplicate_consecutive_turns(turns):
    """
    Detect duplicate consecutive turns
    """
    for i in range(1, len(turns)):
        prev = turns[i - 1]
        curr = turns[i]

        if prev["role"] == curr["role"] and prev["text"] == curr["text"]:
            return True

    return False


def has_too_few_turns(turns):
    """
    Detect conversations with less than 2 turns
    """
    return len(turns) < 2


def invalid_metadata(metadata):
    """
    Check metadata validity
    """
    if metadata is None:
        return True

    duration = metadata.get("call_duration_seconds")
    outcome = metadata.get("outcome")

    if duration is None or duration < 0:
        return True

    if outcome not in VALID_OUTCOMES:
        return True

    return False


def invalid_language(language):
    """
    Validate language field
    """
    return language not in VALID_LANGUAGES


def detect_encoding_issue(turns):
    """
    Very simple heuristic for garbled characters
    """
    bad_chars = ["€", "¥", "�"]

    for turn in turns:
        text = turn.get("text", "")
        for ch in bad_chars:
            if ch in text:
                return True

    return False


def main():

    cleaned = []
    rejected = []

    with open(RAW_FILE, "r", encoding="utf-8") as f:

        for line in f:
            conversation = json.loads(line)

            turns = conversation.get("turns", [])
            metadata = conversation.get("metadata")
            language = conversation.get("language")

            rejection_reason = None

            if has_too_few_turns(turns):
                rejection_reason = "too_few_turns"

            elif has_empty_turn(turns):
                rejection_reason = "empty_turn"

            elif has_duplicate_consecutive_turns(turns):
                rejection_reason = "duplicate_turn"

            elif invalid_metadata(metadata):
                rejection_reason = "invalid_metadata"

            elif invalid_language(language):
                rejection_reason = "invalid_language"

            elif detect_encoding_issue(turns):
                rejection_reason = "encoding_issue"

            if rejection_reason:
                conversation["rejection_reason"] = rejection_reason
                rejected.append(conversation)
            else:
                cleaned.append(conversation)

    with open(CLEAN_FILE, "w", encoding="utf-8") as f:
        for convo in cleaned:
            f.write(json.dumps(convo) + "\n")

    with open(REJECT_FILE, "w", encoding="utf-8") as f:
        for convo in rejected:
            f.write(json.dumps(convo) + "\n")

    print("Cleaning completed")
    print("Valid conversations:", len(cleaned))
    print("Rejected conversations:", len(rejected))


if __name__ == "__main__":
    main()