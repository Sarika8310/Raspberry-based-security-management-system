# Raspberry Pi Security Management System

Our project develops a security system with a Raspberry Pi as the central controller, integrating a 4x4 keypad, buzzer, USB camera, servo motor, and PIR sensor. Incorrect keypad entries trigger the buzzer and capture images for identification. Correct entries activate the servo motor to release the latch. Python scripts manage interactions, utilizing RPi.GPIO and OpenCV. Security measures include passcode encryption and a timeout mechanism to deter attacks. Rigorous testing ensures functionality, with thorough documentation provided. The project aims to enhance home security, prioritizing safety and user-friendliness.

## Hardware Setup

1. Raspberry Pi 4 Model B
2. 4x4 Keypad (Connected via GPIO pins)
3. Buzzer (Connected to GPIO pin 23)
4. USB Camera (Connected via USB port)
5. Servo Motor (Connected to GPIO pin 18)
6. PIR Sensor (Connected to GPIO pin 24)

## Installation

1. Clone the repository to your Raspberry Pi.
2. Ensure that Python 3 and the required libraries are installed:
   - RPi.GPIO
   - OpenCV (opencv-python)
3. Connect the hardware components according to the provided instructions.
4. Run the Python script to activate the security system.

## Usage

1. Enter the correct passcode on the keypad to activate the servo motor and release the latch.
2. Incorrect passcode entries trigger the buzzer and capture images with the USB camera.
3. Motion detection by the PIR sensor also triggers image capture.

