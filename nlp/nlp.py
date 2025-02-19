from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import nltk

nltk.download('punkt')
nltk.download('stopwords')

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def analyze_text(self, text):
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in self.stop_words and word.isalnum()]
        word_freq = Counter(filtered_words)
        return word_freq

    def summarize_text(self, text):
        sentences = sent_tokenize(text)
        if len(sentences) <= 2:
            return text
        word_freq = self.analyze_text(text)
        ranked_sentences = sorted(sentences, key=lambda s: sum(word_freq[word] for word in word_tokenize(s.lower()) if word in word_freq), reverse=True)
        summary = ' '.join(ranked_sentences[:2])
        return summary