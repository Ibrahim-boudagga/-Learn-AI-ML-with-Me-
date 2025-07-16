import os, sys

from regex import D


def import_path(path):
    return os.path.join(os.path.dirname(__file__), path)


sys.path.append(import_path("../../../../"))
from ColoredLogs import Debugger

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
from nltk.util import ngrams
import matplotlib.pyplot as plt

# Download required packages
nltk.download("stopwords")
nltk.download("punkt_tab")

data = pd.read_csv(import_path("tripadvisor_hotel_reviews.csv"))

Debugger.white(data.info())
Debugger.yellow(data.head())
Debugger.red(data["Review"][0])
# Lowercase
data["Review_lower"] = data["Review"].str.lower()
Debugger.yellow(data.head())
Debugger.red(data["Review_lower"][0])
# Remove punctuation
data["Review_lower_no_punct"] = data["Review_lower"].str.replace(r"[^\w\s]", "")
Debugger.yellow(data.head())
Debugger.red(data["Review_lower_no_punct"][0])
# Remove stopwords
en_stopwords = stopwords.words("english")
en_stopwords.remove("not")
data["Review_lower_no_punc_no_stopwords"] = data["Review_lower_no_punct"].apply(
    lambda x: " ".join(
        [word for word in x.split() if word not in en_stopwords],
    )
)
Debugger.yellow(data.head())
Debugger.red(data["Review_lower_no_punc_no_stopwords"][0])
# Tokenization
data["Review_lower_no_punc_no_stopwords_tokenized"] = data[
    "Review_lower_no_punc_no_stopwords"
].apply(lambda x: nltk.word_tokenize(x))
Debugger.yellow(data.head())
Debugger.red(data["Review_lower_no_punc_no_stopwords_tokenized"][0])
# Stemming
ps = PorterStemmer()
data["stemmed"] = data["Review_lower_no_punc_no_stopwords_tokenized"].apply(
    lambda x: " ".join([ps.stem(word) for word in x])
)
Debugger.yellow(data.head())
Debugger.red(data["stemmed"][0])
# Lemmatization
lm = WordNetLemmatizer()
data["lemmatized"] = data["stemmed"].apply(
    lambda x: " ".join([lm.lemmatize(word) for word in x.split()])
)
Debugger.yellow(data.head())
Debugger.red(data["lemmatized"][0])

# N-grams
# Convert lemmatized strings back to tokens for n-gram analysis
all_tokens = []
for text in data["lemmatized"]:
    all_tokens.extend(text.split())

# unigram
unigram_tokens = Counter(ngrams(all_tokens, 1)).most_common(10)
Debugger.red(unigram_tokens)
# bigram
bigram_tokens = Counter(ngrams(all_tokens, 2)).most_common(10)
Debugger.yellow(bigram_tokens)
# trigram
trigram_tokens = Counter(ngrams(all_tokens, 3)).most_common(10)
Debugger.green(trigram_tokens)
