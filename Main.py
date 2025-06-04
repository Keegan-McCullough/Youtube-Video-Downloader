import os
import yt_dlp

if not os.path.exists('YT Downloader Videos'):
    os.makedirs('YT Downloader Videos')

while True:
    url = input("Welcome to the YouTube Video Downloader!\nCopy the URL of the YouTube video you want to download and press Enter to continue: ").strip()

    if not url.startswith("https://www.youtube.com/watch?") and not url.startswith("http://www.youtube.com/watch?"):
        print("Invalid URL, please enter a valid YouTube video URL.")
        continue

    try:
        ydl_opts = {'outtmpl': 'downloads/%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

    another = input("Do you want to download another video? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Thank you for using the YouTube Video Downloader!")
        break
