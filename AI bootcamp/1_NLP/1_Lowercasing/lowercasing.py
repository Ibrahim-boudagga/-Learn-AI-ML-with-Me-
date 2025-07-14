import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../colored logs'))
from colored_logs import ColoredLog


log = ColoredLog()

log.info("Starting lowercasing...")

sentence = "Her cat's name is Luna"
log.yellow(f"Original: {sentence}")
lower_sentence = sentence.lower()
log.green(f"Lowercase: {lower_sentence}")

sentenceList = [
    "Her cat's name is Luna",
    "MY CAT'S NAME IS LUNA",
    "her cat's name is luna",
    "HER CAT'S NAME IS LUNA",]

log.yellow(f"Original list: {sentenceList}")
lower_sentenceList = [sentence.lower() for sentence in sentenceList]
log.green(f"Lowercase list: {lower_sentenceList}")

log.success("Lowercasing completed!")

