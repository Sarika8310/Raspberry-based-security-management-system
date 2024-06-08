import RPi.GPIO as GPIO
import time
import cv2

# Define GPIO pins
PIR_PIN = 24  # PIR sensor pin
BUZZER_PIN = 23  # Buzzer pin
SERVO_PIN = 18  # Servo motor pin

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize USB camera
camera = cv2.VideoCapture(0)

# Function to handle incorrect keypad entries
def handle_incorrect_entry():
    print("Incorrect entry! Activating buzzer and capturing image...")
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(2)  # Buzzer activation duration
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    _, image = camera.read()
    cv2.imwrite("intruder.jpg", image)
    print("Image captured.")

# Main loop
try:
    while True:
        if GPIO.input(PIR_PIN):
            handle_incorrect_entry()
            time.sleep(5)  # Delay to prevent repeated triggering
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
    # Release camera
    camera.release()
