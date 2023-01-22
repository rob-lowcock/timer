from machine import Pin, SPI
import gc9a01
import utime

import vga1_bold_16x32 as font

class Display:
    
    tft: any
    
    def __init__(self, sck, mosi, reset, cs, dc, backlight):
        spi = SPI(1, baudrate=60000000, sck=Pin(sck), mosi=Pin(mosi))
        self.tft = gc9a01.GC9A01(
            spi,
            240,
            240,
            reset=Pin(reset, Pin.OUT),
            cs=Pin(cs, Pin.OUT),
            dc=Pin(dc, Pin.OUT),
            backlight=Pin(backlight, Pin.OUT),
            rotation=0
        )
        self.tft.init()
        self.tft.fill(gc9a01.BLACK)
    
    def updateCounter(self, value):
        width = self.tft.width()
        self.tft.fill_rect(0, 104, width, 42, gc9a01.BLACK)
        self.tft.text(font, value, 0, 120, 0x00d3)
        
    def flash(self, value):
        width = self.tft.width()
        self.tft.fill_rect(0, 104, width, 42, gc9a01.BLACK)
        utime.sleep(0.2)
        self.tft.text(font, value, 0, 120, gc9a01.WHITE)
        utime.sleep(0.2)
        
display = Display(sck=14, mosi=15, reset=11, cs=13, dc=12, backlight=10)

count = 10
while True:
    display.updateCounter(str(count))
    
    if count == 0:
        for i in range(8):
            display.flash(str(count))
        break
    
    count -= 1
        
    utime.sleep(1)