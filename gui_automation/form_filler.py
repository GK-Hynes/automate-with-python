#! python3
# form_filler.py - Automatically fills in a simple Google form

import pyautogui, time

form_data = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
    'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
    ]

pyautogui.PAUSE = 0.5
print('Ensure the browser window is active and the form is loaed!')

for person in form_data:
    # Give the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C<<<')
    time.sleep(5)

    print(f"Entering {person['name']} info")
    pyautogui.write(['\t', '\t'])

    # Fill out Name field
    pyautogui.write(person['name'] + '\t')

    # Fill out Greatest Fear(s) field
    pyautogui.write(person['fear'] + '\t')

    # Fill out the Source of Wizard's Power field
    if person['source'] == 'wand':
        pyautogui.write(['down', '\n', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\n', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', '\n', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', '\n', '\t'], 0.5)

    # Fill out Robocop field
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)

    # Fill out Additional Comments
    pyautogui.write(person['comments'] + '\t')

    # 'Click' Submit by pressing Enter
    # Wait for the button to activate
    time.sleep(0.5) 
    pyautogui.press('enter')

    # Wait until form page as loaded
    print('Submitted form')
    time.sleep(5)

    # 'Click' the 'Submit another response' link
    pyautogui.write(['\t', '\n'])