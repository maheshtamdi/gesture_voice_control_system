import azure.cognitiveservices.speech as speechsdk

class VoiceController:
    def __init__(self, subscription_key="YOUR_AZURE_KEY", region="YOUR_REGION"):
        self.speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    def listen_command(self):
        print("Listening for voice command...")
        result = self.speech_recognizer.recognize_once_async().get()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text.lower()
        return None
