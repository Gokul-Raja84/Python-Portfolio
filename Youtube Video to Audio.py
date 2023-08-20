# Import the necessary library
from pytube import YouTube

# Function to download a YouTube video
def download_video(video_url, download_location):
    try:
        # Create a YouTube object using the provided link
        yt = YouTube(video_url)

        # Get the stream with the highest resolution
        ys = yt.streams.get_highest_resolution()

        # Display a message indicating that the download is in progress
        print("Downloading...")

        # Download the video to the specified location
        ys.download(download_location)

        # Display a message to indicate that the download has been completed
        print("Download completed!!")
    except Exception as e:
        print("An error occurred:", str(e))

# Main function
def main():
    try:
        # Ask the user to input the YouTube video link
        video_url = input("Enter the YouTube video URL: ")

        # Specify the location where the video will be downloaded
        download_location = "Downloads\python"

        # Call the download_video function
        download_video(video_url, download_location)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
