import sys
import subprocess
from RealtimeTTS import TextToAudioStream, GTTSEngine, GTTSVoice

args = sys.argv

if len(args) != 3:
  print(f"Usage: python {args[0]} <path to output file> '<input string>'")
else:
  engine = GTTSEngine(voice = GTTSVoice("en", "com")) # available voices: com, com.au, co.uk, us, ca, co.i, ie, co.za
  stream = TextToAudioStream(engine)
  inputStr = args[2]
  outputPath = args[1]
  stream.feed(inputStr)
  # Convert the input string to a .wav file:
  stream.play(muted = True, output_wavfile = outputPath + ".wav")
  # Convert the .wav file to the originally given audio format:
  subprocess.run(["ffmpeg", "-y", "-i", outputPath + ".wav", outputPath])
  subprocess.run(["rm", outputPath + ".wav"])
