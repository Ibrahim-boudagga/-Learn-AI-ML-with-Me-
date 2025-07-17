# BBC News Analysis: Practical Task

This practical task demonstrates a complete NLP pipeline for analyzing BBC news articles using text preprocessing, Part-of-Speech (POS) tagging, and Named Entity Recognition (NER).

## 📊 Dataset

**bbc_news.csv** - A comprehensive dataset containing:
- **1,001 BBC news articles** from various categories
- **Columns**: index, title, pubDate, guid, link, description
- **Time period**: 2022-2023 news coverage
- **Topics**: Politics, sports, entertainment, business, technology, and more

## 🎯 Learning Objectives

### **Text Preprocessing Pipeline**
1. **Lowercasing** - Convert text to lowercase for consistency
2. **Stopword Removal** - Remove common words that don't add meaning
3. **Punctuation Removal** - Clean text by removing special characters
4. **Tokenization** - Split text into individual words/tokens
5. **Lemmatization** - Reduce words to their base form

### **Part-of-Speech Analysis**
- Identify most common **nouns** in news titles
- Find most frequent **verbs** used in headlines
- Analyze grammatical patterns in news writing

### **Named Entity Recognition**
- Extract **person names** from news articles
- Identify **geographic locations** (GPE - Geo-Political Entities)
- Discover **organizations** and other named entities

## 📁 Files

- **bbc_news.ipynb** - Complete Jupyter notebook with step-by-step analysis
- **bbc_news.csv** - Dataset containing 1,001 BBC news articles
- **README.md** - This documentation file

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas nltk spacy
python -m spacy download en_core_web_sm
```

### Running the Analysis
```bash
jupyter notebook bbc_news.ipynb
```

## 📈 Analysis Steps

### 1. Data Loading and Exploration
```python
import pandas as pd
bbc_data = pd.read_csv("bbc_news.csv")
titles = pd.DataFrame(bbc_data["title"])
```

### 2. Text Preprocessing
- **Lowercasing**: `titles["lowercase"] = titles["title"].str.lower()`
- **Stopword Removal**: Using NLTK's English stopwords
- **Punctuation Removal**: Using regex patterns
- **Tokenization**: Using NLTK's word_tokenize
- **Lemmatization**: Using WordNetLemmatizer

### 3. POS Tagging with spaCy
```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(" ".join(tokensOriginalList))
```

### 4. Named Entity Recognition
```python
ner_rows = [{
    "token": token.text, 
    "entity": token.label_,
} for token in doc.ents]
```

## 🔍 Key Findings

### **Most Common Nouns**
- News-related terms: "news", "report", "story"
- Political terms: "government", "minister", "party"
- Sports terms: "team", "player", "match"

### **Most Common Verbs**
- Action verbs: "says", "announces", "reports"
- Sports verbs: "wins", "beats", "plays"
- Political verbs: "calls", "urges", "warns"

### **Named Entities**
- **Persons**: Political figures, athletes, celebrities
- **Places**: Countries, cities, regions
- **Organizations**: Companies, government bodies, sports teams

## 🛠️ Technologies Used

- **Pandas**: Data manipulation and analysis
- **NLTK**: Natural Language Toolkit for text processing
- **spaCy**: Industrial-strength NLP for POS and NER
- **Regular Expressions**: Text cleaning and pattern matching

## 📚 Learning Outcomes

By completing this practical task, you will:

1. **Master Text Preprocessing** - Understand the complete pipeline from raw text to clean tokens
2. **Apply POS Tagging** - Learn to analyze grammatical structure of news articles
3. **Implement NER** - Extract meaningful entities from real-world text
4. **Work with Real Data** - Handle actual news articles with various topics and styles
5. **Build Analysis Skills** - Create insights from large text datasets

## 🔗 Related Modules

- **Text Preprocessing** (`../1_text_preprocessing/`) - Foundation techniques
- **POS Tagging** (`../pos/`) - Detailed POS analysis
- **NER** (`../ner/`) - Advanced entity recognition

---

**Next Steps**: Explore the Jupyter notebook to see the complete analysis in action!
