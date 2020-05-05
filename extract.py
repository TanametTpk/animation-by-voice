from contextlib import closing
from PIL import Image
import subprocess
import numpy as np
import re
import math
from shutil import copyfile, rmtree
import os
import argparse

def copyFrame(inputFrame,outputFrame):
    src = TEMP_FOLDER+"/frame{:06d}".format(inputFrame+1)+".jpg"
    dst = TEMP_FOLDER+"/newFrame{:06d}".format(outputFrame+1)+".jpg"
    if not os.path.isfile(src):
        return False
    copyfile(src, dst)
    if outputFrame%20 == 19:
        print(str(outputFrame+1)+" time-altered frames saved.")
    return True

def inputToOutputFilename(filename):
    dotIndex = filename.rfind(".")
    return filename[:dotIndex]+"_ALTERED"+filename[dotIndex:]

def createPath(s):
    #assert (not os.path.exists(s)), "The filepath "+s+" already exists. Don't want to overwrite it. Aborting."

    try:  
        os.mkdir(s)
    except OSError:  
        assert False, "Creation of the directory %s failed. (The TEMP folder may already exist. Delete or rename it, and try again.)"

def deletePath(s): # Dangerous! Watch out!
    try:  
        rmtree(s,ignore_errors=False)
    except OSError:  
        print ("Deletion of the directory %s failed" % s)
        print(OSError)

parser = argparse.ArgumentParser(description='Modifies a video file to play at different speeds when there is sound vs. silence.')
parser.add_argument('--input_file', type=str,  help='the video file you want modified')
parser.add_argument('--output_file', type=str, default="", help="the output file. (optional. if not included, it'll just modify the input file name)")
parser.add_argument('--frame_rate', type=float, default=30, help="frame rate of the input and output videos. optional... I try to find it out myself, but it doesn't always work.")
parser.add_argument('--frame_quality', type=int, default=3, help="quality of frames to be extracted from input video. 1 is highest, 31 is lowest, 3 is the default.")

args = parser.parse_args()

# declare global variable
frameRate = args.frame_rate
FRAME_QUALITY = args.frame_quality
TEMP_FOLDER = "extract_results"

INPUT_FILE = args.input_file

# check input file
assert INPUT_FILE != None , "why u put no input file, that dum"

# create output file path
if len(args.output_file) >= 1:
    OUTPUT_FILE = args.output_file
else:
    OUTPUT_FILE = inputToOutputFilename(INPUT_FILE)
    
createPath(TEMP_FOLDER)

# extract frame
command = "ffmpeg -i "+INPUT_FILE+" -qscale:v "+str(FRAME_QUALITY)+" "+TEMP_FOLDER+"/%d.jpg -hide_banner"
subprocess.call(command, shell=True)