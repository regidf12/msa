# Welcome to White-prince :crown:

 [![White-prince](https://github.com/White-prince/White-prince/blob/main/assets/vk-head-andrew.png?raw=true)](http://white-prince.ru/)

You can follow me on my social networks:

[![Twitter](https://img.shields.io/badge/-Twitter-131313?style=for-the-badge&logo=Twitter)](https://twitter.com/White_prince_0)

[![Instagram](https://img.shields.io/badge/-Instagram-131313?style=for-the-badge&logo=Instagram)](https://www.instagram.com/0xe_white_prince_ex0/)
  
[![Telegram](https://img.shields.io/badge/-Telegram-131313?style=for-the-badge&logo=Telegram)](https://t.me/Dark_Hub_info)

[![VK](https://img.shields.io/badge/-VK-131313?style=for-the-badge&logo=VK)](https://vk.com/id333667069)

[![Facebook](https://img.shields.io/badge/-Facebook-131313?style=for-the-badge&logo=Facebook)](https://www.facebook.com/profile.php?id=100023988285502)

# White-prince Smart assistant :robot: :loud_sound:

The voice assistant will help you with the simplest tasks.

## Installation :gear:
If you are cloning a project, run it first, otherwise you can download the source on the release page and skip this step.

    https://github.com/White-prince/msa.git
    
Before launching the bot, you will need to install the aiogram library.

    from vosk import Model, KaldiRecognizer
    from pyowm import OWM
    from dotenv import load_dotenv
    import speech_recognition
    import pyttsx3
    import wikipediaapi
    import random
    import webbrowser
    import traceback
    import json
    import wave

## Usege :information_source:
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
