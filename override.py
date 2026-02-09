class MediaPlayer:
    def play(self):
        print("playing media")


class AudioPlayer(MediaPlayer):
    def play(self):
        print("playing audio")


class VideoPlayer(MediaPlayer):
    def play(self):
        print("playing video")


AP=AudioPlayer()
AP.play()
VP=VideoPlayer()
VP.play()
