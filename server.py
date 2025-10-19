'''
Executing this function initiates the application of emotion detector
to be executed over the Flask app and deployed on
localhost:5000
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion detector')

@app.route('/emotionDetector')

def sent_detector():
    '''
    Receives text from the HTML interface and
    executes emotion detector over it.
    The output shows the prediction on the emotion
    alongside each confidence score, as well as
    the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant = response.pop('dominant_emotion')
    if dominant is not None:
        result = str(response).strip('{}')
        return f"""For the given statement, the system response is {result}.
The dominant emotion is {dominant}."""
    return "Invalid text! Please try again!"
@app.route("/")

def render_index_page():
    '''
    This function initiates the rendering of the main application
    over to Flask.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
