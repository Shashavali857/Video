from flask import Flask, request, jsonify
from video_generator import generate_scene_videos
from combine_videos import merge_videos
import os

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Prompt missing"}), 400

    video_paths = generate_scene_videos(prompt)
    return jsonify({"videos": video_paths}), 200

@app.route('/merge', methods=['POST'])
def merge():
    merged_path = merge_videos()
    return jsonify({"final_video": merged_path})

if __name__ == '__main__':
    app.run(debug=True)
