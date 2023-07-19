# Pico Alarm Clock

**1. Connect the TM1627 4-Digit Display:**
  - Connect the `VCC` and `GND` pin to the `3v3` and `GND` pins on the Raspberry Pi Pico Respectivly
  - Connect the `DIO` pin on the display to the `GP4` pin on the Pico
  - Connect the `CLK` pin to the `GP5` pin on the Pico

**2. Connect the Button and Buzzer to the Pico**
  - Connect one side of the button to a `GND` pin on the Pico, and the other side to the `GP7` pin on the Pico
  - Connect one side of the buzzer to a `GND` pin on the Pico, and the other side to the `GP28` pin on the Pico

**3. Connect the Rotary Encoder to the Pico**
  - Connect the `VCC` and `GND` pins on the Encoder to `3V3` and `GND` pins on the Pico Respectivly
  - Connect the `SW` pin on the Encoder to `GP2` on the Pico
  - Connect the `DT` pin to the `GP0` pin on the Pico
  - Connect the `CLK` pin on the Encoder to the `GP1` pin on the Pico

**4. Code Everything**
  - Download and extract all the files and folders from this repository
  - Open Everything in the Thoney Python editor
  - Plug it your Pico and Be sure it has Micro-Python installed on it found on the Offical Raspberry Pi Pico Documentation
  - Save the `main.py` file to the main directory on the pico through Thoney
  - If there is no folder named `lib` on the Pico, Create a new directory and save the `rotary.py` and `tm1637` files to that new directory.

**5. Set the time and alarm**
  - Plug the Pico with everything connected into a permanent power supply (To Avoid have to reset the time and alarm)
  - Turn the rotary encoder left or right to change the time that is displayed (Note: The time is in the 24-Hour Format)
  - Once you have set the time, you may disconnect the rotary encoder from the setup. (Unless You want to set an alarm)
  - To set the alarm connect the rotary encoder back where it originally was makeing sure it fallows the above wiring instructions
  - Then click the button three times within 2 seconds. This will display `00:00` on the `TM1637` display
  - Turn the rotary encoder to set the disired time the alarm will go off
  - Once the alarm is set, click the button three time within 2 seconds again and it will display the current time
  - When the alarm sounds at your disired time, hit the button to turn the alarm off
  - The alarm will the sound again at the same time the next day

## **Disclaimer:** When loss of power occurs the Pico will have to be reset
