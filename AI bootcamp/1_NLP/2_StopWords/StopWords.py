from ColoredLogs import Debugger


# import packages
import nltk 
Debugger.info("Downloading stopwords...")
nltk.download('stopwords')

Debugger.info("Getting English stopwords...")
en_stopwords = nltk.corpus.stopwords.words('english')
Debugger.green(f"English stopwords: {en_stopwords}")

sentence = "The talented artist painted colorful murals on city walls"
Debugger.yellow(f"Original sentence: {sentence}")

sentence_without_stopwords = ' '.join([
    word 
    for word in sentence.split() 
    if word not in (en_stopwords)
    and word.isalpha()
    ])


Debugger.green(f"Sentence without stopwords: {sentence_without_stopwords}")

en_stopwords.remove("on")
en_stopwords.append("colorful")

sentence_without_stopwords_custom = ' '.join([
    word for word in sentence.split() 
    if word not in (en_stopwords)
    and word.isalpha()
    ])

Debugger.green(f"Sentence without stopwords custom: {sentence_without_stopwords_custom}")




