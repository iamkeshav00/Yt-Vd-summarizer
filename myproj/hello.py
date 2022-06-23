from flask import Flask , render_template , request
from youtube_transcript_api import YouTubeTranscriptApi

app=Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/ytlink",methods=['POST'])
def ytlink():
    return  request.form['ytlink']
if __name__=='__main__':
    app.debug=True
    app.run()