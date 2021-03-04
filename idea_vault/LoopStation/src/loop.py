from typing import Dict, Optional

from audio import Audio


class Loop:
    def __init__(self, beats_p_minute, beats_p_bar, bars_p_loop):
        if beats_p_minute < 10:
            raise ValueError("bpm is to slow")
        if beats_p_minute > 280:
            raise ValueError("bpm is to fast")
        if beats_p_bar <= 1:
            raise ValueError("Bar must contain more than one beat")
        if bars_p_loop <= 0:
            raise ValueError("You must set at least one bar per loop")

        self.beats_p_minute = beats_p_minute
        self.beats_p_bar = beats_p_bar
        self.bars_p_loop = bars_p_loop

        # time that passes between two clicks in seconds
        timeout = 1 / (beats_p_minute / 60)
        # length of one loop in seconds
        self.length = bars_p_loop * beats_p_bar * timeout

        self.channels: Dict = {'main': []}

        self.audio = Audio()

    def play(self, channel: Optional[str]):
        pass

    def stop(self, channel: Optional[str]):
        if channel is None:
            for channel in self.channels:
                self.stop(channel)
        elif channel in self.channels:
            # TODO stop playback of a channel
            pass
        else:
            raise ValueError("Channel does not exist")

    def record(self, channel: str):
        self.channels[channel] = self.audio.record(self.length, channel)

    def record_all(self, filename: str):
        """
        Records a running session
        """
        self.audio.record(filename)

    def add_channel(self, name: str):
        self.channels[name] = []

    class Click:
        def __init__(self):
            pass

        def get_audio(self):
            pass
