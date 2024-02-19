from TTSHelper import SpeakerHelper
from DocumentReader import DocumentReader
from AudioController import AudioController

pdfFileName = "Nathan-Homka-Resume.pdf"

speaker = SpeakerHelper()
speaker.set_voice(1)
speaker.set_rate(210)
speaker.set_volume(1.0)

reader = DocumentReader()
reader.open(pdfFileName)
text = reader.convert_to_text()
print(text)
reader.close()

wav_filename = "output.wav"
speaker.save_to_file(text, wav_filename)
speaker.stop()

audio_controller = AudioController()
audio_controller.play(wav_filename)

while True:
    print("Press 'p to pause \nPress 'r' to resume \nPress 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
        audio_controller.pause() 
    elif query == 'r':
        audio_controller.unpause() 
    elif query == 'e':
        audio_controller.stop()
        break

