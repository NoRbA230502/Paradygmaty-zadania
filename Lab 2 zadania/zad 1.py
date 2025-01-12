import re
from collections import Counter


def analyze_text(text):

    num_words = len(re.findall(r'\b\w+\b', text))
    num_sentences = len(re.findall(r'[.!?]', text))
    num_paragraphs = len(re.findall(r'\n+', text)) + 1


    stop_words = {'i', 'a', 'u'}
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(10)


    def reverse_word(word):
        return word[::-1] if word.lower().startswith('a') else word

    transformed_text = ' '.join(map(reverse_word, words))


    results = {
        'Liczba wyrazów': num_words,
        'Liczba zdan': num_sentences,
        'Liczba akapitów w tekście': num_paragraphs,
        'Najczesciej wystepujace slowa': most_common_words,
        'Transformowany tekst': transformed_text
    }

    return results



if __name__ == "__main__":
    sample_text = "Ala ma kota"

    analysis_results = analyze_text(sample_text)

    for key, value in analysis_results.items():
        print(f"{key}: {value}")
