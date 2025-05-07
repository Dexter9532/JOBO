import RPi.GPIO as GPIO
import time
im

# Pin configuration
LED_PIN = 18  # Replace with your GPIO pin number

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Set up PWM on the LED pin with a frequency of 100 Hz
pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)  # Start with LED off

try:
    while True:
        # Gradually increase brightness
        for duty_cycle in range(0, 101, 5):  # 0% to 100% in steps of 5
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
        
        # Gradually decrease brightness
        for duty_cycle in range(100, -1, -5):  # 100% to 0% in steps of 5
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    pwm.stop()
    GPIO.cleanup()