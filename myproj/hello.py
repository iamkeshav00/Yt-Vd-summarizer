from re import sub
from flask import Flask , render_template , request
from youtube_transcript_api import YouTubeTranscriptApi
from flask import jsonify

app=Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/ytlink",methods=['POST'])
def ytlink():
    link=request.form['ytlink'] #to get the youtube video link from the main webpage
    link=link[32:] #to get the youtube video id 
    subtitle = YouTubeTranscriptApi.get_transcript(link,languages=['en']) #to get the transcript of the video 
    return jsonify(subtitle) #this function cannot return a list so i have to make it in the form of a js object 



if __name__=='__main__':
    app.debug=True
    app.run()