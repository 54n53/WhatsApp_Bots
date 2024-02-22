import pyautogui
import pywhatkit

#v1.1

# Open a browser tab with WhatsApp Web
# Syntax: phone number with country code, message, hour and minutes
pywhatkit.sendwhatmsg('+YYXXXXXXXXX', '⠀', HH, MM)
# pywhatkit.sendwhatmsg('$GROUP', 'First message to a group', HH, MM) 
# Does not work with group names, but it can be done with the group id, i.e. the sharing link.
pyautogui.press("Enter") # Sends the pre-programmed message
