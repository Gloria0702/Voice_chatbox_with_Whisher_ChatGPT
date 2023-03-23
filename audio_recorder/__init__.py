import pyaudio
import wave
import keyboard
import os
from datetime import datetime
import paramiko


def record_audio():
    # set parameters for recording
    chunk = 1024  # number of samples per frame
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2  # stereo
    fs = 44100  # sample rate

    # create PyAudio object
    p = pyaudio.PyAudio()

    # generate unique filename based on current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"recording_{date_time}.wav"
    path = os.getcwd() + '/record/'
    filepath = os.path.join(path, filename)

    # wait for user to press Enter to start recording
    print("Press Enter to start recording...")
    keyboard.wait('enter')
    print("Recording... Press 'ctrl' to stop recording.")

    # open input stream for recording
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    # start recording
    frames = []
    while True:
        # read audio data from stream
        data = stream.read(chunk)
        # append data to frames list
        frames.append(data)
        # stop recording when user presses Enter again
        if keyboard.is_pressed('ctrl'):
            break

    # stop recording and close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # save recording as WAV file
    print("Saving recording...")
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # print(f"Recording saved as {filepath}.")

    return filepath
