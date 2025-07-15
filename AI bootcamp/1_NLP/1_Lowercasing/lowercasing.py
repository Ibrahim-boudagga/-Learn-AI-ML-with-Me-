import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from ColoredLogs import Debugger


Debugger.info("Starting lowercasing...")

sentence = "Her cat's name is Luna"
Debugger.yellow(f"Original: {sentence}")
lower_sentence = sentence.lower()
Debugger.green(f"Lowercase: {lower_sentence}")

sentenceList = [
    "Her cat's name is Luna",
    "MY CAT'S NAME IS LUNA",
    "her cat's name is luna",
    "HER CAT'S NAME IS LUNA",]

Debugger.yellow(f"Original list: {sentenceList}")
lower_sentenceList = [sentence.lower() for sentence in sentenceList]
Debugger.green(f"Lowercase list: {lower_sentenceList}")

Debugger.success("Lowercasing completed!")

