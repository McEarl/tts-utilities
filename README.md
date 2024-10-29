# TTS Utilities

## Setup

  1.  Create a virtual environment (from within the root directory of this
      repository): `python3 -m venv venv`

  2.  Activate the virtual environment: `source venv/bin/activate`

  3.  Install the [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS),
      `nltk` and `pyspellchecker` packages:
      `pip install realtimetts\[all\] nltk pyspellchecker`

  4.  Close the virtual environment: `deactivate`

  5.  Create an environment variable `TTSUTILITIES` containing the absolute path
      to the root directory of this repository.

  6.  *(Optional, if you want to use TTS in LaTeX)* Add the `tex` directory to
      your `$TEXINPUTS` variable.


## Real-Time TTS

Enter text in a shell-like environment that is read aloud in real-time.

**Usage:** Run the script `sh/realtimetts.sh`.


## Text to Audio File

Convert a string to an audio file.

**Usage:** Run the script `sh/tts.sh <path to output file> '<input string>'`.


## TTS in LaTeX

Embed synthesized speech in LaTeX documents.


### Usage

**Note:** Intended to be used in beamer frames only!
 
Use `\audiotitle{<frame title>}{<path to audio file>}{<text>}` to invoke TTS
during the compilation of the document to create an audio file for a given
text that can be played (and stopped) by clicking on a "play" button that is
rendered beneath the title (together with a "stop" button).

To only show the audio buttons without invoking the TTS generation, use
`\audiotitle[\skiptts]{<frame title>}{<path to audio file>}{<text>}` instead.

**Important**: Make sure to run pdflatex with the `--shell-escape` flag!


### Misc

The embedding of synthesized speech in to PDF relies on the `\sound` comaḿand
of the `multimedia` package (see section 14.2 of
<https://mirror.quantum5.ca/CTAN/macros/latex/contrib/beamer/doc/beameruserguide.pdf>)
The audio files that are passed to the `\sound` command are embedded into the
PDF file which results in comparably large file sizes. Moreover, the audio
files might need to be in an uncompressed format, depending on the PDF viewer.
