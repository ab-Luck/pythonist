import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech_from_mic():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            # Recognize the speech using Google's speech recognition API
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an error with the request.")

# Call the function
recognize_speech_from_mic()
