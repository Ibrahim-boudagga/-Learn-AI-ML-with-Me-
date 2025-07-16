import spacy, spacy.displacy, webbrowser, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))
from ColoredLogs import Debugger

Debugger.info("Loading the model...")
nlp = spacy.load("en_core_web_sm")

google_text = "Google was founded on September 4, 1998, by computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet."
doc = nlp(google_text)

Debugger.info("Extracting entities directly from the text...")
for ent in doc.ents:
    Debugger.success(f"{ent.text} - {ent.label_}")

Debugger.info("Visualizing the entities...")
# Save visualization to HTML file
file_name = "ner_visualization_original.html"
html = spacy.displacy.render(doc, style="ent", page=True)
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)
Debugger.success(f"Visualization saved to '{file_name}'")
# Automatically open the HTML file in browser
file_path = os.path.abspath(file_name)
webbrowser.open(f"file://{file_path}")
Debugger.info("Opening visualization in your default browser...")

# Remove stop words and punctuation
Debugger.info("Removing stop words and punctuation...")
google_text_clean = " ".join(
    [token.text for token in doc if not token.is_stop and not token.is_punct]
)
Debugger.yellow(google_text_clean)

Debugger.info("Removing stop words and punctuation...")
google_text_clean_doc = nlp(google_text_clean)

Debugger.info("Extracting entities from the cleaned text...")
for ent in google_text_clean_doc.ents:
    Debugger.success(f"{ent.text} - {ent.label_}")

Debugger.info("Visualizing the entities...")
# Save visualization to HTML file
file_name = "ner_visualization_cleaned.html"
html = spacy.displacy.render(google_text_clean_doc, style="ent", page=True)
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)
Debugger.success(f"Visualization saved to '{file_name}'")
# Automatically open the HTML file in browser
file_path = os.path.abspath(file_name)
webbrowser.open(f"file://{file_path}")
Debugger.info("Opening visualization in your default browser...")
# the difference is that the cleaned text has less entities, because the stop words and punctuation are removed
