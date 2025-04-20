#pyautogui are used for keyboard and mouse gui automatic interaction
#automation for gui 
import pyautogui
import time

# Give time to open the application
time.sleep(2)

# Press the Windows key to open the Start menu
pyautogui.hotkey('win')

# Type "Notepad" to search for it
pyautogui.write("Notepad")

# Press Enter to open Notepad
pyautogui.press('enter')

# Wait for Notepad to open
time.sleep(1)

# Type some text in Notepad
pyautogui.write("Hello, this is an automated text!")

# Wait for a few seconds before closing
time.sleep(3)

# Close the Notepad window by simulating ALT + F4
pyautogui.hotkey('alt', 'f4')



# commands
# pyautogui.write("")
# pyautogui.press("")
# pyautogui.click("")
# pyautogui.hotkey("")
# pyautogui.scroll("")