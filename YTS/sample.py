from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

summarization = pipeline("summarization")
link="https://www.youtube.com/watch?v=rFP7rUYtOOg"
link=link[32:] #to get the youtube video id 
subtitle = YouTubeTranscriptApi.get_transcript(link,languages=['en']) #to get the transcript of the video 

original_text=""
for i in subtitle:
    original_text+=i['text']

original_length=len(original_text)
summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)