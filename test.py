from SpeakerHelper import SpeakerHelper
from DocumentReader import DocumentReader
from pygame import mixer

pdfFileName = "Nathan-Homka-Resume.pdf"
reader = DocumentReader()

speaker = SpeakerHelper()
speaker.set_voice(1)
speaker.set_rate(210)
speaker.set_volume(1.0)

reader.open(pdfFileName)
text = reader.convert_to_text()
print(text)
reader.close()

wav_file = "output.wav"
speaker.save_to_file(text, wav_file)
speaker.stop()

mixer.init()
mixer.music.load(wav_file)
mixer.music.play()

def pause():
    mixer.music.pause()
    
def unpause():
    mixer.music.unpause()
    
def stop():
    mixer.music.stop()

while True:
    print("Press 'p to pause \nPress 'r' to resume \nPress 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
        pause() 
    elif query == 'r':
        unpause() 
    elif query == 'e':
        stop()
        break

