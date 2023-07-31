from flask import Flask, render_template, Response, request, jsonify
import cv2


from hand_gesture2.final import hand_gesture
from llm.quiz import quiz
from llm.doubt import doubt


app = Flask(__name__)


cap = cv2.VideoCapture(0)

# funstions
def quiz_cv():
     prompt = "save water"
     question,answer= quiz(prompt)
     return question,answer

def gesture_recognition():
    while True:
        frame = hand_gesture(cap)  # Call the hand_gesture function to process the frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Pages of the website with templates
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meeting')
def meeting():
    return render_template('meeting.html')

# @app.route('/classroom')
# def classroom():
#     return render_template('classroom.html')

# @app.route('/quiz')
# def quiz_m():
#     question, answer= quiz_cv()
#     return render_template('quiz.html', question=question, answer=answer)

# @app.route('/doubt')
# def doubt_m():
#    return render_template('doubt.html')



# # other endpoints of the web without template
# @app.route('/get_doubt', methods=['POST'])
# def get_doubt_from_user():
#     topic = request.form['topic']
#     doubt_result = doubt(topic)
#     return jsonify(doubt_result) 

# @app.route('/video_feed')
# def gesture_recog():
#     return Response(gesture_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed')
def video_feed():
    return Response(gesture_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)





# import cv2
# from flask import Flask, Response, render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# camera = cv2.VideoCapture(0)

# def generate_frames():
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)



