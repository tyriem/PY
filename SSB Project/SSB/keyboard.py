import time
import RPi.GPIO as GPIO
import uinput

def main():
    events = (
        uinput.KEY_ENTER,
        uinput.KEY_E,
        uinput.KEY_H,
        uinput.KEY_L,
        uinput.KEY_O,
        uinput.KEY_LEFT,
        uinput.KEY_RIGHT,
        )

# Enable the GPIO and map it to functions
key_events=( uinput.KEY_ENTER, uinput.KEY_LEFT, uinput.KEY_RIGHT )

device=uinput.Device(key_events)

GPIO.setmode(GPIO.BCM)

GPIO.setup (4 , GPIO.IN , pull_up_down=GPIO.PUD_UP)
GPIO.setup (18 , GPIO.IN , pull_up_down=GPIO.PUD_UP)
GPIO.setup (23 , GPIO.IN , pull_up_down=GPIO.PUD_UP)

# Mapping the keyboard to GPIO
while True:
#    GPIO.wait_for_edge(18,GPIO.FALLING)
    input_state = GPIO.input(18)
    if input_state == False:
     device.emit(uinput.KEY_LEFT,1)
     time.sleep(2)
     device.emit(uinput.KEY_LEFT,0) 

#    GPIO.wait_for_edge(4,GPIO.FALLING)
    input_state = GPIO.input(4)
    if input_state == False:
     device.emit(uinput.KEY_RIGHT,1)
     time.sleep(2)
     device.emit(uinput.KEY_RIGHT,0) 

#    GPIO.wait_for_edge(23,GPIO.FALLING)
    input_state = GPIO.input(23)
    if input_state == False:
     device.emit(uinput.KEY_ENTER,1)
     time.sleep(2)
     device.emit(uinput.KEY_ENTER,0) 

GPIO.cleanup()