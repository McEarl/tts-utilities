from RealtimeTTS import TextToAudioStream, GTTSEngine, GTTSVoice

engine = GTTSEngine(GTTSVoice("en", "com"), False) # available voices: com, com.au, co.uk, us, ca, co.i, ie, co.za
stream = TextToAudioStream(engine)

inputStr = ""

print("\nEnter some text to be read aloud. Type \":q\" to quit.")
while True:
  inputStr = input("> ")
  if inputStr == ":q":
    break
  stream.feed(inputStr)
  stream.play_async()
