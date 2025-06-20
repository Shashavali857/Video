import moviepy.editor as mp
import os

def merge_videos():
    clips = []
    for i in range(1, 6):
        path = f"static/output/scene_{i}.mp4"
        clips.append(mp.VideoFileClip(path))

    final = mp.concatenate_videoclips(clips)
    merged_path = "static/output/final_video.mp4"
    final.write_videofile(merged_path, fps=24)
    return merged_path
