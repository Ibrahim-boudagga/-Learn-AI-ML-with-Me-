# Named Entity Recognition (NER)

This folder contains implementations and examples of Named Entity Recognition using spaCy.

## What is Named Entity Recognition (NER)?

Named Entity Recognition is a subtask of information extraction that identifies and classifies named entities in text into predefined categories. It's crucial for understanding the key information in documents.

### Common Entity Types:
- **PERSON**: Names of people (e.g., "Larry Page", "Sundar Pichai")
- **ORG**: Organizations (e.g., "Google", "Alphabet Inc.")
- **GPE**: Countries, cities, states (e.g., "California", "United States")
- **LOC**: Non-GPE locations (e.g., "Stanford University")
- **DATE**: Dates and time expressions (e.g., "September 4, 1998")
- **CARDINAL**: Numbers (e.g., "14%", "56%")
- **ORDINAL**: Ordinal numbers (e.g., "first", "second")
- **MONEY**: Monetary values (e.g., "$1.5 billion")
- **PERCENT**: Percentages (e.g., "14%", "56%")
- **QUANTITY**: Measurements (e.g., "10 miles", "5 kg")
- **TIME**: Time expressions (e.g., "2 PM", "morning")
- **EVENT**: Named events (e.g., "World War II")
- **WORK_OF_ART**: Titles of books, songs, etc.
- **LAW**: Named documents made into laws
- **LANGUAGE**: Named languages

## Files in this folder:

- `ner.py`: Implementation of NER using spaCy with visualization
- `NER.ipynb`: Jupyter notebook with NER examples and interactive tutorials
- `README.md`: This documentation file

## Usage Example:

```python
import spacy
import spacy.displacy
import webbrowser
import os

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "Google was founded on September 4, 1998, by Larry Page and Sergey Brin."
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

# Visualize entities
html = spacy.displacy.render(doc, style="ent", page=True)
with open("ner_visualization.html", "w", encoding="utf-8") as f:
    f.write(html)

# Open in browser
webbrowser.open(f"file://{os.path.abspath('ner_visualization.html')}")
```

## Features:

### **Entity Extraction**
- Identifies named entities in text
- Classifies entities into predefined categories
- Provides confidence scores for entity recognition

### **Text Preprocessing**
- Removes stop words and punctuation
- Compares entity extraction before and after cleaning
- Shows how preprocessing affects NER results

### **Visualization**
- Creates interactive HTML visualizations
- Automatically opens in browser
- Color-coded entities by type
- Side-by-side comparison of original vs cleaned text

### **Real-world Example**
The implementation uses Google's founding story as an example, demonstrating:
- **PERSON**: Larry Page, Sergey Brin, Sundar Pichai
- **ORG**: Google, Alphabet Inc., Stanford University
- **DATE**: September 4, 1998, 2004, 2015, 2019
- **GPE**: California
- **CARDINAL**: 14%, 56%
- **EVENT**: IPO (Initial Public Offering)

## Installation:

Make sure you have spaCy and the English model installed:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Running the Script:

```bash
python ner.py
```

This will:
1. Load the spaCy model
2. Process the Google text example
3. Extract entities from original text
4. Create visualization of original text
5. Clean the text (remove stop words and punctuation)
6. Extract entities from cleaned text
7. Create visualization of cleaned text
8. Open both visualizations in your browser

## Output Files:

- `ner_visualization_original.html`: Visualization of entities in original text
- `ner_visualization_cleaned.html`: Visualization of entities in cleaned text
- `ner_visualization.html`: General NER visualization file

**Note**: These HTML files are automatically generated and opened in your browser when running the script.

## Applications:

- **Information Extraction**: Extract key facts from documents
- **Question Answering**: Find relevant entities for queries
- **Document Classification**: Categorize documents by entity types
- **Knowledge Graph Construction**: Build entity relationships
- **Search Engine Optimization**: Improve search relevance
- **Content Analysis**: Understand document structure and key information
- **Data Mining**: Extract structured data from unstructured text
- **Chatbot Development**: Understand user queries and context

## Key Learning Points:

1. **Entity Types**: Understanding different categories of named entities
2. **Preprocessing Impact**: How text cleaning affects entity recognition
3. **Visualization**: Interactive display of entity recognition results
4. **Real-world Data**: Working with actual company and historical information
5. **Browser Integration**: Automatic opening of visualizations
6. **Comparison Analysis**: Side-by-side analysis of original vs cleaned text

## Advanced Features:

- **Custom Entity Recognition**: Training models for domain-specific entities
- **Entity Linking**: Connecting entities to knowledge bases
- **Multi-language Support**: NER in different languages
- **Context Analysis**: Understanding entity relationships
- **Temporal Analysis**: Tracking entities over time

---

**Next Steps**: Explore the visualization files to see how NER works in practice!
