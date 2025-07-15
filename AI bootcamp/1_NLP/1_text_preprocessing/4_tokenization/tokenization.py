import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from ColoredLogs import Debugger


# import nltk package
import nltk
nltk.download('punkt_tab')

text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
Debugger.yellow(f"Original text: {text}")
wordTokens = nltk.word_tokenize(text)
Debugger.green(f"Word tokens: {wordTokens}")

sentenceTokens = nltk.sent_tokenize(text)
Debugger.magenta(f"Sentence tokens: {sentenceTokens}")









