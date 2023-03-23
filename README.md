# Voice_chatbox_with_Whisher_ChatGPT
Voice command for career advisor with ChatGPT and Whisper

------------------------------------------------------------------------------------
instructions:
Installation
We have tested TFT based on Python 3.10 on Win 10, theoretically it should also work on other operating systems. To get all the dependencies, it is sufficient to run the following command.

pip install -r requirements.txt

------------------------------------------------------------------------------------

The structure of the repository
 It is structured as follows:

+-- readme.md

+-- record/

+-- audio_recorder/

+-- config.py

+-- robotics_local.py

+-- requirements.txt


record/

This directory contains the voice recode files.

audio_recorder/

This directory contains the function to record the voice and automatically saved in the directory ./record

config.py

This code file is the key for connect ChatGPT server.

robotics_local.py

This code file is for recording the voice, and then return the ID number to the robot.

------------------------------------------------------------------------------------
