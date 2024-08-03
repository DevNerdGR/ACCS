import pyttsx3
import gtts
import random
import time
from pyt2s.services import stream_elements

engine = pyttsx3.init()
altEngine = stream_elements.StreamElements()

pyt2sVoices = [
    "Brian",
    "Matthew",
    "Russell",
    "Amy",
    "Emma",
    "Kimberly"
]

def generateSpeech_pysstx3(funfact, intro="Did you know?", ending="Well, I guess now you do! Bye!", filename="out.mp3", voice=1):
    """
    voice: 1 for male, 2 for female, 3 for random
    WARNING: wait for method to return True before continuing
    """
    match voice:
        case 1:
            engine.setProperty("voice", engine.getProperty("voices")[0].id)
        case 2:
            engine.setProperty("voice", engine.getProperty("voices")[1].id)
        case 3:
            engine.setProperty("voice", engine.getProperty("voices")[random.randint(0, 2)].id)
        case _:
            raise Exception("Invalid voice mode set")
    
    engine.save_to_file(f"{intro} {funfact} {ending}", f"./workFiles/{filename}")
    engine.runAndWait()
    return True

def generateSpeech_gtts(script, lang="en", slow=False, filename="out.mp3"):
    gtts.gTTS(text=script, lang=lang, slow=False).save(f"./workFiles/{filename}")
    time.sleep(2)

def generateSpeech_pyt2s(script, voice="Brian", filename="out.mp3"):
    """
    Current implementation uses stream elements voice models
    """
    with open(f"./workfiles/{filename}", '+wb') as file:
        file.write(altEngine.requestTTS(script, voice=voice))

def makeFunfact(script, intro="Hey, did you know?", ending="Well, I guess now you do! Bye!"):
    return f"{intro} {script} {ending}"

def makeAdvice(script):
    return f"Hey, here's some advice. {script} If you found this useful, make sure to like, share and follow to help spread it to more people."

