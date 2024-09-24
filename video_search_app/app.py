from flask import Flask
from flask import request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

video_titles = sorted([
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
])



@app.route('/videos',methods=["GET"])
def get_video():
    video = request.args.get('video')
    l = 0
    r = len(video_titles)-1
    while l <= r:
        m = (l+r)//2
        if video == video_titles[m]:
            return jsonify({'video':m}), 200
        elif video < video_titles[m]:
            r = m-1
        elif video > video_titles[m]:
            l = m+1
    return jsonify({'error':'video not found!'}), 400



if __name__ == '__main__':
    app.run(debug=True)
    