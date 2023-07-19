from rotary import Rotary
from machine import Pin, I2C, ADC, RTC
import framebuf
import tm1637
import utime

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
button = Pin(7, Pin.IN, Pin.PULL_UP)
led = Pin(28, Pin.OUT)

rtc = RTC()
datetime = rtc.datetime()

rotary = Rotary(0, 1, 2)

val = 0

exit_loops = False

alarm_time = None
alarm_set = False

button_presses = 0
last_button_press_time = 0

def rotary_changed(change):
    global datetime
    global alarm_time
    if change == Rotary.ROT_CW:
        if alarm_set:
            if button.value() == 0:
                alarm_time = (alarm_time[0], alarm_time[1], alarm_time[2], alarm_time[3], (alarm_time[4] + 1) % 24, alarm_time[5], 0, 0)
            else:
                new_minute = (alarm_time[5] + 1) % 60
                new_hour = (alarm_time[4] + (new_minute == 0)) % 24
                alarm_time = (alarm_time[0], alarm_time[1], alarm_time[2], alarm_time[3], new_hour, new_minute, 0, 0)
        else:
            datetime = rtc.datetime()
            if button.value() == 0:
                datetime = (datetime[0], datetime[1], datetime[2], datetime[3], (datetime[4] + 1) % 24, datetime[5], 0, 0)
            else:
                new_minute = (datetime[5] + 1) % 60
                new_hour = (datetime[4] + (new_minute == 0)) % 24
                datetime = (datetime[0], datetime[1], datetime[2], datetime[3], new_hour, new_minute, 0, 0)
            rtc.datetime(datetime)
    elif change == Rotary.ROT_CCW:
        if alarm_set:
            if button.value() == 0:
                alarm_time = (alarm_time[0], alarm_time[1], alarm_time[2], alarm_time[3], (alarm_time[4] - 1) % 24, alarm_time[5], 0, 0)
            else:
                new_minute = (alarm_time[5] - 1) % 60
                new_hour = (alarm_time[4] - (new_minute == 59)) % 24
                alarm_time = (alarm_time[0], alarm_time[1], alarm_time[2], alarm_time[3], new_hour, new_minute, 0, 0)
        else:
            datetime = rtc.datetime()
            if button.value() == 0:
                datetime = (datetime[0], datetime[1], datetime[2], datetime[3], (datetime[4] - 1) % 24, datetime[5], 0, 0)
            else:
                new_minute = (datetime[5] - 1) % 60
                new_hour = (datetime[4] - (new_minute == 59)) % 24
                datetime = (datetime[0], datetime[1], datetime[2], datetime[3], new_hour, new_minute, 0, 0)
            rtc.datetime(datetime)

def button_pressed(pin):
    global button_presses
    global last_button_press_time
    global alarm_set
    global alarm_time
    current_time = utime.ticks_ms()
    if current_time - last_button_press_time > 2000:
        button_presses = 0
    last_button_press_time = current_time
    button_presses += 1
    if button_presses == 3:
        if not alarm_set:
            alarm_set = True
            if alarm_time is None:
                alarm_time = (0,) * 8
        else:
            alarm_set = False

try:
    rotary.add_handler(rotary_changed)
except RuntimeError:
    pass

button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

while True:
    if not alarm_set:
        datetime = rtc.datetime()
        tm.numbers(datetime[4], datetime[5])
        print("Alarm: ", alarm_time)
        print("Local Time: ", datetime)
        if alarm_time is not None and datetime[4] == alarm_time[4] and datetime[5] == alarm_time[5] and datetime[6] == alarm_time[6]:
            led.value(1)
            while button.value() != 0:
                utime.sleep_ms(10)
            led.value(0)
    else:
        tm.numbers(alarm_time[4], alarm_time[5])
    
    utime.sleep(1)