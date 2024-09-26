import re 

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def extract_video_id(url: str) -> str:
    """
    Extracts the video ID from a YouTube URL.
    """
    # Ensure the URL is converted to a string before regex search
    url_str = str(url)
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    matches = re.search(regex, url_str)
    if matches:
        return matches.group(1)
    return ""


# Function to get the transcript
def get_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        # You can format the transcript into plain text using TextFormatter
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript_list)

        return transcript_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Replace with the YouTube video ID
    url = "https://www.youtube.com/watch?v=96VlfN7ViyE"
    video_id = extract_video_id(url)

    print(f"Video ID: {video_id}")

    transcript = get_youtube_transcript(video_id)

    if transcript:
        print("Transcript:")
        print(transcript)
    else:
        print("Transcript not available for this video.")

