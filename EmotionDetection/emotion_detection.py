'''
Module for performing emotion detection using Watson NLP API.
'''

import json
import requests

def emotion_detector(text_to_analyze):
    '''
    This code performs an emotion detection analysis on a specified text.
        Parameters:
            str
        Output:
            dict
    '''
    baseurl = 'https://sn-watson-emotion.labs.skills.network/'
    url = baseurl + 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers, timeout=60)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        json_response =  json_response['emotionPredictions'][0]['emotion']
        emotions = sorted(json_response.items(), key=lambda x: x[1],  reverse=True)
        dominant_emotion = emotions[0][0]
        emotions = dict(emotions)
        json_response['dominant_emotion'] = dominant_emotion
        return json_response

    json_response = json.loads(response.text)
    json_pattern = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
    none_result = {key: None for key in json_pattern}
    return none_result
