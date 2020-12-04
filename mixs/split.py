from spleeter.separator import Separator
from spleeter.audio.adapter import  get_default_audio_adapter
from youtube import get_audio_directory, clear_wavs


def splitter(path):
    '''takes a file name from youtube.py and separates into 5 stems: vocals,
    drums, bass, piano, and accompaniment'''

    separator = Separator('spleeter:5stems')
    audio_loader = get_default_audio_adapter()
    waveform, rate = audio_loader.load(path, sample_rate=None)
    prediction = separator.separate(waveform)
    clear_wavs()
    return prediction


if __name__ == "__main__":
    splitter()
