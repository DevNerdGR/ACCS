import textwrap
import datetime

def wrapText(txt, width):
    wrapper = textwrap.TextWrapper(width=width)
    return "\n".join(wrapper.wrap(txt))

def generateFilename(type="fact"):
    """
    type argument specifies the type of content (fact/advice)
    """
    now = datetime.datetime.now()
    return f"{type}_video_{str(now.day).zfill(2)}{str(now.month).zfill(2)}{now.year}_{now.hour}_{now.minute}_{now.second}"