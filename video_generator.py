import moviepy.editor as mp
import os

def generate_scene_videos(prompt):
    os.makedirs("static/output", exist_ok=True)
    paths = []

    for i in range(5):
        clip = mp.TextClip(f"{prompt} - Scene {i+1}", fontsize=50, color='white', bg_color='black', size=(720, 480))
        clip = clip.set_duration(5)
        filename = f"static/output/scene_{i+1}.mp4"
        clip.write_videofile(filename, fps=24)
        paths.append(filename)

    return paths
