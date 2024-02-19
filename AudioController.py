from pygame import mixer

class AudioController:
    def __init__(self):
        mixer.init()
        
    def play(self, wav_filename):
        mixer.music.load(wav_filename)
        mixer.music.play()
        
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