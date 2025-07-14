sentence = "Her cat's name is Luna"
print(sentence)
lower_sentence = sentence.lower()
print(lower_sentence)

sentenceList = [
    "Her cat's name is Luna",
    "My cat's name is Luna",
    "Her cat's name is Luna",
    "Her cat's name is Luna",]
print(sentenceList)
lower_sentenceList = [sentence.lower() for sentence in sentenceList]
print(lower_sentenceList)

