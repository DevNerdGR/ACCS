import requests
import time


def generateImageLP(width=1080, height=1920, filename="out.jpg"):
    """
    Returns height of generated image
    """
    try:
        r = requests.get(f"https://picsum.photos/{width}/{height}")
        f = open(f"./workFiles/{filename}", "wb")
        f.write(r.content)
        f.close
        time.sleep(2)
        return (width, height)
    except:
        print("Image cannot be generated")
