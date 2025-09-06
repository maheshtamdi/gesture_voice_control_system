import pyautogui

class MachineControl:
    def execute_action(self, action):
        print(f"Executing: {action}")
        if "click" in action:
            pyautogui.click()
        elif "up" in action:
            pyautogui.moveRel(0, -50)
        elif "down" in action:
            pyautogui.moveRel(0, 50)
        elif "left" in action:
            pyautogui.moveRel(-50, 0)
        elif "right" in action:
            pyautogui.moveRel(50, 0)
