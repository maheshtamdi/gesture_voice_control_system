from gesture_recognition import GestureController
from voice_recognition import VoiceController
from gui import ControlGUI
from control import MachineControl

def main():
    # Initialize controllers
    gesture = GestureController()
    voice = VoiceController()
    machine = MachineControl()

    # Start GUI
    gui = ControlGUI(gesture, voice, machine)
    gui.run()

if __name__ == "__main__":
    main()
