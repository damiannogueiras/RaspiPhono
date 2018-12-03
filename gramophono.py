import RPi.GPIO as IO
import time
import os
import pygame

IO.setwarnings(False)
IO.setmode(IO.BCM)

# button to add time when crank turn
buttonTimePin = 4  # fourth pin
# button to change folder music
buttonDiscPin = 17  # sixth pin

IO.setup(buttonTimePin, IO.IN, IO.PUD_UP)
IO.setup(buttonDiscPin, IO.IN, IO.PUD_UP)

current_time = 0
finish_time = 0
# arrays to store files and dirs
vinyls = []
all_songs = []
index_vinyls = 0
index_songs = 0
# boolean to enable play music
isRotating = False

# save the list of directory and songs
# directories -> vinyls
# mp3 files -> all_songs
def recopile_vinyls():
    global vinyls
    global all_songs
    # dir with folder with mp3 files
    path = "./Music"
    scandirs = os.scandir(path)

    for its in scandirs:
        # print(its.name)
        if its.is_dir():
            # print(its.path)
            subdirs = os.scandir(its.path)
            vinyls.append(its.name)
            # for each dir, one array with mp3 files
            songs = []
            for files in subdirs:
                # print(files.name)
                # create list with files of a directory
                songs.append(files.path)
            # all_songs is array of arrays
            all_songs.append(songs)
    # order alphabetic
    # vinyls.sort()


# every crank turn add one min
def addMin(pin):
    global finish_time
    # local var, to compare at the crank turn moment
    current_time = time.time()
    # every turn add 5 scs
    seconds = 60
    # if the gramaphono is rotating
    if finish_time > current_time:
        finish_time = finish_time + seconds
        print("plus turn")
    # else, the gramophono is stop
    else:
        finish_time = current_time + seconds
        # print("reset time")


# change directory, other disc
def changeDisc(pin):
    global index_vinyls
    global index_songs
    print("Change Disc")
    # first stop the music
    pygame.mixer.music.stop()
    # the next vinyl
    if index_vinyls < len(vinyls) - 1:
        index_vinyls += 1
    # or the first
    else:
        index_vinyls = 0
    index_songs = 0


def loadSong():
    global index_songs
    # load songs
    if index_songs < len(all_songs[index_vinyls]):
        pygame.mixer.music.load(all_songs[index_vinyls][index_songs])
        pygame.mixer.music.play()
        print("play " + str(all_songs[index_vinyls][index_songs]))
        index_songs += 1
    else:
        pygame.mixer.music.stop()

# events for the buttons
IO.add_event_detect(buttonTimePin, IO.RISING, addMin, bouncetime=200)
IO.add_event_detect(buttonDiscPin, IO.RISING, changeDisc, bouncetime=200)

# save the files at the array
recopile_vinyls()

# print(vinyls)
# print(all_songs)

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""

    # Initialize Everything
    # init display
    # screen = pygame.display.set_mode((468, 60))
    # pygame.display.set_caption('Raspiphono')
    # init mixer
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 1  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples (experiment to get right sound)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(0.5)
    # init pygame
    pygame.init()
    # Main Loop
    going = True
    while going:
        time.sleep(1)
        current_time = time.time()
        if finish_time > current_time:
            # print("REMAIN:" + str(int(finish_time) - int(time.time())))
            isRotating = True
        else:
            # print("STOP")
            isRotating = False
            # stop music
            pygame.mixer.music.stop()
        # print("Disc:" + str(vinyls[index_vinyls]))
        if (not pygame.mixer.music.get_busy()) and isRotating:
            loadSong()

    pygame.quit()

# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
