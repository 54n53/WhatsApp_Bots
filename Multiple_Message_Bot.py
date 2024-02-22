import pywhatkit
import pyautogui
from datetime import datetime
import time
import pause

#v1.1

# Read messages from file
with open('messages_to_send.txt', 'r') as file:
    messages = file.readlines()

# Counter for the number of messages sent.
count = 0

# Start time of sending messages. It must be prior to the time of sending the first message
# Sintax: year, month, day, hour, minute, second
pause.until(datetime(YYYY, MM, DD, HH, MM, SS))

# Send the first message
first_message = messages.pop(0).strip()  # Get the first message from the file
pywhatkit.sendwhatmsg('+YYXXXXXXXXX', first_message, HH, MM)  # #Syntax: phone number with country code, message, hour and minutes
pyautogui.press("Enter")

# Function to calculate wait time based on number of words
def calculate_delay(message):
    words = message.split()
    word_count = len(words)
    # Adjust these values according to your preference.
    base_delay = 1,25  # Base delay.
    delay_per_word = 0.6  # Additional delay per word in seconds.
    return base_delay + (delay_per_word * word_count)


for message in messages:
    count += 1
    # Calculate the waiting time according to the number of words in the message.
    delay = calculate_delay(message)
    # Writing message
    time.sleep(delay)
    pyautogui.typewrite(message.strip())
    pyautogui.press("Enter")

# Confirmation message
print(f"{count} mensajes have been sent.")

