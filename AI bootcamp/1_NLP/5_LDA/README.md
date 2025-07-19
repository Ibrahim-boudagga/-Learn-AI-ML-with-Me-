# Topic Modeling with LDA & LSA

> **Discover hidden topics in text documents** 📊

## 📁 What's Included

### **LDA & LSA Analysis** (`LDA._LSA.ipynb`)

- **Latent Dirichlet Allocation (LDA)** - Topic modeling
- **Latent Semantic Analysis (LSA)** - Document similarity
- **News articles dataset** - Real-world text analysis
- **Topic visualization** - Interactive topic exploration

### **Dataset** (`news_articles.csv`)

- **657KB** of news articles
- **102 articles** for topic modeling
- **Real-world content** for analysis

## 🎯 What Are LDA & LSA?

### **LDA (Latent Dirichlet Allocation)**

- **Probabilistic model** that discovers hidden topics in documents
- **Assumes** each document is a mixture of topics
- **Each topic** is a distribution over words
- **Best for** finding semantic themes and document classification

### **LSA (Latent Semantic Analysis)**

- **Linear algebra approach** using Singular Value Decomposition (SVD)
- **Reduces dimensionality** while preserving semantic relationships
- **Creates** a lower-dimensional representation of documents
- **Best for** document similarity and information retrieval

## 📊 When to Use What?

| Technique | Use Case                                   | Pros                                   | Cons                                     | Best For                                     |
| --------- | ------------------------------------------ | -------------------------------------- | ---------------------------------------- | -------------------------------------------- |
| **LDA**   | Topic discovery, document classification   | Interpretable topics, handles polysemy | Requires tuning, assumes topic structure | Research papers, news articles, social media |
| **LSA**   | Document similarity, information retrieval | Fast, simple, preserves relationships  | Less interpretable, linear assumptions   | Search engines, recommendation systems       |

## 🔍 Topic Coherence

### **What is Coherence?**

- **Measures** how semantically similar words in a topic are
- **Higher coherence** = more meaningful topics
- **Lower coherence** = random word collections

### **Coherence Score Interpretation**

- **0.0 - 0.3**: Poor coherence (random topics)
- **0.3 - 0.5**: Moderate coherence (somewhat meaningful)
- **0.5 - 0.7**: Good coherence (meaningful topics)
- **0.7 - 1.0**: Excellent coherence (highly interpretable)

### **Improving Coherence**

```python
# Optimize number of topics
coherence_scores = []
for num_topics in range(2, 21):
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)
    coherence = CoherenceModel(model=lda_model, texts=processed_docs,
                              dictionary=dictionary, coherence='c_v')
    coherence_scores.append(coherence.get_coherence())

# Find optimal number of topics
optimal_topics = range(2, 21)[np.argmax(coherence_scores)]
```

## 🚀 Quick Start

```bash
pip install gensim scikit-learn numpy pandas matplotlib
```

```python
# LDA Topic Modeling
from gensim import corpora, models
from gensim.models import LdaModel, CoherenceModel

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Train LDA model
lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary)

# Evaluate coherence
coherence_model = CoherenceModel(model=lda_model, texts=processed_docs,
                                dictionary=dictionary, coherence='c_v')
coherence_score = coherence_model.get_coherence()
print(f"Coherence Score: {coherence_score:.3f}")
```

## 📊 What You'll Learn

- **Topic modeling** - Discover hidden themes in documents
- **LDA vs LSA** - Different approaches to document analysis
- **Coherence evaluation** - Measure topic quality
- **Document clustering** - Group similar documents
- **Topic visualization** - Interactive topic exploration

## 🎯 Next Level

Ready for more? Explore:

- **Advanced topic models** (HDP, CTM)
- **Dynamic topic modeling**
- **Multi-language topic modeling**
- **Real-time topic analysis**

**🚀 Start with the notebook and discover hidden patterns in text!**
