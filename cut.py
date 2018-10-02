# Importing required packages
import glob # finding all .mp4 files
import numpy as np # creating array for time_table
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip # cutting videos
from moviepy.editor import VideoFileClip # video duration

# Get the duration and calculate the time_table
def get_time_table(clip_name):
    clip = VideoFileClip(clip_name+'.mp4')
    duration = clip.duration
    split = (duration - (duration % 30)) / 30
    step = duration / (split)
    time_table = np.arange(0, duration, step-0.0001)
    print("time_table generated success!")
    return time_table

# Extract videos using time_table
def extract_video(clip_name):
    # get time_table
    time_table = get_time_table(clip_name)

    # loop for making sub-videos
    for i, v in enumerate(time_table):
        if v != time_table[-1]:
            target_name = clip_name+'-'+str(i+1)+'.mp4'
            ffmpeg_extract_subclip(clip_name+'.mp4', time_table[i], time_table[i+1], targetname=target_name)
            print("subvideo-"+str(i+1)+" generated success!")

# Get all the .mp4 filename and store in name_list
name_list = []
for i in glob.glob('*.mp4'):
    name_list.append(i.split('.mp4')[0])

# Extract_video
for i in name_list:
    extract_video(i)
    print("Successfully Cut Video for: " + i)
