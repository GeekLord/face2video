from moviepy import VideoFileClip
import datetime
import os

def add_sound(video_sound_path, video_no_sound_path):
    video_with_sound = VideoFileClip(video_sound_path)
    video_without_sound = VideoFileClip(video_no_sound_path)

    video_without_sound = video_without_sound.with_audio(video_with_sound.audio)

    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    video_without_sound.write_videofile(f"finished_videos/final_{current_datetime}.mp4", codec='libx264')

    os.remove(video_no_sound_path)
