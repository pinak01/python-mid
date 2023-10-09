from gtts import gTTS
 
language="en"
text="FUCK MEE MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
speech=gTTS(text=text, lang=language, slow=False)
speech.save("text.mp3")