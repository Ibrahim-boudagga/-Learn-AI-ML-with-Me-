# 🗣️ Natural Language Processing (NLP)

> **Learn NLP fundamentals with hands-on projects** 📚

## 🚀 **Quick Start**

```bash
pip install nltk spacy textblob transformers torch
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## 📁 **Course Structure**

### **1. Text Preprocessing** `1_text_preprocessing/`
- **Lowercasing** - Text normalization
- **Stopwords** - Remove noise words  
- **Regex** - Pattern matching
- **Tokenization** - Break text into units
- **Stemming** - Reduce words to roots
- **Lemmatization** - Advanced word normalization
- **N-Grams** - Word sequences

### **2. POS & NER** `2_POS_NER/`
- **POS Tagging** - Grammatical analysis
- **Named Entity Recognition** - Extract entities
- **Practical Task** - BBC news analysis

### **3. Sentiment Analysis** `3_sentiment_alanlysis/`
- **Rule-based** - VADER, TextBlob
- **Practical** - Book reviews analysis

## 🎯 **Learning Path**

1. **Start** → Text preprocessing basics
2. **Build** → Complete NLP pipeline  
3. **Apply** → Real-world projects
4. **Master** → Advanced techniques

## 🛠️ **Technologies**

- **NLTK** - Natural language toolkit
- **spaCy** - Industrial NLP
- **Transformers** - State-of-the-art models
- **TextBlob** - Simple text processing

## 📊 **Quick Example**

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Simple NLP pipeline
text = "The quick brown fox jumps over the lazy dog"
tokens = word_tokenize(text.lower())
clean_tokens = [w for w in tokens if w not in stopwords.words('english')]
print(clean_tokens)  # ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']
```

## 🏆 **Achievement Checklist**

- [ ] Text preprocessing
- [ ] POS tagging & NER  
- [ ] Sentiment analysis
- [ ] Real-world projects

**🎉 Complete all to become an NLP expert!**
