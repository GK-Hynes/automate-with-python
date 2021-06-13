import pyautogui, time
import os

os.environ['DISPLAY'] = ':0'

time.sleep(5)

# Click to make the window active
pyautogui.click()
distance = 300
change = 20
while distance > 0:
    # Move right
    pyautogui.drag(distance,0,duration=0.2)
    distance = distance - change
    # Move down
    pyautogui.drag(0,distance,duration=0.2)
    # Move left
    pyautogui.drag(-distance,0,duration=0.2)
    distance = distance - change
    # Move up
    pyautogui.drag(0, -distance, duration=0.2)

