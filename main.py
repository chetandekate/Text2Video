from flask import Flask, render_template, request, send_from_directory
from moviepy.editor import *
import os
import pyttsx3
from PIL import Image as PILImage  # This is to avoid conflict with the ImageClip

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET', 'POST'])
def index():
    video_path = None
    if request.method == 'POST':
        content = request.form['text'][:1000]  # Limit content to 1000 characters
        video_path = generate_video(content)
    return render_template('index.html', video_path=video_path)


@app.route('/videos/<path:filename>')
def download(filename):
    return send_from_directory(directory=os.path.join('static'), filename=filename)


def generate_audio_from_text(content):
    engine = pyttsx3.init()
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice', voice_id)
    audio_path = os.path.join(BASE_DIR, 'static', 'generated_audio.mp3')
    engine.save_to_file(content, audio_path)
    engine.runAndWait()
    return audio_path


def resize_image(image_path, output_path, size):
    with PILImage.open(image_path) as img:
        img_resized = img.resize(size, PILImage.LANCZOS)
        img_resized.save(output_path)


def generate_video(content):
    audio_path = generate_audio_from_text(content)
    audio_clip = AudioFileClip(audio_path)

    img_path = os.path.join(BASE_DIR, 'static', 'placeholder.jpg')
    resized_img_path = os.path.join(BASE_DIR, 'static', 'resized_placeholder.jpg')

    resize_image(img_path, resized_img_path, (640, 480))
    img_clip = ImageClip(resized_img_path, duration=audio_clip.duration).set_audio(audio_clip)

    video_path = os.path.join('static', 'generated_video.mp4')
    img_clip.write_videofile(video_path, codec="libx264", fps=24)

    return video_path.replace(BASE_DIR, '')


if __name__ == '__main__':
    app.run(debug=True)
