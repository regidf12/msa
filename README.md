# Welcome to Regidf

# Smart assistant :robot: :loud_sound:

The voice assistant will help you with the simplest tasks.

## Installation :gear:
If you are cloning a project, run it first, otherwise you can download the source on the release page and skip this step.

    https://github.com/White-prince/msa.git
    
Before launching the bot, you will need to install the aiogram library.

    from vosk import Model, KaldiRecognizer
    import speech_recognition
    import pyttsx3
    import json
    import wave

## Usege :information_source:

pip install PyAudio

If the library doesn't install, try updating pip or installing pipwin.

    pip install pipwin
    
Also, some libraries began to be installed using this method:

    pip install python-...
    
All you have to do is run the cod.

In order to start in the terminal, write the command:

    python main.py
    
The bot will start listening to you, tell it one of these commands:

    "hello", "hey", "hi", "morning", "привет" - Greetings
    "bye", "goodbye", "quit", "exit", "stop", "пока" - Parting
    "search", "google", "find", "найди" - Search
    "video", "youtube", "watch", "видео" - Video search
    "wikipedia", "definition", "about", "определение", "википедия" - Search wikipedia
    "translate", "interpretation", "translation", "перевод", "перевести", "переведи" - translater
    "language", "язык" - Language
    "weather", "forecast", "погода", "прогноз" - Weather
    
To work with weather command. You will need a key from the owm - [OpenWeather](https://openweathermap.org/) website, to get it, register on the site.

        try:
        # использование ключа
        weather_api_key = os.getenv("WEATHER_API_KEY")
        open_weather_map = OWM(weather_api_key)

        # запрос данных о текущем состоянии погоды
        weather_manager = open_weather_map.weather_manager()
        observation = weather_manager.weather_at_place(city_name)
        weather = observation.weather
        
If an oops sound occurs when a command is invoked, check the logs.

Hope this code helps you :crown:
