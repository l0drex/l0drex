import pyaudio
import wave


class Audio:
    def __init__(self):
        self.playing = False
        self.recording = False

        self.CHANNELS: int = 2
        self.RATE = 44100
        self.CHUNK = 1024

        # setup portaudio system
        self.p = pyaudio.PyAudio()

    def record(self, length: int, file: str):
        # length is the amount of seconds to record
        if length <= 0:
            raise ValueError("Length must be higher than 0")
        if not file.lower().endswith(".wav"):
            file.append(".wav")

        FORMAT = pyaudio.paInt16

        # open new stream
        self.recording = True
        stream = self.p.open(format=FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * length)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        self.p.terminate()
        self.recording = False

        # write the data to the file
        with wave.open(file, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))

    def play(self, file):
        # open the file
        with wave.open(file, 'rb') as wf:
            self.playing = True
            stream = self.p.open(format=self.p.get_format_from_width(
                                wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

            data = wf.readframes(self.CHUNK)

            while data != '':
                stream.write(data)
                data = wf.readframes(self.CHUNK)

            stream.stop_stream()
            stream.close()
            self.playing = False

    def playback(self, length: int):
        self.playing = True
        self.recording = True

        WIDTH = 2

        stream = self.p.open(format=self.p.get_format_from_width(WIDTH),
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             output=True,
                             frames_per_buffer=self.CHUNK)

        print("* recording")

        for i in range(0, int(self.RATE / self.CHUNK * length)):
            data = stream.read(self.CHUNK)
            stream.write(data, self.CHUNK)

        print("* done")

        stream.stop_stream()
        stream.close()

        self.p.terminate()

        self.recording = False
        self.playing = False
