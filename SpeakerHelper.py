import pyttsx3

class SpeakerHelper:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty('rate')
        self.volume = self.engine.getProperty('volume')
        self.engine.setProperty('voice', self.voices[1].id)
        
    def set_voice(self, voice_index):
        """ Set the voice of the speaker

        Args:
            voice_index (int): 0 = male, 1 = female
        """
        self.engine.setProperty('voice', self.voices[voice_index].id)

    def set_rate(self, words_per_minute):
        """ Set the rate of the speaker

        Args:
            words_per_minute (int): Default is 200 wpm
        """
        self.rate = words_per_minute
        self.engine.setProperty('rate', words_per_minute)
        
    def set_volume(self, volume):
        """ Set the volume of the speaker

        Args:
            volume (float): Default is 1.0, range is 0.0 to 1.0
        """
        self.volume = volume
        self.engine.setProperty('volume', volume)
    
    def speak(self, text):
        """ Speak the given text

        Args:
            text (str): Text to be spoken
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()
        
    def save_to_file(self, text, filename):
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()