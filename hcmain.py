import hclcd as lcd
from time import sleep
from gpiozero import LED
import iw_parse

buzzer = LED(27)
led1 = LED(4)
led2 = LED(5)
led3 = LED(6)
led4 = LED(12)
led5 = LED(13)
led6 = LED(16)
led7 = LED(17)
led8 = LED(18)
led9 = LED(19)
led10 = LED(20)
network_name = "GiPhone"

def initialize():
    print ('HC Program is starting ... ')
    lcd.display_lcd_line1("HC Program")
    lcd.display_lcd_line2("Started")
    sleep(3)
    lcd.clear()
    lcd.display_lcd_line1("Initializing...")
    for sec in range(1,6):
        lcd.display_lcd_line2("#"*sec)
        
    
def is_network_in_list(list, name):
    for item in list:
        if (item["Name"] == name):
            return True
    return False

    
def get_network(list, name):
    for item in list:
        if (item["Name"] == name):
            return item
    return None


def get_level(dbLevel):
    if (dbLevel >= -20):
        return 10
    min = -20.0 # 10
    max = -85.0 # 1
    level = 10.0 * ((max - dbLevel) / (max - min));
    print("max - dbLevel = " + str(max - dbLevel))
    print("max - min = " + str(max - min))
    print("level = " + str(level))
    return int(level)

def turn_leds_on(level):
    for led in range(1,level+1):
        turn_led_on(led)
    for led in range(level+1, 11):
        turn_led_off(led)

def turn_led_on(level):
    if (level == 1):
        led1.on()
    elif (level == 2):
        led1.on()
    elif (level == 3):
        led3.on()
    elif (level == 4):
        led4.on()
    elif (level == 5):
        led5.on()
    elif (level == 6):
        led6.on()
    elif (level == 7):
        led7.on()
    elif (level == 8):
        led8.on()
    elif (level == 9):
        led9.on()
    elif (level == 10):
        led10.on()        

def turn_led_off(level):
    if (level == 1):
        led1.off()
    elif (level == 2):
        led1.off()
    elif (level == 3):
        led3.off()
    elif (level == 4):
        led4.off()
    elif (level == 5):
        led5.off()
    elif (level == 6):
        led6.off()
    elif (level == 7):
        led7.off()
    elif (level == 8):
        led8.off()
    elif (level == 9):
        led9.off()
    elif (level == 10):
        led10.off()  


initialize()
lcd.clear()
lcd.display_lcd_line2("Scanning...")
while(True):
    wifilist = iw_parse.get_interfaces(interface="wlan1")
    if (is_network_in_list(wifilist, network_name)):
        network = get_network(wifilist, network_name)
        dbLevel = int(network["Signal Level"])
        level = get_level(dbLevel)
        lcd.display_lcd_line1("level = " + str(level))
        lcd.display_lcd_line2("Signal = " +  str(dbLevel))
        turn_leds_on(level)
    else:
        turn_leds_on(0)
        lcd.clear()
        lcd.display_lcd_line1("Out of Range")
        





