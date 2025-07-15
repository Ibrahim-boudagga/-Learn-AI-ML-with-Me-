import sys, os
import re
# Add the parent directory to the Python path to find ColoredLogs
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

from ColoredLogs import Debugger


Debugger.info("Regular Expression")

text = "The quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog"
Debugger.yellow(f"Original text: {text}")

# find all the words that start with "t"
words_starting_with_t = re.findall(r'\bt\w+', text)
Debugger.green(f"Words starting with 't': {words_starting_with_t}")

# include raw string indicator
my_folder = "C:\desktop\notes"
Debugger.cyan(f"My folder without raw string indicator: {my_folder}")

my_folder = r"C:\desktop\notes"
Debugger.cyan(f"My folder with raw string indicator: {my_folder}")

#re.search
text = "The quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog"
Debugger.yellow(f"Original text: {text}")
search_result = re.search(r"fox", text)
if search_result:
    Debugger.green(f"Search result: {search_result}")
    Debugger.green(f"Search result start: {search_result.start()}")
    Debugger.green(f"Search result end: {search_result.end()}")
    Debugger.green(f"Search result span: {search_result.span()}")
    Debugger.green(f"Search result string: {search_result.string}")
    Debugger.green(f"Search result re: {search_result.re}")
else:
    Debugger.red("No match found")


#Substitute
string = r"sara was able to help me find the items i needed quickly"
new_string = re.sub(r"sara", r"sarah", string) # replace the incorrect spelling of sarah
Debugger.green(f"New string: {new_string}")

#re.findall
sarahs_reviews = []
pattern_to_find = r"sarah?" 


