import numpy
import soundcard as sc

# get a list of all speakers:
speakers = sc.all_speakers()
print("Speakers:")
for s in speakers:
    print(s)
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
print(f"\nDefault speaker is: {default_speaker}\n")

# get a list of all microphones:
mics = sc.all_microphones()
print("Microphones:")
for m in mics:
    print(m)
# get the current default microphone on your system:
default_mic = sc.default_microphone()
print(f"\nDefault mic is: {default_mic}\n")

# search for a sound card by substring:
one_speaker = sc.get_speaker("Mono")
one_mic = sc.get_microphone("Mono")
# fuzzy-search to get the same results:
# one_speaker = sc.get_speaker('FS2i2')
# one_mic = sc.get_microphone('FS2i2')#


# record and play back one second of audio:
# data = one_mic.record(samplerate=48000, numframes=48000)
# one_speaker.play(data/numpy.max(data), samplerate=48000)

# alternatively, get a `Recorder` and `Player` object
# and play or record continuously:
with one_mic.recorder(samplerate=48000) as mic, one_speaker.player(
    samplerate=48000
) as sp:
    for _ in range(1000):
        data = mic.record(numframes=1024)
        sp.play(data)
