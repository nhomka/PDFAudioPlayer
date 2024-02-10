import pyttsx3, PyPDF2

pdfFileName = "Nathan-Homka-Resume.pdf"
pdfReader = PyPDF2.PdfReader(pdfFileName)
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

for page in pdfReader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    engine.say(text)
    engine.runAndWait()
    
engine.stop()