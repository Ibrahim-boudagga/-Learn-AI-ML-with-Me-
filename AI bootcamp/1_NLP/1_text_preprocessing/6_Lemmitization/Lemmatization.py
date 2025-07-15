import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from ColoredLogs import Debugger

import nltk
from nltk.stem import PorterStemmer , WordNetLemmatizer

#wordnet is a pre-defined dictionary of words and their meanings
nltk.download('wordnet')

#the diffrence between ls and ps is that ls is more aggressive in removing suffixes and ps is more conservative
ps = PorterStemmer()
wnl = WordNetLemmatizer()

connectTokens = [
    "connecting",
    "connected",
    "connection",
    "connect",
    "connects",
]

for connectToken in connectTokens:  
    Debugger.log(f"{connectToken} PorterStemmer -> {ps.stem(connectToken)}") # PorterStemmer
    Debugger.purple(f"{connectToken} WordNetLemmatizer -> {wnl.lemmatize(connectToken)}") # WordNetLemmatizer


footballTokens = [
    "football",
    "footballs",
    "footballer",
    "footballers",
    "footballing",
]

for footballToken in footballTokens:
    Debugger.blue(f"{footballToken} PorterStemmer -> {ps.stem(footballToken)}") # PorterStemmer
    Debugger.yellow(f"{footballToken} WordNetLemmatizer -> {wnl.lemmatize(footballToken)}") # WordNetLemmatizer


learnTokens = [
    "learning",
    "learned",
    "learning",
    "learns",
    "learn",
    "learnt",
    "learns",
    "learner",
    "learners",
    "learning",
    "learned",
    "learning",
    "learns",
    "learner",
]

for learnToken in learnTokens:
    Debugger.green(f"{learnToken} PorterStemmer -> {ps.stem(learnToken)}") # PorterStemmer
    Debugger.yellow(f"{learnToken} WordNetLemmatizer -> {wnl.lemmatize(learnToken)}") # WordNetLemmatizer


likeTokens = [
    'likes',
    'better',
    'worse',
]

for likeToken in likeTokens:
    Debugger.red(f"{likeToken} PorterStemmer -> {ps.stem(likeToken)}") # PorterStemmer
    Debugger.white(f"{likeToken} WordNetLemmatizer -> {wnl.lemmatize(likeToken)}") # WordNetLemmatizer
