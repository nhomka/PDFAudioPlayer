from SpeakerHelper import SpeakerHelper
from DocumentReader import DocumentReader

pdfFileName = "Nathan-Homka-Resume.pdf"
reader = DocumentReader()

speaker = SpeakerHelper()
speaker.set_voice(1)
speaker.set_rate(210)
speaker.set_volume(1.0)

reader.open(pdfFileName)
text = reader.convert_to_text()
print(text)
speaker.speak(text)
    
speaker.stop()

