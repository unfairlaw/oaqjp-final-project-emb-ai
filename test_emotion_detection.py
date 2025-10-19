import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        case1 = "I am glad this happened"
        test1 = emotion_detector(case1)
        result = test1['dominant_emotion']
        self.assertEqual(result, 'joy')
    
    def test_anger(self):
        case2 = "I am really mad about this"
        test2 = emotion_detector(case2)
        result = test2['dominant_emotion']
        self.assertEqual(result, 'anger')

    def test_disgust(self):
        case3 = "I feel disgusted just hearing about this"
        test3 = emotion_detector(case3)
        result = test3['dominant_emotion']
        self.assertEqual(result, 'disgust')

    def test_sadness(self):
        case4 = "I am so sad about this"
        test4 = emotion_detector(case4)
        result = test4['dominant_emotion']
        self.assertEqual(result, 'sadness')
    
    def test_fear(self):
        case5 = "I am really afraid that this will happen"
        test5 = emotion_detector(case5)
        result = test5['dominant_emotion']
        self.assertEqual(result, 'fear')

if __name__ == '__main__':
    unittest.main()