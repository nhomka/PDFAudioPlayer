import from SpeakerHelper import SpeakerHelper, PyPDF2

pdfFileName = "Nathan-Homka-Resume.pdf"
pdfReader = PyPDF2.PdfReader(pdfFileName)

speaker = SpeakerHelper()
speaker.set_voice(1)
speaker.set_rate(210)
speaker.set_volume(1.0)

for page in pdfReader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    speaker.speak(text)
    
speaker.stop()