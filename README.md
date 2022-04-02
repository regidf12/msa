# Welcome to White-prince :crown:

[![White-prince](https://i.postimg.cc/BvYV1D9b/logogitorg0.png)](https://postimg.cc/t165KsgG)

You can follow me on my social networks:

:bird:[Twitter](https://twitter.com/White_prince_0)

:camera_flash: [Instagram](https://www.instagram.com/0xe_white_prince_ex0/)

:blue_book: [Facebook](https://www.facebook.com/profile.php?id=100023988285502)

:information_source: [Website](https://white-prince.github.io/Homepage/)

# White-prince Smart assistant :robot: :loud_sound:

The voice assistant will help you with the simplest tasks

## Installation :gear:
If you are cloning a project, run it first, otherwise you can download the source on the release page and skip this step.

    git clone https://github.com/White-prince/Moderbot.git
    
Before launching the bot, you will need to install the aiogram library

    pip install speech_recognition
    pip install googletrans
    pip install pyttsx3
    pip install wikipediaapi
    pip install webbrowser
    pip install traceback
    pip install wave
    pip install dotenv
    pip install vosk
    pip install googlesearch
    pip install pyowm
    
## Usege :information_source:
If the library doesn't install, try updating pip or installing pipwin

    pip install pipwin
    
Also, some libraries began to be installed using this method:

    pip install python-...
    
All you have to do is run the code

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
    
To work with weather command. You will need a key from the owm - ![OpenWeather](https://openweathermap.org/) website, to get it, register on the site.

        try:
        # использование ключа
        weather_api_key = os.getenv("WEATHER_API_KEY")
        open_weather_map = OWM(weather_api_key)

        # запрос данных о текущем состоянии погоды
        weather_manager = open_weather_map.weather_manager()
        observation = weather_manager.weather_at_place(city_name)
        weather = observation.weather

Hope this code helps you :crown:
