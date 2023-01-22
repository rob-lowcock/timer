from machine import Pin, PWM
from utime import sleep

class Buzzer:
    buzzer: PWM
    
    def __init__(self, pin):
        self.buzzer = PWM(Pin(pin))
        
    def playtone(self, frequency):
        self.buzzer.duty_u16(1000)
        self.buzzer.freq(frequency)
        
    def silence(self):
        self.buzzer.duty_u16(0)
    
    def tune(self):
        notes = [659, 659, 659, 659, 659, 659, 659, 1047]
        for n in notes:
            self.playtone(n)
            sleep(0.2)
            self.silence()
            sleep(0.2)
    
    def beep(self):
        self.playtone(330)
        sleep(1)
        self.silence()
        
buzz = Buzzer(16)
buzz.tune()