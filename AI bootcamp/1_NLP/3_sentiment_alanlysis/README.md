# Sentiment Analysis

> **Learn sentiment analysis with rule-based and transformer approaches** 📊

## 📁 What's Included

### **Rule-Based** (`rule_based_sentiment.ipynb`)
- **VADER** - Social media sentiment analysis
- **TextBlob** - Simple sentiment detection
- **Use case**: Quick analysis without deep learning

### **Transformers** (`pre-trained_transformers.ipynb`)
- **DistilBERT** - High-accuracy sentiment analysis
- **BERTweet** - Twitter-specific sentiment
- **Use case**: Production applications

### **Practical Project** (`practical_task.ipynb`)
- **Dataset**: Book reviews (`book_reviews_sample.csv`)
- **End-to-end** sentiment analysis pipeline
- **Model comparison** and evaluation

## 🚀 Quick Start

```bash
pip install transformers torch textblob vaderSentiment
```

```python
# Rule-based
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
sentiment = analyzer.polarity_scores("I love this!")
print(sentiment)  # {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.6369}

# Transformer-based
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
result = sentiment_pipeline("This is amazing!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]
```

## 📊 What You'll Learn

- **Rule-based vs. transformer approaches**
- **Model comparison** (accuracy, speed, resources)
- **Real-world application** with book reviews
- **Performance optimization** tips

## 🔧 Quick Fixes

```bash
# Faster model downloads
pip install huggingface_hub[hf_xet]

# Memory issues - use smaller model
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```

## 🎯 Next Level

Ready for more? Explore:
- **Advanced transformers** (BERT, GPT, T5)
- **Custom model training**
- **Multi-language sentiment**
- **Real-time sentiment analysis**

**🚀 Start with the notebooks and discover advanced techniques!** 