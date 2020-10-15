import requests
import json
import speech_recognition as sr 
import subprocess
# from gtts import gTTs
print("Speak Anything:")


def get_response(val):
	url = 'http://localhost:5005'
	data = json.dumps({"sender": "Rasa","message": val})
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	res = requests.post(url+'/webhooks/rest/webhook', data= data, headers = headers)
	res = res.json()
	out = res[0]['text']
	return out

def get_text():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio  = r.listen(source)
		try:
			text = r.recognize_google(audio)
			print("You: ",text)
			return text
		except:
			print("sorry could not Recognize your voice")
			return -1

text = ''


import pyttsx3
def text_to_speech2(text):
	engine = pyttsx3.init()
	# voices = engine.getProperty('voices')
	# engine.setProperty('voice', voices[1].id)
	# engine.setProperty('volume',0.9)
	engine.say(text);
	engine.runAndWait()

def text_to_speech(text):
	myobj = gTTs(text=text, lang='en')
	myobj.save('wl.mp3')
	subprocess.call(['mpg321','wl.mp3','--play-and-exit'])

while text != "stop":

	text = get_text()
	if text != -1:
		response = get_response(text)
		print("Chatbot:", response)
		text_to_speech2(response)
	else:
		pass


# val = input('Your Input: ')
# print("Chatbot:", out)
