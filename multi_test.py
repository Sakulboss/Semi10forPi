import RPi.GPIO as GPIO
import time

# Define GPIO pins for select lines
S0 = 17  # A
S1 = 27  # B
S2 = 22  # C
Z = 18   # Common pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(Z, GPIO.IN)

def read_mux_channel(channel):
    # Set the select lines based on the channel
    GPIO.output(S0, channel & 0x01)  # A
    GPIO.output(S1, (channel >> 1) & 0x01)  # B
    GPIO.output(S2, (channel >> 2) & 0x01)  # C

    # Read the common pin
    return GPIO.input(Z)

try:
    while True:
        for channel in range(8):  # Test channels 0 to 7
            read_mux_channel(channel)
            time.sleep(0.1)  # Wait a bit to stabilize
            value = read_mux_channel(channel)
            print(f"Channel {channel}: {'HIGH' if value else 'LOW'}")
            time.sleep(1)  # Wait before switching to the next channel

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()