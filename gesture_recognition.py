import cv2
import mediapipe as mp
import pyautogui

class GestureController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def detect_gesture(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.mp_hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks)
                # Example gesture logic
                if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:
                    return "CLICK"
        return None
