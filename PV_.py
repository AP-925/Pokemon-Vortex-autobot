import pyautogui
import time
from pyscreeze import Box

button1x = 630       # First continue button on battle page. (X coordinate on screen)
button1y = 628       # First continue button on battle page. (Y coordinate on screen)
attackx = 564        # Attack button on screen after clicking firsts continue button.
attacky = 352
rebattlex = 575      # rebattle button X
rebattley = 203      # rebattle button Y

number_of_battles=5    # Number of battles you want to perform.
while(number_of_battles):
    mons_to_defeat = 6 # 6 pokemons to defeat in opponent team.
    while mons_to_defeat != 0:
        time.sleep(0.65)
        pyautogui.moveTo(button1x,button1y,duration=0.3)       # Continue 1 button
        pyautogui.click(button1x,button1y,clicks=1)
        time.sleep(1.15)

        time.sleep(1.0)
        pyautogui.moveTo(attackx,attacky,duration=0.55)       # Attack button
        pyautogui.click(attackx,attacky,clicks=1)             # Clicks the center of attack button

        time.sleep(1.0)
        num=0
        continue_change = pyautogui.locateOnScreen("C:/Users/panse/Desktop/continue2.png", confidence=0.75)
        if continue_change is None:
            while continue_change is None:                    # Runs until image is located on screen.
                num+=1
                print("Failed, locating again : ",num)
                continue_change = pyautogui.locateOnScreen("C:/Users/panse/Desktop/continue2.png", confidence=0.72)
        else:
            continue2 = pyautogui.center(continue_change)

        time.sleep(0.3)
        print(continue_change)
        print(continue2)
        continuex, continuey = continue2
        pyautogui.moveTo(continuex,continuey,duration=0.55)   # Continue 2 button
        pyautogui.click(continuex,continuey,clicks=1)
        mons_to_defeat = mons_to_defeat-1

    time.sleep(1.5)
    pyautogui.moveTo(rebattlex,rebattley,duration=0.65)    # Rebattle opponent button
    pyautogui.click(rebattlex,rebattley,clicks=1)
    number_of_battles = number_of_battles-1
