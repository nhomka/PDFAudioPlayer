import sys
import argparse
from SpeakerHelper import SpeakerHelper
from DocumentReader import DocumentReader
import PyPDF2

parser = argparse.ArgumentParser(description='Speak a file')

parser.add_argument('filename', help='The file to be spoken')
parser.add_argument('--voice', type=int, default=1, help='Voice modifier, 0=male, 1=female')
parser.add_argument('--rate', type=int, default=210, help='Words per minute')
parser.add_argument('--volume', type=float, default=1.0, help='Volume, range 0.0 to 1.0')

args = parser.parse_args()

pdfFileName = ""
if args.filename:
    pdfFileName = args.filename
else:
    print('You must provide a filename')
    sys.exit(1)

reader = DocumentReader()
speaker = SpeakerHelper()      

if args.voice in [0, 1]:
    speaker.set_voice(args.voice)
    print(f"Voice set to {args.voice}")
if 10 <= args.rate <= 500:
    speaker.set_rate(args.rate)
if 0 <= args.volume <= 1.0:
    speaker.set_volume(args.volume)

reader.open(pdfFileName)
pdf_text = reader.convert_to_text()
print(pdf_text)
speaker.speak(pdf_text)
    
speaker.stop()