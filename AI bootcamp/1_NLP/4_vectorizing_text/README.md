# Text Vectorization

> **Convert text to numerical features for machine learning** 📊

## 📁 What's Included

### **Bag of Words** (`1_bag_of_words.ipynb`)
- **CountVectorizer** - Word frequency representation
- **Custom implementation** - Manual bag of words
- **Use case**: Basic text classification

### **TF-IDF** (`2_TF-IDF.ipynb`)
- **TfidfVectorizer** - Term frequency-inverse document frequency
- **Document similarity** - Compare text documents
- **Use case**: Advanced text analysis

## 🚀 Quick Start

```bash
pip install scikit-learn numpy pandas
```

```python
# Bag of Words
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(["hello world", "world of python"])
print(X.toarray())  # [[1 1 0], [0 1 1]]

# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(["hello world", "world of python"])
print(X_tfidf.toarray())
```

## 📊 What You'll Learn

- **Text to numbers** - Convert text to machine learning features
- **Bag of Words** - Simple word frequency approach
- **TF-IDF** - Advanced weighting for important words

## 🎯 Next Level

Ready for more? Explore:
- **Word embeddings** (Word2Vec, GloVe)
- **Sentence transformers** (BERT embeddings)
- **Custom vectorization** techniques
- **Large-scale text processing**

**🚀 Start with the notebooks and discover advanced vectorization!**
