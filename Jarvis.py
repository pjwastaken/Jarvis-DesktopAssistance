import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		print("Good Morning PJ")
		speak("Good Morning PJ")

	elif hour>=12 and hour<18:
		print("Good AfterNoon PJ")
		speak("Good AfterNoon PJ")

	else:
		print("Good Evening! PJ")
		speak("Good Evening! PJ")

	print("Hey I am Jarvis Sir,Please Tell Me how may I help You PJ")
	speak("Hey I am Jarvis Sir,Please Tell Me how may I help You PJ")

def takeCommand():

	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		#r.pause_threshold=0.8 for stop and listen your voice
		r.energy_threshold=4000
		audio=r.listen(source)

	try:
		print("Recognizing....")
		query=r.recognize_google(audio, language='en-in')
		print("User said:", query)

	except Exception as e:
		#print(e)"
		print("Sorry I didn't catch that,Say that again Please...")
		speak("Sorry I didn't catch that,Say that again Please...")
		return "None"
	return query

def sendEmail(to, content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('prajwaljadhav300@gmail.com','************')
	server.sendmail('prajwaljadhav300@gmail.com',to,content)
	server.close()

if __name__ == '__main__':
	wishMe()
	while True:
	#if 1:
		query=takeCommand().lower()

		if 'wikipedia' in query:
			speak("Searching Wikipedia")
			query=query.replace("wikipedia","")
			results=wikipedia.summary(query,sentences=3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'play music' in query:
			music_dir='D:\\mysongs'
			songs=os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs))

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")


		elif 'open google' in query:
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")

		elif 'open spotify' in query:
			webbrowser.open("spotify.com")

		elif 'open facebook' in query:
			webbrowser.open("facebook.com")

		elif 'show weather' in query:
			webbrowser.open("accuweather.com")

		elif 'open instagram' in query:
			webbrowser.open("instagram.com")

		elif 'open gmail' in query:
			webbrowser.open("gmail.com")

		elif 'my birthday' in query:
			print("your birthday is on 15 th March")
			speak("your birthday is on 15 th March")
			

		elif 'brother name' in query:
			print("I know you told me about your brother ,his name is Atharva")
			speak("I know you told me about your brother ,his name is Atharva")

		elif 'the time' in query:
			strTime=datetime.datetime.now().strftime("%H:%M:%S")
			print(strTime)
			speak(strTime)

		elif 'github account' in query:
			webbrowser.open("github.com/pjwastaken")

		elif 'linkedin' in query:
			webbrowser.open("linkedin.com/feed")

		elif 'pubg lite' in query:
			pubgpath="C:\\Program Files (x86)\\PUBGLite\\Launcher.exe"
			os.startfile(pubgpath)

		elif 'chrome' in query:
			chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			os.startfile(chromepath)

		elif 'mail to omkar' in query:
			try:
				print("What should I say?")
				speak("What should I say?")
				content=takeCommand()
				to="omkarraskar20@gmail.com"
				sendEmail(to, content)
				print("Email has been sent!")
				speak("Email has been sent!")


			except Exception as e:
				print(e)
				speak("Sorry I can't sent an mail")


		elif 'mail to yash' in query:
			try:
				print("What should I say?")
				speak("What should I say?")
				content=takeCommand()
				to="yashgarole1999@gmail.com"
				sendEmail(to, content)
				print("Email has been sent!")
				speak("Email has been sent!")


			except Exception as e:
				print(e)
				speak("Sorry I can't sent an mail")


		elif 'mail to aditya' in query:
			try:
				print("What should I say?")
				speak("What should I say?")
				content=takeCommand()
				to="adityamankar09@gmail.com"
				sendEmail(to, content)
				print("Email has been sent!")
				speak("Email has been sent!")


			except Exception as e:
				print(e)
				speak("Sorry I can't sent an mail")

		elif 'mail to papa' in query:
			try:
				print("What should I say?")
				speak("What should I say?")
				content=takeCommand()
				to="gorakhj009@gmail.com"
				sendEmail(to, content)
				print("Email has been sent!")
				speak("Email has been sent!")


			except Exception as e:
				print(e)
				speak("Sorry I can't sent an mail")


		elif 'shutdown' in query:
			print("Jarvis system is getting off,")
			speak("Jarvis system is getting off")
			print("Hope you enjoyed the time we spend... ")
			speak("Hope you enjoyed the time we spend... ")
			print("Bye PJ!")
			speak("Bye PJ!")
			break











