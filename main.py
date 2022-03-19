from vosk import Model, KaldiRecognizer
import speech_recognition
import pyttsx3
import wave
import json
import os


class VoiceAssistant:
    """
    Настройки голосового ассистента
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_assistant_voice():
    """
    Установка голоса по умолчанию (индекс может меняться в
    зависимости от настроек операционной системы)
    """
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознание
    """
    with mic:
        rec_data = ""

        # регулирование уровня окружающего шума
        rec.adjust_for_ambient_noise(mic, duration=2)

        try:
            print("Слушаю...")
            audio = rec.listen(mic, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Проверьте подключение микрофона")
            return

        # использование online-распознавания через Google
        try:
            print("Начал распознавать...")
            rec_data = rec.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Проверьте свое соеденение с интернетом")

        return rec_data


def use_offline_recognition():
    """
    Переключение на оффлайн-распознавание речи
    """
    rec_data = ""
    try:
        # проверка наличия модели на нужном языке в каталоге приложения
        if not os.path.exists("models/vosk-model-small-ru-0.4"):
            print("Пожалуйста, скачайте модель с:\n"
                  "https://alphacephei.com/vosk/models и распаковать как 'модель' в текущую папку.")
            exit(1)

        # анализ записанного в микрофон аудио
        wave_audio_file = wave.open("mic-results.wav", "rb")
        model = Model("models/vosk-model-small-ru-0.4")
        offline_rec = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_rec.AcceptWaveform(data):
                rec_data = offline_rec.Result()

                # получение данных распознанного текста из JSON-строки
                # (чтобы можно было выдать по ней ответ)
                rec_data = json.loads(rec_data)
                rec_data = rec_data["text"]
    except "err":
        print("Простите, сервес сейчас недоступен. Попробуйте позже!")

    return rec_data


if __name__ == "__main__":
    # инициализация инструментов распознавания и ввода речи
    rec = speech_recognition.Recognizer()
    mic = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Alice"
    assistant.sex = "female"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию
    setup_assistant_voice()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        voice_in = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_in)

        voice_in = voice_in.split(" ")
        command = voice_in[0]

        if command == "привет":
            play_voice_assistant_speech("Здравствуй")
