from RealtimeTTS import TextToAudioStream, GTTSEngine, GTTSVoice

from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols
import nltk
import re
from spellchecker import SpellChecker

# Substrings to be replaced in the input text.
replacements = [
    ("\\forthel", "Fortel"),
    ("\\latex", "Lay Tech"),
    ("\\smglom", "S M Glom"),
    ("\\stex", "S Tech"),
    ("\\tex", "Tech"),
    ("\\mmt", "M M T"),
    ("\\immt", "I M M T"),
    ("\\uri", "U R I"),
    ("\\url", "U R L"),
    ("\\bnf", "B N F")
  ]

# Replace all substrings of the input text that match @replacements@.
for keyValuePair in replacements:
  gtts.tokenizer.symbols.SUB_PAIRS.append(keyValuePair)

engine = GTTSEngine(GTTSVoice("en", "ie"), False) # available voices: com, com.au, co.uk, us, ca, co.i, ie, co.za
stream = TextToAudioStream(engine)

welcomeStr = "Enter some text to be read aloud. Type \":h\" for help."
helpStr = ":h  help\n:q  quit\n:s  stop\n:p  pause\n:r  resume"

print("\n" + welcomeStr)
while True:
  inputStr = input("> ")
  if inputStr == ":h":
    print(helpStr)
    continue
  elif inputStr == ":q":
    break
  elif inputStr == ":s":
    stream.stop()
    continue
  elif inputStr == ":p":
    stream.pause()
    continue
  elif inputStr == ":r":
    stream.resume()
    continue
  else:
    # Spell-correct the input string (use @distance=1@ to work properly on long 
    # words):
    spell = SpellChecker(distance=1)
    # Extend list of words that are known to the spell checker:
    spell.word_frequency.load_words([
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
      ])
    # Split the input string, keeping all separators. Backslashes and braces do
    # not count as separators such that backslashed words and single (!) words
    # surounded by braces are not auto-corrected.
    words = re.split('([^a-zA-Z0-9\\\\\\{\\}])', inputStr)
    word = ""
    for i in range(len(words)):
      word = words[i]
      if word.isalpha():
        correction = spell.correction(word)
        if correction is not None:
          words[i] = correction
    inputStr = "".join(words) # Concatenate the components of the modified input string
    # Remove braces.
    inputStr = inputStr.replace('{', '').replace('}', '')
    print(inputStr)
    # Split the input text into sentences:
    for sentence in nltk.sent_tokenize(inputStr):
      stream.feed(sentence)
      stream.play_async()
