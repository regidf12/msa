import speech_recognition  # распознание голоса
from vosk import Model, KaldiRecognizer  # offline mode for Vosk
import os  # работа с системой
import wave  # запись
import pyttsx3  # синтез речи


def setup_assistant_voice():
    """
     Установка голоса ассистента по умолчанию
    """
    voices = ttsEngine.getProperty("voices")


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_voice(*args: tuple):
    """
    Функция записи и распознавания сказанного
    """
    with microphone:
        recognized_data = ""

        #  регулирование внешних шумов
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print('Говорите')
            audio = recognizer.listen(microphone, 5, 5)
            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())
        except speech_recognition.WaitTimeoutError:
            print('Я не могу распознать что вы говорите, проверьте свой микрофон!')
            return

    #  online google распознавание
    try:
        print('Запись начата')
        recognized_data = recognizer.recognize_google(audio, language='ru').lower()
    except speech_recognition.UnknownValueError:
        pass

    #  offline mode - Vosk
    except speech_recognition.RequestError:
        print("Попытка offline распознавания...")
        recognized_data = offline_recognition()

    return recognized_data


def offline_recognition():
    """
    Функция offline записи и распознавания сказанного
    """
    recognized_data = ""

    try:
        if not os.path.exists("model/vosk-model-small-ru-0.22"):
            # проверка наличия модели на нужном языке
            print('У вас нет модуля для данной функции!')
            print('Устаеновите его тут:')
            print('https://alphacephei.com/vosk/models и распакуйте в папку с программой')
            exit(1)

        wave_audio_file = wave.open("microphone-result.wav", 'rb')
        model = Model("model/vosk-model-small-ru-0.22")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())
        date = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(date) > 0:
            if offline_recognizer.AcceptWaveform(date):
                recognized_data = offline_recognizer.Result()
    except NameError:
        print('К сожалению, распознание сейчас не возможно')

    return recognized_data


if __name__ == '__main__':

    #  распознавание и ввод речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    # синтез речи
    ttsEngine = pyttsx3.init()
    # установка голоса по умолчанию
    setup_assistant_voice()

    while True:
        #  старт записи речи с последующим записи речи
        voice_input = record_and_recognize_voice()
        os.remove("microphone-results.wav")
        print(voice_input)

        voice_input = voice_input.split(" ")
        command = voice_input[0]

        if command == "привет":
            play_voice_assistant_speech("Здравствуй")
