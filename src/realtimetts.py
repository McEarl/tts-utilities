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
    ("\\tex", "Tech")
  ]

# Replace all substrings of the input text that match @replacements@.
for keyValuePair in replacements:
  gtts.tokenizer.symbols.SUB_PAIRS.append(keyValuePair)

engine = GTTSEngine(GTTSVoice("en", "ie"), False) # available voices: com, com.au, co.uk, us, ca, co.i, ie, co.za
stream = TextToAudioStream(engine)

welcomeStr = "Enter some text to be read aloud. Type \":h\" for help."
helpStr = ":h  help\n:q  quit\n:s  stop\n:p  pause\n:r  resume"

print("\n" + welcomeStr)
#inputStr = ""
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
    # Spell-correct the input string:
    spell = SpellChecker()
    words = re.split('([^a-zA-Z0-9\\\\])', inputStr) # Split the input string, keeping all separators
    word = ""
    for i in range(len(words)):
      word = words[i]
      if word.isalpha():
        correction = spell.correction(word)
        if correction is not None:
          words[i] = correction
    inputStr = "".join(words) # Concatenate the components of the modified input string
    print("Correction:" + inputStr)
    # Split the input text into sentences:
    for sentence in nltk.sent_tokenize(inputStr):
      stream.feed(sentence)
      stream.play_async()
