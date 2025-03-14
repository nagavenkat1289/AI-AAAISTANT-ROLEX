# AI Assistant

Rolex is a versatile AI assistant designed to help you with various tasks through voice commands. It can recognize speech, respond with text-to-speech, and perform a variety of functions such as opening applications, setting alarms, fetching weather updates, and more.

## Features

1. **Speech Recognition**: Understands and processes voice commands.
2. **Text-to-Speech**: Responds with spoken text.
3. **Open Applications**: Opens common applications like Chrome, Notepad, Word, Excel, and Spotify.
4. **Set Alarms**: Sets alarms for specified times.
5. **Schedule Meetings**: Opens meeting links at specified times.
6. **Weather Updates**: Provides current weather information for specified cities.
7. **News Updates**: Reads out the latest news headlines.
8. **Currency Conversion**: Converts amounts between different currencies.
9. **Tell Jokes and Quotes**: Reads out random jokes or motivational quotes.
10. **Send Emails**: Sends emails using SMTP.
11. **WolframAlpha Queries**: Answers factual questions using WolframAlpha API.
12. **Wikipedia Search**: Fetches summaries from Wikipedia.
13. **Translate Text**: Translates text from one language to another.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nagavenkat1289/AI-Assistant.git
   cd AI-Assistant
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add the following environment variables:
   ```
   WEATHER_API_KEY=your_openweathermap_api_key
   NEWS_API_KEY=your_newsapi_key
   EMAIL_ADDRESS=your_email_address
   EMAIL_PASSWORD=your_email_password
   WOLFRAM_APP_ID=your_wolframalpha_app_id
   ```

## Usage

1. Run the AI assistant:
   ```bash
   python main.py
   ```

2. Speak your command after the prompt. Some example commands:
   - "Open Chrome"
   - "Set alarm for 07:00"
   - "Weather in New York"
   - "News update"
   - "Convert 100 USD to EUR"
   - "Tell me a joke"
   - "Send email to example@example.com subject Test body This is a test email"
   - "Wolfram what is the capital of France"
   - "Search Wikipedia for Python programming"
   - "Translate Hello to Spanish"

## Detailed Instructions for Each Feature

### Speech Recognition
- The assistant listens for your command and processes it using Google's speech recognition service. Ensure your microphone is working properly.

### Text-to-Speech
- Responses are given using the pyttsx3 text-to-speech engine. You can customize the voice by modifying the `speak` function in the script.

### Open Applications
- The assistant can open specified applications installed on your system. Ensure the paths in the `app_paths` dictionary point to the correct executable files.

### Set Alarms
- Set alarms in the format "HH:MM". The assistant will notify you when it's time.

### Schedule Meetings
- Provide the meeting time and link. The assistant will open the link at the specified time.

### Weather Updates
- Get the current weather information for any city. Ensure you have a valid OpenWeatherMap API key.

### News Updates
- Get the latest news headlines. Ensure you have a valid News API key.

### Currency Conversion
- Convert amounts between different currencies using the exchange rate API.

### Tell Jokes and Quotes
- Hear random jokes or motivational quotes to lighten up your day.

### Send Emails
- Send emails using your Gmail account. Ensure you have provided your email credentials in the `.env` file.

### WolframAlpha Queries
- Get factual answers to your questions using the WolframAlpha API.

### Wikipedia Search
- Fetch summaries from Wikipedia for any topic.

### Translate Text
- Translate text from one language to another using the translate API.

## Troubleshooting

- **Speech Recognition Issues**: Ensure your microphone is working and properly configured. Check internet connectivity for Google's speech recognition service.
- **API Key Errors**: Ensure all API keys are correctly set in the `.env` file.
- **Email Sending Issues**: Verify your email credentials and ensure less secure app access is enabled in your email account settings.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License.
