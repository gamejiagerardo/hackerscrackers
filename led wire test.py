from gpiozero import LED

from time import sleep

def allLights( action ):
    if action == "on":
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        led5.on()
        led6.on()
        led7.on()
        led8.on()
        led9.on()
        led10.on()
    else:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        led6.off()
        led7.off()
        led8.off()
        led9.off()
        led10.off()
    return

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
buzzer = LED(27)



led1.on()

