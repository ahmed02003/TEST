from pytube import YouTube
import ssl
import re

# Enable SSL handling
ssl._create_default_https_context = ssl._create_unverified_context

def clean_url(url):
    # Extract video ID using regex
    video_id = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if video_id:
        return f'https://www.youtube.com/watch?v={video_id.group(1)}'
    return url

def download_video():
    # Your video URL
    original_url = "https://www.youtube.com/watch?v=OkVK611l0_A"
    url = clean_url(original_url)
    
    try:
        # First update pytube to latest version
        print("Starting download process...")
        yt = YouTube(url)
        
        # Select the best quality
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Download
        print(f"Downloading video...")
        stream.download()
        print("✨ Download successful! Check your current folder for the video file")
        
    except Exception as e:
        print(f"Technical details: {str(e)}")

if __name__ == "__main__":
    download_video()
