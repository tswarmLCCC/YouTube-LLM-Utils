#https://pytubefix.readthedocs.io/en/latest/index.html
#https://pytubefix.readthedocs.io/en/latest/user/captions.html

#import logging
from pytubefix import YouTube

# Set up logging
#logging.basicConfig(level=logging.DEBUG)

nightwish = 'https://www.youtube.com/watch?v=pvkYwOJZONU'
#nightwish:  https://www.youtube.com/watch?v=pvkYwOJZONU
ollamaVid = 'https://www.youtube.com/watch?v=5kMF6DEd3KM'
gitHubVid = 'https://www.youtube.com/watch?v=6CwH_pXl7M0'

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

def getFirstCaption(inYouTube = YouTube(gitHubVid)):
    subtitles = inYouTube.captions
    languageCodes = ['a.en', 'en']
    caption = None
    i = 0 #len(languageCodes)

    while not caption:
        # will be caption = yt.captions[languageCodes[i]] soon - need to get first one
        caption = subtitles.get_by_language_code(languageCodes[i])
        i +=1
        
    return caption

def makeNiceFilename(inString):
    return inString.replace(' ', '_').replace(':', '_').replace('\'', '').replace('\"', '').replace('?', '').replace('!', '').replace(',', '').replace('.', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('/', '_').replace('\\', '_').replace('|', '_').replace('<', '_').replace('>', '_').replace('~', '_').replace('`', '_').replace('=', '_').replace('+', '_').replace('*', '_').replace('&', '_').replace('^', '_').replace('%', '_').replace('$', '_').replace('#', '_').replace('@', '_').replace('!','_')

def extractCaptionFromYTURL(inURL = gitHubVid):
    
    yt = YouTube(inURL)
    caption = getFirstCaption(yt)
    #logging.debug("Getting Captions for video: %s", yt.title)
    
    if caption:
        caption.save_captions("captions/captions2.txt")
        result = returnEveryFourthLineFromFile('captions/captions2.txt').replace('\n', ' ')
        trimFileName = "captions/" + makeNiceFilename(yt.title) + '_captions.txt'
        #trimFileName = 'captions/small'
        with open(trimFileName, 'w') as file:
            file.write(result)
    else:
        print("Could not find captions for: ", ollamaVid)

def extract_playlist_title_url(playlist_url):
    from pytubefix import Playlist

    playlist = Playlist(playlist_url)
    
    outList = []
    for video in playlist.videos:
        title = video.title
        url = video.watch_url
        outList.append((title, url))
        #logging.debug(f"Title: {title}, URL: {url}")
    #logging.debug(outList)
    return outList

def captionsFromVideoList(
        video_list = [

            ("COSC 2409  25S20  Integers Floats and Typing", "https://youtube.com/watch?v=fBGEYOn-YYc"),
            ("COSC 2409  25S21  Basic Strings", "https://youtube.com/watch?v=7gR-iycVPN8"),
            ("COSC 2409  25S22  Slicing Strings", "https://youtube.com/watch?v=hP0utz5y_Tc"),
            ("COSC 2409  25S23 Lists Intro", "https://youtube.com/watch?v=DdBHzfjJ6Q0"),
            ("COSC 2409  25S24 Programing Differences", "https://youtube.com/watch?v=4pk98imvIH8"),
                    # Add more titles and URLs as needed
    ]
):
    for title, url in video_list:
        #logging.debug("Getting Captions for video: %s", title)
        extractCaptionFromYTURL(url)
        
    


if __name__ == "__main__":
    #captionsFromVideoList()
    allCOSCvids = extract_playlist_title_url("https://www.youtube.com/watch?v=VRv07luFcxI&list=PLRhd0Rs1v-Bc4cMeWhjA7fBhZBDkGHpT9")
    captionsFromVideoList(allCOSCvids)
    print("Captions have been extracted to files.")