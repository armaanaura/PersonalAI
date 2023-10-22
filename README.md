# PersonalAI
# J.A.R.V.I.S - Personal AI Assistant

## Overview

J.A.R.V.I.S is a Python-based personal AI assistant that leverages OpenAI's GPT-3 model for natural language understanding and generation. It can perform various tasks, including voice recognition, web browsing, time reporting, and engaging in conversations using artificial intelligence.

## Features

- **Voice Recognition:** J.A.R.V.I.S can recognize voice commands using the SpeechRecognition library and Google Speech Recognition API.

- **Text-to-Speech:** The assistant uses the SAPI SpVoice library to convert text responses into speech for user interaction.

- **Web Browsing:** You can command J.A.R.V.I.S to open specific websites such as YouTube, Wikipedia, or Google.

- **Time Reporting:** Ask J.A.R.V.I.S about the current time, and it will provide you with the current time using the datetime library.

- **AI Conversation:** J.A.R.V.I.S can engage in conversations using the OpenAI GPT-3 model, providing intelligent responses based on the input it receives.

- **Memory Functionality:** The assistant can save conversations and responses from the OpenAI model to files for later reference.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/J.A.R.V.I.S.git
   ```

2. Install the required Python libraries:

   ```bash
   pip install speech_recognition win32com.client openai
   ```

3. Obtain an API key from OpenAI and replace the placeholder in `config.py` with your actual API key.

4. Run the `JARVIS.py` script:

   ```bash
   python JARVIS.py
   ```

## Usage

- **Voice Commands:** Speak commands such as "Open YouTube," "What's the time," or engage in conversations with J.A.R.V.I.S.

- **Web Browsing:** Command J.A.R.V.I.S to open specific websites by saying "Open [website name]."

- **AI Conversation:** Ask J.A.R.V.I.S questions or provide prompts for engaging in intelligent conversations.

- **Memory Functionality:** Conversations with J.A.R.V.I.S are saved in the "OpenAi" directory for future reference.

## Customization

- **Adding Websites:** Extend the list of websites in the `sites` variable within the script to include more options for web browsing.

- **Enhancing Conversations:** Adjust the OpenAI GPT-3 parameters in the `ai` and `chat` functions for different conversation styles and responses.

## Dependencies

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Library for performing speech recognition.

- [win32com.client](https://pypi.org/project/pywin32/): Python extensions for Windows, used for text-to-speech.

- [OpenAI](https://beta.openai.com/docs/): GPT-3 API for natural language processing.

## Contributions

Contributions are welcome! Feel free to open issues, suggest improvements, or submit pull requests to enhance the functionality and usability of J.A.R.V.I.S.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This project is developed for educational and personal use. Use the OpenAI GPT-3 API responsibly and comply with OpenAI's usage policies.
