# 📊 N-Grams in Natural Language Processing (NLP)

> **Master N-gram analysis for text modeling and language understanding** 📈🔤

[![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat&logo=python)](https://python.org)
[![NLTK](https://img.shields.io/badge/NLTK-Natural%20Language%20Toolkit-blue?style=flat)](https://www.nltk.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-red?style=flat&logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=flat)](https://matplotlib.org/)

---

## 🎯 **What are N-Grams?**

**N-Grams** are contiguous sequences of N items (words, characters, or other units) from a given text. They are fundamental building blocks for understanding language patterns and are widely used in NLP for various applications.

### **🌍 Real-World Analogy**
Think of N-grams like **word combinations** in a sentence:
- **Unigrams (1-grams)**: Individual words → "the", "quick", "brown"
- **Bigrams (2-grams)**: Word pairs → "the quick", "quick brown", "brown fox"
- **Trigrams (3-grams)**: Word triplets → "the quick brown", "quick brown fox"
- **N-grams**: N consecutive words → "the quick brown fox jumps"

---

## 📚 **Why N-Grams Matter**

### **🚀 Key Benefits**
- **Language Modeling** - Predict next word in sequence
- **Text Classification** - Feature extraction for ML models
- **Spell Checking** - Identify incorrect word combinations
- **Machine Translation** - Understand phrase patterns
- **Speech Recognition** - Improve accuracy with context
- **Information Retrieval** - Better search and matching

### **💼 Real-World Applications**
- **Autocomplete** - Google search suggestions
- **Spell Checkers** - Microsoft Word, Grammarly
- **Chatbots** - Natural conversation flow
- **Text Prediction** - Mobile keyboard suggestions
- **Language Models** - GPT, BERT foundation
- **Search Engines** - Query understanding and matching

---

## 🛠️ **Types of N-Grams**

### **1. Unigrams (1-grams)** 📝
- **Definition**: Single words
- **Example**: "the", "quick", "brown", "fox"
- **Use Cases**: Basic word frequency analysis
- **Applications**: Bag-of-words models, keyword extraction

### **2. Bigrams (2-grams)** 🔗
- **Definition**: Pairs of consecutive words
- **Example**: "the quick", "quick brown", "brown fox"
- **Use Cases**: Phrase detection, collocation analysis
- **Applications**: Text classification, language modeling

### **3. Trigrams (3-grams)** 🔗🔗
- **Definition**: Triplets of consecutive words
- **Example**: "the quick brown", "quick brown fox"
- **Use Cases**: Context understanding, phrase patterns
- **Applications**: Machine translation, speech recognition

### **4. Higher N-Grams** 📈
- **4-grams**: "the quick brown fox"
- **5-grams**: "the quick brown fox jumps"
- **N-grams**: N consecutive words
- **Use Cases**: Advanced language modeling
- **Applications**: GPT, BERT, advanced NLP models

---

## 📊 **Implementation Examples**

### **1. Basic N-Gram Generation** 🔧

```python
import nltk
from nltk import ngrams
from ColoredLogs import Debugger

# Sample text
text = "the quick brown fox jumps over the lazy dog"
tokens = text.split()

# Generate different n-grams
unigrams = list(ngrams(tokens, 1))
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

Debugger.info("N-gram examples:")
Debugger.blue(f"Unigrams: {unigrams[:5]}")
Debugger.green(f"Bigrams: {bigrams[:5]}")
Debugger.yellow(f"Trigrams: {trigrams[:5]}")
```

### **2. N-Gram Frequency Analysis** 📈

```python
import pandas as pd
from collections import Counter

# Generate and count n-grams
unigram_counts = Counter(ngrams(tokens, 1))
bigram_counts = Counter(ngrams(tokens, 2))

# Convert to DataFrame for analysis
unigram_df = pd.DataFrame(unigram_counts.most_common(), columns=['N-gram', 'Frequency'])
bigram_df = pd.DataFrame(bigram_counts.most_common(), columns=['N-gram', 'Frequency'])

Debugger.success("Most common n-grams:")
Debugger.blue(f"Top unigrams: {unigram_df.head()}")
Debugger.green(f"Top bigrams: {bigram_df.head()}")
```

### **3. N-Gram Visualization** 📊

```python
import matplotlib.pyplot as plt

def plot_ngrams(tokens, n, title, top_k=10):
    """Plot top K n-grams"""
    ngram_counts = pd.Series(list(ngrams(tokens, n))).value_counts()
    
    # Plot top K n-grams
    ngram_counts.head(top_k).plot.barh(color='lightsalmon', figsize=(12, 8))
    plt.title(title)
    plt.ylabel('N-gram')
    plt.xlabel('Frequency')
    plt.show()

# Generate visualizations
plot_ngrams(tokens, 1, 'Top 10 Unigrams')
plot_ngrams(tokens, 2, 'Top 10 Bigrams')
plot_ngrams(tokens, 3, 'Top 10 Trigrams')
```

---

## 🎯 **N-Gram Analysis Techniques**

### **1. Frequency Analysis** 📊
- **Purpose**: Find most common word combinations
- **Use Cases**: Keyword extraction, topic modeling
- **Benefits**: Identify important phrases and patterns
- **Applications**: SEO analysis, content optimization

### **2. Collocation Detection** 🔍
- **Purpose**: Find words that frequently appear together
- **Use Cases**: Phrase extraction, terminology identification
- **Benefits**: Discover meaningful word associations
- **Applications**: Dictionary building, domain analysis

### **3. Language Modeling** 🤖
- **Purpose**: Predict next word in sequence
- **Use Cases**: Text generation, autocomplete
- **Benefits**: Understand language patterns
- **Applications**: Chatbots, text prediction

### **4. Text Classification** 🏷️
- **Purpose**: Use n-grams as features for ML models
- **Use Cases**: Spam detection, sentiment analysis
- **Benefits**: Capture word order and context
- **Applications**: Document categorization, content filtering

---

## 📈 **Advanced N-Gram Techniques**

### **1. Skip-Grams** ⏭️
```python
def generate_skip_grams(tokens, n, skip=1):
    """Generate n-grams with skip connections"""
    skip_grams = []
    for i in range(len(tokens) - n + 1):
        gram = []
        for j in range(n):
            gram.append(tokens[i + j * skip])
        skip_grams.append(tuple(gram))
    return skip_grams

# Example
tokens = ['the', 'quick', 'brown', 'fox', 'jumps']
skip_bigrams = generate_skip_grams(tokens, 2, skip=2)
Debugger.info(f"Skip bigrams: {skip_bigrams}")
```

### **2. Character N-Grams** 🔤
```python
def character_ngrams(text, n):
    """Generate character-level n-grams"""
    return [text[i:i+n] for i in range(len(text) - n + 1)]

# Example
text = "hello"
char_bigrams = character_ngrams(text, 2)
Debugger.info(f"Character bigrams: {char_bigrams}")
```

### **3. N-Gram Language Model** 📚
```python
from collections import defaultdict

class NGramLanguageModel:
    def __init__(self, n):
        self.n = n
        self.ngram_counts = defaultdict(int)
        self.context_counts = defaultdict(int)
    
    def train(self, tokens):
        """Train the language model"""
        for i in range(len(tokens) - self.n + 1):
            ngram = tuple(tokens[i:i+self.n])
            context = tuple(tokens[i:i+self.n-1])
            
            self.ngram_counts[ngram] += 1
            self.context_counts[context] += 1
    
    def predict_next(self, context):
        """Predict next word given context"""
        context = tuple(context)
        if context not in self.context_counts:
            return None
        
        # Find most likely next word
        max_prob = 0
        best_word = None
        
        for ngram, count in self.ngram_counts.items():
            if ngram[:-1] == context:
                prob = count / self.context_counts[context]
                if prob > max_prob:
                    max_prob = prob
                    best_word = ngram[-1]
        
        return best_word

# Example usage
model = NGramLanguageModel(3)
model.train(tokens)
next_word = model.predict_next(['the', 'quick'])
Debugger.success(f"Predicted next word: {next_word}")
```

---

## 🎯 **Best Practices**

### **✅ Do's**
- **Choose appropriate N** - Balance between context and sparsity
- **Handle edge cases** - Beginning and end of text
- **Consider vocabulary** - Large vocabularies need more data
- **Use smoothing** - Handle unseen n-grams
- **Validate results** - Check n-gram quality
- **Consider domain** - Different domains have different patterns

### **❌ Don'ts**
- **Don't use too large N** - Can lead to data sparsity
- **Don't ignore context** - Consider surrounding words
- **Don't forget preprocessing** - Clean text before n-gram generation
- **Don't ignore smoothing** - Handle unseen combinations
- **Don't use small datasets** - Need sufficient data for reliable patterns
- **Don't ignore stopwords** - Can affect n-gram quality

---

## 🔧 **Installation & Setup**

### **Prerequisites**
```bash
# Install Python 3.8+
python --version

# Install required packages
pip install nltk pandas matplotlib colorama

# Download NLTK data
python -c "import nltk; nltk.download('punkt')"
```

### **Quick Start**
```python
import nltk
from nltk import ngrams
import pandas as pd
from ColoredLogs import Debugger

# Sample text
text = "the quick brown fox jumps over the lazy dog"
tokens = text.split()

# Generate n-grams
unigrams = list(ngrams(tokens, 1))
bigrams = list(ngrams(tokens, 2))

Debugger.info("N-gram generation completed!")
Debugger.blue(f"Unigrams: {len(unigrams)}")
Debugger.green(f"Bigrams: {len(bigrams)}")
```

---

## 📁 **Project Files**

### **Files in this Directory**
- **`N-grams.py`** - Python script with n-gram analysis and visualization
- **`README.md`** - This comprehensive guide

### **Usage**
```bash
# Run the Python script
python "N-grams.py"

# The script will generate:
# - Unigram frequency analysis
# - Bigram frequency analysis  
# - Trigram frequency analysis
# - Visualizations for each
```

---

## 🚀 **Advanced Examples**

### **N-Gram for Text Classification**
```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from ColoredLogs import Debugger

# Sample documents
documents = [
    "the quick brown fox",
    "the lazy dog sleeps",
    "the fox jumps quickly",
    "the dog runs slowly"
]

# Create n-gram features
vectorizer = CountVectorizer(ngram_range=(1, 2))  # Unigrams and bigrams
X = vectorizer.fit_transform(documents)

Debugger.info("N-gram features for text classification:")
Debugger.blue(f"Feature matrix shape: {X.shape}")
Debugger.green(f"Feature names: {vectorizer.get_feature_names_out()[:10]}")
```

### **N-Gram for Language Detection**
```python
def detect_language_ngrams(text, n=3):
    """Detect language using character n-grams"""
    char_ngrams = character_ngrams(text.lower(), n)
    ngram_freq = Counter(char_ngrams)
    
    # Language-specific n-gram patterns
    english_patterns = ['the', 'and', 'ing', 'ion']
    spanish_patterns = ['que', 'los', 'del', 'ción']
    
    english_score = sum(ngram_freq[pattern] for pattern in english_patterns)
    spanish_score = sum(ngram_freq[pattern] for pattern in spanish_patterns)
    
    return 'English' if english_score > spanish_score else 'Spanish'

# Example
text = "the quick brown fox"
language = detect_language_ngrams(text)
Debugger.success(f"Detected language: {language}")
```

---

## 📈 **Performance Considerations**

### **Efficiency Tips**
- **Use efficient data structures** - Counter, defaultdict
- **Process in chunks** for large datasets
- **Cache results** when possible
- **Use vectorized operations** with pandas
- **Consider memory usage** for large n-grams

### **Memory Optimization**
```python
# For large datasets, process in chunks
def process_large_text_ngrams(text, n, chunk_size=1000):
    tokens = text.split()
    for i in range(0, len(tokens), chunk_size):
        chunk = tokens[i:i + chunk_size]
        ngrams_chunk = list(ngrams(chunk, n))
        yield ngrams_chunk
```

---

## 🎓 **Learning Path**

### **Beginner** 🟢
1. **Understand** what n-grams are and why they're useful
2. **Learn** to generate unigrams, bigrams, trigrams
3. **Practice** with simple text examples
4. **Visualize** n-gram frequencies

### **Intermediate** 🟡
1. **Explore** different n-gram types (skip-grams, character n-grams)
2. **Understand** n-gram language models
3. **Implement** n-gram-based text classification
4. **Optimize** for performance and memory

### **Advanced** 🔴
1. **Master** advanced n-gram techniques
2. **Build** custom n-gram language models
3. **Implement** n-gram smoothing techniques
4. **Scale** to large datasets and real-world applications

---

## 🔗 **Related Topics**

- **Text Preprocessing** → Preparing text for n-gram analysis
- **Language Modeling** → Using n-grams for prediction
- **Text Classification** → N-grams as features
- **Machine Learning** → N-gram-based models
- **Information Retrieval** → N-gram matching
- **Natural Language Processing** → Advanced n-gram applications

---

## 📞 **Get Help**

### **Common Issues**
- **Memory problems** → Process in chunks, use efficient data structures
- **Sparsity issues** → Use smoothing techniques, larger datasets
- **Performance problems** → Vectorize operations, use optimized libraries
- **Context limitations** → Consider higher-order n-grams
- **Domain specificity** → Use domain-specific n-gram patterns

### **Resources**
- [NLTK N-gram Documentation](https://www.nltk.org/api/nltk.util.html#nltk.util.ngrams)
- [N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [Character N-grams](https://en.wikipedia.org/wiki/N-gram#Character_n-grams)
- [N-gram Smoothing](https://en.wikipedia.org/wiki/Language_model#Smoothing)

---

## 🎯 **Next Steps**

After mastering n-grams, explore:
1. **Language Models** - Advanced prediction techniques
2. **Word Embeddings** - Vector representations of words
3. **Neural Networks** - Deep learning for text
4. **Transformer Models** - State-of-the-art NLP
5. **Production Systems** - Real-world n-gram applications

---

## 🚨 **Important Considerations**

### **When to Use N-Grams**
- ✅ **Text classification** and categorization
- ✅ **Language modeling** and prediction
- ✅ **Information retrieval** and search
- ✅ **Spell checking** and correction
- ✅ **Machine translation** quality improvement

### **When NOT to Use N-Grams**
- ❌ **Very small datasets** - Insufficient patterns
- ❌ **Real-time applications** - Can be computationally expensive
- ❌ **Very large N values** - Data sparsity issues
- ❌ **Context-independent tasks** - Where word order doesn't matter
- ❌ **Character-level tasks** - Use character n-grams instead

---

*Happy n-gramming! 📊✨* 