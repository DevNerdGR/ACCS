import src.speechGenerator
import src.factGenerator
import src.adviceGenerator
import src.imageGenerator
import src.utils
import random
import sys
from moviepy.editor import *

#CONSTANTS
FONTSIZE = 50
FONTFAMILY = "Rockwell"
TTSVOICES = src.speechGenerator.pyt2sVoices

BANNER = """
============================================================
           _____ _____  _____ 
     /\   / ____/ ____|/ ____|
    /  \ | |   | |    | (___  
   / /\ \| |   | |     \___ \ 
  / ____ \ |___| |____ ____) |
 /_/    \_\_____\_____|_____/ 
                                               
Automatic Content Creation System (ACCS), v1.0 by DevNerdGR.

This program is used to create short-form videos that feature motivational quotes or fun facts.
Note: THE USE OF THIS PROGRAM SHOULD BE FOR EDUCATIONAL PURPOSES ONLY!! Any damages caused by the use of this program (e.g. loss of account for posting bot/spam content, etc.) shall be fully borne by the user.
============================================================
"""

HELP = """
On your first run of the program, you should ensure all requirements are installed on your device by running: "pip3 install requirements.txt"

To run the program, simply enter the following command into your shell (make sure you are in the correct directory!): "python3 reelGenerator.py <number of videos> <type of content>"

Arguments:
    Number of videos:
        Number of videos you would like to generate (value should be >= 1)
    Type of content:
        Type of content you would like to generate. (Currently supported types are "fact" for fun fact videos and "advice" for advice related videos)
"""

def generateReel(mode="auto", contentType="fact"):
    """
    mode: specifies if the program will ask the user for manual verification of prompt to ensure content published is safe
    contentType specifies type of content to generate, either fun facts ("fact") or advices ("advice")
    """
    #Get filename
    print("\n\nGenerating filename...")
    comFilename = src.utils.generateFilename(type=contentType)

    #Get background image
    print("Getting background image...")
    width = src.imageGenerator.generateImageLP(filename=f"{comFilename}.jpg")[0]

    #Get fact
    print(f"Retrieving {contentType}...")
    match contentType:
        case "fact":
            fact = src.factGenerator.getFunfact()
            if mode.lower() == "safe" and input(f"\nCurrent fact: \n{fact}\nAccept fact? [y/n]: ").lower() == "n":
                return generateReel(mode="safe", contentType=contentType)
            content = "Did you know??\n\n" + src.utils.wrapText(fact, int(width / FONTSIZE))
            script = src.speechGenerator.makeFunfact(fact)
        case "advice":
            advice = src.adviceGenerator.getAdvice()
            if mode.lower() == "safe" and input(f"\nCurrent advice: \n{advice}\nAccept fact? [y/n]: ").lower() == "n":
                return generateReel(mode="safe", contentType=contentType)
            content = "Save advice for later:\n\n" + src.utils.wrapText(advice, int(width / FONTSIZE))
            script = src.speechGenerator.makeAdvice(advice)
        case _:
            raise Exception("Invalid content type! Available content types are fact and advice")
    #Get narration
    print("Creating voiceover...")
    src.speechGenerator.generateSpeech_pyt2s(script=script, filename=f"{comFilename}.mp3", voice=TTSVOICES[random.randint(0, len(TTSVOICES) - 1)])


    #Video creation
    audio = AudioFileClip(f"./workFiles/{comFilename}.mp3")

    bg = ImageClip(f"./workFiles/{comFilename}.jpg")

    txt = TextClip(content, color="white", bg_color="black", font=FONTFAMILY, fontsize=FONTSIZE).set_duration(audio.duration)
    txt = txt.set_position("center")

    video = CompositeVideoClip(clips = [bg, txt], size=(bg.size))
    video = video.set_audio(audio)
    video = video.set_duration(audio.duration)


    video.write_videofile(f"./out/{comFilename}.mp4", codec = "mpeg4", threads = 12, bitrate = "8000k", fps=24)
    video.close()

    return comFilename

if __name__ == "__main__":
    print(BANNER)
    if len(sys.argv) != 3 or not sys.argv[1].isnumeric or int(sys.argv[1]) < 1:
            print("Invalid arguments! See the following to resolve the issue:")
            print(HELP)
            exit(1)
    for i in range(0, int(sys.argv[1])):
        print(f"\n\nMaking reel {i + 1} of {sys.argv[1]}")
        generateReel(contentType=sys.argv[2])