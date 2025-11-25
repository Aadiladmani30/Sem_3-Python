# Python Code

import serial
import time

# Set the COM port of your Arduino (Windows: COM3, Linux: /dev/ttyUSB0)
arduino_port = "COM3"
baud_rate = 9600

# Open serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow Arduino to reset

print("Type ON or OFF to control the LED. Type EXIT to stop.\n")

while True:
    command = input("Enter command (ON/OFF): ").strip().upper()

    if command == "EXIT":
        print("Exiting...")
        break

    if command in ["ON", "OFF"]:
        ser.write(command.encode())
        print(f"Sent: {command}")
    else:
        print("Invalid command! Please type only ON or OFF.")

ser.close()


# Arduino Code

# int ledPin = 13;  // Built-in LED

# void setup() {
#   Serial.begin(9600);
#   pinMode(ledPin, OUTPUT);
# }

# void loop() {
#   if (Serial.available()) {
#     String cmd = Serial.readStringUntil('\n');
#     cmd.trim();

#     if (cmd == "ON") {
#       digitalWrite(ledPin, HIGH);
#     }
#     else if (cmd == "OFF") {
#       digitalWrite(ledPin, LOW);
#     }
#   }
# }
