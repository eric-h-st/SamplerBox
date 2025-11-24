#########################################
# LOCAL
# CONFIG
#########################################

AUDIO_DEVICE_ID = 2                     # change this number to use another soundcard
SAMPLES_DIR = "."                       # The root directory containing the sample-sets. Example: "/media/" to look for samples on a USB stick / SD card
MAX_POLYPHONY = 80                      # This can be set higher, but 80 is a safe value
USE_BUTTONS = False                     # Set to True to use momentary buttons (connected to RaspberryPi's GPIO pins) to change preset
USE_I2C_7SEGMENTDISPLAY = False         # Set to True to use a 7-segment display via I2C
USE_SERIALPORT_MIDI = False             # Set to True to enable MIDI IN via SerialPort (e.g. RaspberryPi's GPIO UART pins)
USE_SYSTEMLED = False                   # Flashing LED after successful boot, only works on RPi/Linux
SERIALPORT_PORT = '/dev/ttyAMA0'
SERIALPORT_BAUDRATE = 31250
PITCHBAND_NOTE_RANGE = 2                # Pitchband note range, each direction
IGNORE_MIDI_DEVICES =  []               # Ignore MIDI devices to avoid midi errors and missing/lingering notes. For example: [b'Impulse 20:1', b'Impulse 20:2']
AUTO_LOAD_PROGRAMS =  []                # Upon start, automatically load the programs into midi channels, starting with 1. For example: [1,2,10,6,2] will go to MIDI channels 1-5 respectively. Must not exceed 16 items. 

