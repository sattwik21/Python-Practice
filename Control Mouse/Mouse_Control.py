import pyautogui
distance = 360
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)  # Move right
    distance = distance-8
    pyautogui.dragRel(0, distance, duration=0.1)  # Move down
    distance = distance-8
    pyautogui.dragRel(-distance, 0, duration=0.1)  # Move left
    distance = distance-8
    pyautogui.dragRel(0, -distance, duration=0.1)  # Move right5
    distance = distance - 8
