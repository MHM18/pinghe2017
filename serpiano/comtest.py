import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

song1 = ['1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']
songs=[]

f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')

for row in rows:
    songs.append(row.split(','))


for p in ports:
    print (p[1])
    if "Serial" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")


def run():
    action = "empty"
    while action != "q":
        print ('select which song do you want to play ? 1,2 q and others for quit')
        action = input("> ")
        song_id=int(action)-1
        for notes in songs[song_id]:
            ser.write(notes.encode())
            print ("send:"+notes)
            time.sleep(1)
       
       


run()
