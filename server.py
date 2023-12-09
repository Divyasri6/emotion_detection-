''' Executing this function initiates the application of emotion detection to be executed 
    over the Flask channel and deployed on localhost:8080.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app=Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotions over it using emotion_detector()
        function. The output returned shows the dominant_emotion and individual emotion score.
    '''
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    if response is None:
        return "Invalid text! Please try again!."
    dominant_emotion=response['dominant_emotion']
    return f"For the given statement, the system response is 'anger': {response['anger']},\
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} \
    and 'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}."
@app.route("/")
def render_index_page():
    ''' initial html static page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
