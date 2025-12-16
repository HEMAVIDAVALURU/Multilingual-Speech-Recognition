import tkinter as tk
from tkinter import ttk, messagebox
import speech_recognition as sr
from deep_translator import GoogleTranslator

# Initialize recognizer
recognizer = sr.Recognizer()

# Language mappings
speech_languages = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Telugu": "te-IN",
    "Tamil": "ta-IN"
}

translation_languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta"
}

def recognize_and_translate():
    input_lang = input_lang_var.get()
    output_lang = output_lang_var.get()

    if input_lang == "" or output_lang == "":
        messagebox.showwarning("Warning", "Please select both languages")
        return

    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            window.update()

            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

            # Speech to Text
            recognized_text = recognizer.recognize_google(
                audio,
                language=speech_languages[input_lang]
            )

            input_text_box.delete(1.0, tk.END)
            input_text_box.insert(tk.END, recognized_text)

            status_label.config(text="Translating...")
            window.update()

            # Text Translation (FIXED)
            translated_text = GoogleTranslator(
                source="auto",
                target=translation_languages[output_lang]
            ).translate(recognized_text)

            output_text_box.delete(1.0, tk.END)
            output_text_box.insert(tk.END, translated_text)

            status_label.config(text="Translation Successful ✅")

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio")
        status_label.config(text="Speech not recognized")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error occurred")

def clear_text():
    input_text_box.delete(1.0, tk.END)
    output_text_box.delete(1.0, tk.END)
    status_label.config(text="")

# GUI Setup
window = tk.Tk()
window.title("Speech Recognition & Translation")
window.geometry("600x520")
window.resizable(False, False)

# Title
tk.Label(
    window,
    text="Multilingual Speech Recognition & Translation",
    font=("Arial", 14, "bold")
).pack(pady=10)

# Language Selection
lang_frame = tk.Frame(window)
lang_frame.pack(pady=10)

tk.Label(lang_frame, text="Input Language").grid(row=0, column=0, padx=15)
tk.Label(lang_frame, text="Translate To").grid(row=0, column=1, padx=15)

input_lang_var = tk.StringVar(value="English")
output_lang_var = tk.StringVar(value="Hindi")

input_lang_cb = ttk.Combobox(
    lang_frame,
    textvariable=input_lang_var,
    values=list(speech_languages.keys()),
    state="readonly",
    width=15
)
input_lang_cb.grid(row=1, column=0)

output_lang_cb = ttk.Combobox(
    lang_frame,
    textvariable=output_lang_var,
    values=list(translation_languages.keys()),
    state="readonly",
    width=15
)
output_lang_cb.grid(row=1, column=1)

# Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="🎤 Speak & Translate",
    command=recognize_and_translate,
    bg="green",
    fg="white",
    width=20
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Clear",
    command=clear_text,
    width=10
).grid(row=0, column=1)

# Text Areas
tk.Label(window, text="Recognized Text").pack()
input_text_box = tk.Text(window, height=6, width=70)
input_text_box.pack(pady=5)

tk.Label(window, text="Translated Text").pack()
output_text_box = tk.Text(window, height=6, width=70)
output_text_box.pack(pady=5)

# Status
status_label = tk.Label(window, text="", fg="blue")
status_label.pack(pady=5)

# Run App
window.mainloop()
