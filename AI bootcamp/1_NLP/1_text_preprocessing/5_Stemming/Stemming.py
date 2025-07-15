import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from ColoredLogs import Debugger

from nltk.stem import PorterStemmer , LancasterStemmer

#the diffrence between ls and ps is that ls is more aggressive in removing suffixes and ps is more conservative
ps = PorterStemmer()
ls = LancasterStemmer()

connectTokens = [
    "connecting",
    "connected",
    "connection",
    "connect",
    "connects",
]

for connectToken in connectTokens:
    Debugger.magenta(f"{connectToken} -> {ps.stem(connectToken)}") # PorterStemmer
    Debugger.magenta(f"{connectToken} -> {ls.stem(connectToken)}") # LancasterStemmer


footballTokens = [
    "football",
    "footballs",
    "footballer",
    "footballers",
    "footballing",
]

for footballToken in footballTokens:
    Debugger.blue(f"{footballToken} -> {ps.stem(footballToken)}") # PorterStemmer
    Debugger.blue(f"{footballToken} -> {ls.stem(footballToken)}") # LancasterStemmer


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
    Debugger.green(f"{learnToken} -> {ps.stem(learnToken)}") # PorterStemmer
    Debugger.green(f"{learnToken} -> {ls.stem(learnToken)}") # LancasterStemmer



