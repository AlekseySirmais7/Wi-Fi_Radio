from flask import Flask, render_template
import datetime
import os
import random
from mutagen.mp3 import MP3

def getSong():
	names = os.listdir('./static')
	random_song = random.choice(names)
	while not '.mp3' in random_song:
		random_song = random.choice(names)
		
	#print(names)
	print('========================\n song:'+random_song+'\n========================')
	return random_song
#for name in names:
    #fullname = os.path.join(dirName, name) # получаем полное имя
    #if os.path.isfile(fullname):
 #   print (name)

		


app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   song=getSong()
   audio = MP3('static/'+song)
   time_of_song = int(audio.info.length+1)
   print('Song time: '+(str(int(time_of_song/60)))+' minutes and '+str(int((time_of_song%60)))+' seconds')
   templateData = {
      'title' : 'Wi-Fi Radio',
      'time' : timeString,
      'src_song' : 'static/'+song,
      'title_song': song[:-4],
      'leng': time_of_song*1000, #milisecond for reload
      'song_min' : int(time_of_song/60),
      'song_sec': int((time_of_song%60))

      }
   
   return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)