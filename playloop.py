#!/usr/bin/python3
import simpleaudio as sa
import wave
from pydub import AudioSegment
from sys import argv

player = None
audiofile = argv[1]

try:
	while True:
		try:
			num_channels = 0
			sample_width = 0
			frame_rate = 0
			audio_data = None

			with wave.open(audiofile, "rb") as wf:
				num_channels = wf.getnchannels()
				sample_width = wf.getsampwidth()
				frame_rate = wf.getframerate()
				audio_data = wf.readframes(wf.getnframes())
		except wave.Error:
			audio = AudioSegment.from_file(audiofile)
			audio = audio.fade_in(50)
			audio = audio.fade_out(50)
			audio_data = audio.raw_data
			num_channels = audio.channels
			sample_width = audio.sample_width
			frame_rate = audio.frame_rate
		finally:
			if audio_data is not None:
				player = sa.play_buffer(audio_data, num_channels, sample_width, frame_rate)
				player.wait_done()
except KeyboardInterrupt:
	if player is not None:
		player.stop()
	exit()
except FileNotFoundError:
	print("File not found")
	exit()
