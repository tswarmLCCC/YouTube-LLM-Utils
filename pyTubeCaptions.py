from pytubefix import YouTube


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

def extract_captions(video_list):
    for title, url in video_list:
        video = YouTube(url)
        caption = video.captions.get_by_language_code('en')
        if caption:
            caption_text = caption.generate_srt_captions()
            with open(f"{title}_captions.srt", 'w', encoding='utf-8') as file:
                file.write(caption_text)
        else:
            print(f"No captions found for video: {title}")



        
if __name__ == "__main__":
    video_list = [

            ("COSC 2409  25S20  Integers Floats and Typing", "https://youtube.com/watch?v=fBGEYOn-YYc"),
            ("COSC 2409  25S21  Basic Strings", "https://youtube.com/watch?v=7gR-iycVPN8"),
            ("COSC 2409  25S22  Slicing Strings", "https://youtube.com/watch?v=hP0utz5y_Tc"),
            ("COSC 2409  25S23 Lists Intro", "https://youtube.com/watch?v=DdBHzfjJ6Q0"),
            ("COSC 2409  25S24 Programing Differences", "https://youtube.com/watch?v=4pk98imvIH8"),
                    # Add more titles and URLs as needed
    ]
    extract_captions(video_list)
    print("Captions have been extracted to files.")


