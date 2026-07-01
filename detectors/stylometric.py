import re
import statistics


def analyze_style(text):

    words = re.findall(r"\b\w+\b", text.lower())

    sentences = re.split(r"[.!?]+", text)

    sentence_lengths = [
        len(re.findall(r"\b\w+\b", sentence))
        for sentence in sentences
        if sentence.strip()
    ]

    if len(sentence_lengths) > 1:
        variation = statistics.pstdev(sentence_lengths)
    else:
        variation = 0

    vocabulary = len(set(words))

    total_words = max(len(words), 1)

    type_token_ratio = vocabulary / total_words

    punctuation = len(re.findall(r"[,.!?;:]", text))

    punctuation_density = punctuation / max(len(text), 1)

    score = (
        (1 - min(variation / 20, 1)) * 0.4
        + (1 - type_token_ratio) * 0.4
        + min(punctuation_density * 20, 1) * 0.2
    )

    return round(score, 2)