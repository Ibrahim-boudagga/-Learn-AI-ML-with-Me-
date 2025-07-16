# Part-of-Speech (POS) Tagging and Named Entity Recognition (NER)

This folder contains implementations and examples of Part-of-Speech tagging and Named Entity Recognition using spaCy.

## What is POS Tagging?

Part-of-Speech tagging is the process of assigning grammatical categories (like noun, verb, adjective, etc.) to each word in a text. This is fundamental for understanding the syntactic structure of sentences.

### Common POS Tags:
- **NOUN**: Nouns (e.g., "cat", "house")
- **VERB**: Verbs (e.g., "run", "eat")
- **ADJ**: Adjectives (e.g., "big", "red")
- **ADV**: Adverbs (e.g., "quickly", "very")
- **PROPN**: Proper nouns (e.g., "John", "London")
- **PRON**: Pronouns (e.g., "he", "she", "it")
- **DET**: Determiners (e.g., "the", "a", "an")
- **PREP**: Prepositions (e.g., "in", "on", "at")
- **CONJ**: Conjunctions (e.g., "and", "but", "or")

## What is Named Entity Recognition (NER)?

Named Entity Recognition identifies and classifies named entities in text into predefined categories such as:
- **PERSON**: Names of people
- **ORG**: Organizations
- **GPE**: Countries, cities, etc.
- **LOC**: Non-GPE locations
- **PRODUCT**: Products
- **EVENT**: Named events
- **WORK_OF_ART**: Titles of books, songs, etc.
- **LAW**: Named documents made into laws
- **LANGUAGE**: Named languages

## Files in this folder:

- `pos.py`: Implementation of POS tagging using spaCy
- `pos.ipynb`: Jupyter notebook with POS tagging examples
- `ner.py`: Implementation of Named Entity Recognition
- `ner.ipynb`: Jupyter notebook with NER examples

## Usage Example:

```python
import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "Emma Woodhouse is a character in Jane Austen's novel."
doc = nlp(text)

# POS tagging
for token in doc:
    print(f"{token.text}: {token.pos_}")

# Named Entity Recognition
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
```

## Installation:

Make sure you have spaCy and the English model installed:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Applications:

- **Text Analysis**: Understanding sentence structure
- **Information Extraction**: Identifying key entities
- **Question Answering**: Finding relevant information
- **Machine Translation**: Understanding context
- **Sentiment Analysis**: Understanding word roles in context 