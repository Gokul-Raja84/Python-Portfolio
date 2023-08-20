# Import the necessary library
from pytube import YouTube

# Ask the user to input the YouTube video link
link = input("Enter the link of the YouTube video: ")

# Create a YouTube object using the provided link
yt = YouTube(link)

# Get the stream with the highest resolution
ys = yt.streams.get_highest_resolution()

# Display a message indicating that the download is in progress
print("Downloading...")

# Specify the location where the video will be downloaded
download_location = "Downloads\python"
ys.download(download_location)

# Display a message to indicate that the download has been completed
print("Download completed!!")