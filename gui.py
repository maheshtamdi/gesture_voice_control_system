import tkinter as tk
from threading import Thread

class ControlGUI:
    def __init__(self, gesture, voice, machine):
        self.gesture = gesture
        self.voice = voice
        self.machine = machine
        self.root = tk.Tk()
        self.root.title("Gesture & Voice Control System")

        tk.Label(self.root, text="Gesture & Voice Control").pack(pady=10)
        tk.Button(self.root, text="Start Control", command=self.start_services).pack(pady=5)

    def start_services(self):
        Thread(target=self.run_gesture).start()
        Thread(target=self.run_voice).start()

    def run_gesture(self):
        while True:
            gesture = self.gesture.detect_gesture()
            if gesture:
                self.machine.execute_action(gesture)

    def run_voice(self):
        while True:
            command = self.voice.listen_command()
            if command:
                self.machine.execute_action(command)

    def run(self):
        self.root.mainloop()

