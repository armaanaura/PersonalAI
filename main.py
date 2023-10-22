# Import necessary libraries and modules
import os  # Operating system interface
import speech_recognition as sr  # Library for speech recognition
import win32com.client  # Library for text-to-speech
import webbrowser  # Library for opening web browsers
import openai  # OpenAI GPT-3 API
from config import apikey  # Assuming 'apikey' is a sensitive credential stored in a separate config file
import datetime  # Library for working with dates and times

# Configure OpenAI API key
openai.api_key = apikey

# Function to interact with the OpenAI GPT-3 model and save the response to a file
def ai(prompt):
    # Construct a header for the response file
    text = f"OpenAI response for Prompt: {prompt}\n*********************\n\n"

    # Generate a response using GPT-3
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Append the GPT-3 response to the text
    text += response["choices"][0]["text"]

    # Create a directory if it doesn't exist to store GPT-3 responses
    if not os.path.exists("OpenAi"):
        os.mkdir("OpenAi")

    # Save the OpenAI response to a file
    with open(f"OpenAi/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)

# Initialize the SAPI SpVoice for text-to-speech
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Main function for user interaction
def chat(query):
    global chatStr
    print(query)

    # Update the chat string with the user's query
    chatStr += f"Armaan: {query}\n J.A.R.V.I.S: "

    # Get a response from the OpenAI GPT-3 model
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Speak the response and print it
    speaker.Speak(response["choices"][0]["text"])
    print(response["choices"][0]["text"])

    # Update the chat string with the AI's response
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

# Function to capture user's voice command
def takeCommand():
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Use Google Speech Recognition to convert audio to text
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Error in accessing the Google Speech Recognition API. Check your internet connection.")
        return ""

# Main entry point of the script
if __name__ == '__main__':
    speaker.Speak('Hello, My name is Jarvis and I am your personal assistant')

    # Continuous loop for user interaction
    while True:
        query = takeCommand()
        boolean = True

        # Define a list of sites for web browsing
        sites = [["youtube", "https://www.youtube.com"], ["wikipeida", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]

        # Check if the user wants to open a specific website
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                boolean = False
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                break

        # If the user's query doesn't match any predefined actions, perform additional checks
        if boolean:
            if "the time" in query:
                # Get the current time and speak it out
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                speaker.Speak(f"Sir the time is {strfTime}")
            elif "using artificial intelligence".lower() in query.lower():
                # Invoke the OpenAI GPT-3 model with the user's query
                ai(prompt=query)
            elif "Bye jarvis".lower() in query.lower():
                # Exit the program if the user says goodbye
                exit()
            elif "forget everything".lower() in query.lower():
                # Reset the chat history if the user wants to forget everything
                chatStr = ""
            else:
                # If none of the predefined actions match, engage in a conversation using GPT-3
                print("Talking...")
                chat(query)
