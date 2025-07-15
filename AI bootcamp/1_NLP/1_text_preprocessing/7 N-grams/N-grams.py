import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from ColoredLogs import Debugger

import nltk
import pandas as pd
from matplotlib import pyplot as plt

def plot_ngrams(tokens, n, title, x=10):
    ngrams = (pd.Series(nltk.ngrams(tokens, n)).value_counts())
    Debugger.blue(ngrams)
    ngrams.sort_values().tail(x).plot.barh(color='lightsalmon', width=.9, figsize=(12, 8))
    plt.title(title)
    plt.ylabel('N-gram')
    plt.xlabel('Frequency')
    plt.show()

tokens = [
    'the', 'rise', 'of', 'artificial', 'intelligence', 'has', 'led', 'to', 'significant', 'advancements', 'in', 'natural',
    'language', 'processing', 'computer', 'vision', 'and', 'other', 'fields', 'machine', 'learning', 'algorithms', 'are', 
    'becoming', 'more', 'sophisticated', 'enabling', 'computers', 'to', 'perform', 'complex', 'tasks', 'that', 'were', 
    'once', 'thought', 'to', 'be', 'the', 'exclusive', 'domain', 'of', 'humans', 'with', 'the', 'advent', 'of', 'deep', 
    'learning', 'neural', 'networks', 'have', 'become', 'even', 'more', 'powerful', 'capable', 'of', 'processing', 'vast', 
    'amounts', 'of', 'data', 'and', 'learning', 'from', 'it', 'in', 'ways', 'that', 'were', 'not', 'possible', 'before', 
    'as', 'a', 'result', 'ai', 'is', 'increasingly', 'being', 'used', 'in', 'a', 'wide', 'range', 'of', 'industries', 'from', 
    'healthcare', 'to', 'finance', 'to', 'transportation', 'and', 'its', 'impact', 'is', 'only', 'set', 'to', 'grow', 'in', 
    'the', 'years', 'to', 'come',
]

# 1-grams (unigrams)
plot_ngrams(tokens, 1, '10 Most Frequently Occuring Unigrams', 10)

# 2-grams (bigrams)
plot_ngrams(tokens, 2, '10 Most Frequently Occuring Bigrams', 10)

# 3-grams (trigrams)
plot_ngrams(tokens, 3, '10 Most Frequently Occuring Trigrams', 10)
