import os, sys,re

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../colored logs'))
from colored_logs import ColoredLog

log=ColoredLog()

log.info("Regular Expression")

text = "The quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog"
log.yellow(f"Original text: {text}")

# find all the words that start with "t"
words_starting_with_t = re.findall(r'\bt\w+', text)
log.green(f"Words starting with 't': {words_starting_with_t}")

# include raw string indicator
my_folder = r"C:\desktop\notes"
log.cyan(f"My folder: {my_folder}")

#re.search
text = "The quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog"
log.yellow(f"Original text: {text}")
search_result = re.search(r"fox", text)
if search_result:
    log.green(f"Search result: {search_result}")
    log.green(f"Search result group: {search_result.group()}")
    log.green(f"Search result start: {search_result.start()}")
    log.green(f"Search result end: {search_result.end()}")
    log.green(f"Search result span: {search_result.span()}")
    log.green(f"Search result string   : {search_result.string}")
    log.green(f"Search result re: {search_result.re}")
else:
    log.red("No match found")


#Substitute
string = r"sara was able to help me find the items i needed quickly"
new_string = re.sub(r"sara", r"sarah", string) # replace the incorrect spelling of sarah
log.green(f"New string: {new_string}")

#re.findall
sarahs_reviews = []
pattern_to_find = r"sarah?" 


