import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3 as robot

# Inisialisasi objek
engine = robot.init()
rekam = sr.Recognizer()

def bicara_dan_translate(asal, target):
    translator = GoogleTranslator(source=asal, target=target)
    with sr.Microphone() as sc:
        print("Mendengarkan...")
        dengar = rekam.listen(sc)

    try:
        text = rekam.recognize_google(dengar, language=asal)
        print("Request: ", text)
        hasil = translator.translate(text)
        print("respon: ",hasil)
        BotSuara(hasil)
    except sr.UnknownValueError:
        print("Maaf, saya tidak bisa memahami apa yang Anda ucapkan.")
    except sr.RequestError as e:
        print(f"Maaf, sepertinya Anda tidak dalam jangkauan internet: {e}")

def BotSuara(text):
    suara = engine.getProperty("voices")
    for x in suara:
        if "id" in x.languages:
            engine.setProperty("voice", x.id)
            break
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def banner():
    print("[id] Indonesia to English")
    print("[en] English to Indonesia")

def main():
    banner()
    inputan = input("Masukkan pilihan Anda: ").strip()

    if inputan == "id":
        bicara_dan_translate("id", "en")
    elif inputan == "en":
        bicara_dan_translate("en", "id")
    else:
        print("Pilihan tidak valid. Harap pilih antara 'id' atau 'en'.")

if __name__ == "__main__":
    main()
