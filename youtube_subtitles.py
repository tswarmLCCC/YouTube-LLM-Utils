#https://pytubefix.readthedocs.io/en/latest/index.html
#https://pytubefix.readthedocs.io/en/latest/user/captions.html


from pytubefix import YouTube
from pytubefix.cli import on_progress

nightwish = 'https://www.youtube.com/watch?v=pvkYwOJZONU'
#nightwish:  https://www.youtube.com/watch?v=pvkYwOJZONU
ollamaVid = 'https://www.youtube.com/watch?v=5kMF6DEd3KM'


def returnEveryThirdLine(inString):
    """
    Returns every third line from the given input string.

    Parameters:
    - inString (str): The input string containing multiple lines.

    Returns:
    - str: A string containing every third line from the input string.
    """
    lines = inString.split('\n')
    every_third_line = lines[2::3]
    return '\n'.join(every_third_line)
    
def returnEveryFourthLineFromFile(filePath):
    """
    Returns every third line from the given file.

    Parameters:
    - filePath (str): The path to the file.

    Returns:
    - str: A string containing every third line from the file.
    """
    with open(filePath, 'r') as file:
        lines = file.readlines()
    every_third_line = lines[2::4]
    return ''.join(every_third_line)

# Example usage:
# result = returnEveryThirdLineFromFile('path/to/your/file.txt')
# print(result)
yt = YouTube(ollamaVid)
yt = YouTube(nightwish)
#print(yt.vid_details)

subtitles = yt.captions
#print(subtitles)

languageCodes = ['a.en', 'en']
caption = None
i = 0 #len(languageCodes)

while not caption:
    # will be caption = yt.captions[languageCodes[i]] soon - need to get first one
    caption = yt.captions.get_by_language_code(languageCodes[i])
    i +=1


#if not caption:
#    caption = yt.captions.get_by_language_code('en')

if caption:
    caption.save_captions("captions2.txt")
    result = returnEveryFourthLineFromFile('captions2.txt').replace('\n', ' ')
    with open("captionsTrim.txt", 'w') as file:
        file.write(result)
else:
    print("Could not find captions for: ", ollamaVid)
