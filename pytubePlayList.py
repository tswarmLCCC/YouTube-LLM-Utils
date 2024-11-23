from pytubefix import Playlist

def extract_playlist_info(playlist_url, output_file):
    playlist = Playlist(playlist_url)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for video in playlist.videos:
            title = video.title
            url = video.watch_url
            file.write(f"{title}\n{url}\n\n")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    output_file = "playlist_info.txt"
    extract_playlist_info(playlist_url, output_file)
    print(f"Playlist information has been written to {output_file}")