from pygame import mixer

class AudioController:
    def __init__(self):
        mixer.init()
        
    def play(self, wav_filename):
        mixer.music.load(wav_filename)
        mixer.music.play()
        self._control_active_audio()
        
    def pause(self):
        mixer.music.pause()
        
    def unpause(self):
        mixer.music.unpause()
        
    def stop(self):
        mixer.music.stop()
        
    def close(self):
        mixer.quit()
        
    def is_playing(self):
        return mixer.music.get_busy() == 1
    
    def _control_active_audio(self):
        while True:
            print("Press 'p to pause \nPress 'r' to resume \nPress 'e' to exit the program")
            query = input("  ")
            
            if query == 'p':
                self.pause() 
            elif query == 'r':
                self.unpause() 
            elif query == 'e':
                self.stop()
                break